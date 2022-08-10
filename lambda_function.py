
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
    obj = s3_client.get_object(Bucket=bucket_name, Key=prefix)
    
    
    use_cols = ['event_list', 'product_list', 'referrer']
    df_chunk = pd.read_csv(obj['Body'], sep='\t', usecols=use_cols, chunksize = 5)
    
   
    chunk_list = []

    for chunk in df_chunk:
        if chunk.empty == True:
            output_exp_msg = "There are no results that match your criteria. Dataframe is empty"
        
            return output_exp_msg
        else:
            print("Dataframe was loaded.")
        
        chunk_list.append(chunk)
    
    df_concat = pd.concat(chunk_list)
    
    return df_concat
    
def upload_file_exp_to_s3(df, bucket_name, file_name, destination):
    
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
