
import json
import boto3
import pandas as pd
from io import StringIO
from datetime import datetime
import DATA_PARSER


# S3 resource and client
s3_client = boto3.client('s3')
s3 = boto3.resource('s3')

def load_data(bucket_name, prefix):
    """
    buckect_name: bucket name where input data was loaded
    prefix: prefix name where input data was loaded

    Function reads and loads data in manageable chunk sizes to accomoate for large files. Then it returns concatanated dataframe.

    """
    # Retrieves object from s3 location
    obj = s3_client.get_object(Bucket=bucket_name, Key=prefix)
    
    # Choosing columns to be part of analysis
    use_cols = ['event_list', 'product_list', 'referrer']

    # Read tsv file aand create iterator
    df_chunk = pd.read_csv(obj['Body'], sep='\t', usecols=use_cols, chunksize = 5)
    
   
    chunk_list = []
    # Parse iterator into Chunk dataframes to process large datasets if needed and append result to chunk list 
    for chunk in df_chunk:
        if chunk.empty == True:
            print("There are no results that match your criteria. Dataframe is empty")
        
        else:
            print("Dataframe was loaded.")
        
        chunk_list.append(chunk)
    
    df_concat = pd.concat(chunk_list)
    
    return df_concat
    
def upload_file_exp_to_s3(df, bucket_name, file_name, destination):

    """
    df: dataframe to upload
    bucket_name: bucket name where output would be uploaded
    file_name: name of output file
    destination: object key where the output would be uploaded

    """
    
    csv_buffer = StringIO()
    
    #Write dataframe to buffer
    
    df.to_csv(csv_buffer, index=False)
    
    # Check if dataframe is empty. If not then proceed to upload file to S3 location.
    
    if df.empty == True:
        
        print("There are no results that match your criteria. Nothing was uploaded to S3.")
        
    else:
        
       #Write buffer to S3 object
       
        s3.Object(bucket_name, destination + file_name).put(Body=csv_buffer.getvalue())
        
        print("Output Summary {} file was Uploaded Successfully.")
    
 
def main():
    
    # Variables to get bucket name, prefix, output filename and destination of output file
    bucket_name = 'takehome-martin'
    prefix = 'data/data.tsv'
    destination = 'data/output/'
    file_name =  datetime.now().strftime("%Y-%m-%d")+"_"+"SearchKeyWordPerformance"+".tab"
    
    df_concat = load_data(bucket_name, prefix)
    
    # Expand 'product_list' attribute to get Revenue
    df_concat[['Category', 'Product Name', 'Number of Items', 'Revenue', 'Custom Event']]= df_concat['product_list'].str.split(';', expand=True)
    
    # Apply data parsing to 'referrer' attribute to extract 'Search Engine'
    
    df_concat['Search Engine Domain'] = df_concat['referrer'].apply(lambda x: DATA_PARSER.ParseSearchUrls.search_engine(x)).str[0]
    
    # Apply data parsing to 'referrer' attribute to extract 'Search Keyword'
    df_concat['Search Keyword'] = df_concat['referrer'].apply(lambda x: DATA_PARSER.ParseSearchUrls.key_word(x)).str[0]
    
    # Fill in NaN with 'Other' string if 'Search Engine' (Google, Yahoo, MSN) not found
    df_concat['Search Engine Domain'] = df_concat['Search Engine Domain'].fillna('Other')
    df_concat['Search Keyword'] = df_concat['Search Keyword'].fillna('Other')
    
    # Finally filtering data for confirmed purchases 'event_list'  == 1.0 and create ouput dataframe
    df_concat = df_concat[df_concat['event_list'] == 1.0]

    # Create ouput dataframe with required attributes

    output_cols = ['Search Engine Domain', 'Search Keyword', 'Revenue']

    output_df = df_concat[output_cols]
    
    print(output_df)
    
    
    print(upload_file_exp_to_s3(output_df, bucket_name, file_name, destination))
    
def lambda_handler(event, context):
    # TODO implement
    main()
    return {
        'statusCode': 200,
        'body': json.dumps('Pipeline ran successfully!')
    }
