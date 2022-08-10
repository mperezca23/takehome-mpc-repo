# takehome-mpc-repo

## Table of Contents
1. [General Info](#general-info)
2. [Technologies](#technologies)
3. [Installation](#installation)
4. [Collaboration](#collaboration)

### General Info
***
This serverless python application is a lambda function in AWS that takes a tsv input file and outptus a tsv file based on the following business requirements.

Assumptions:

- Data would fe filtered for confirmed purchases or 'event_list'  == 1.0 
- I'm taking the 'product_list' attribute and parsing it out to come up with Number of Items and Total Revenue.   
- I would use 'referrer' attribute to determine the Search Engine domains
- I would use the 'referrer' attribute to determine the Search Keyword
- 'Search Engines Domain' are limited to Google, Yahoo and MSN to calculate revenue.  However, if there are no matches for determined search engines then, I categorized the revenue under “OTHER”.


### Screenshot
![Image text](https://www.united-internet.de/fileadmin/user_upload/Brands/Downloads/Logo_IONOS_by.jpg)
## Technologies
***
A list of technologies used within the project:
* [AWS CodeBuild](https://aws.amazon.com/codebuild/)
* [AWS Lambda](https://aws.amazon.com/lambda/)
* [AWS S3](https://example.com)
* [GitHub](https://github.com)
## Installation
***
A little intro about the installation. 
```
1. Create empty Lambda function - Update IAM permissions for Lambda to access 
2. Create github repo to host python code and clone repo locally
    - lambda_function.py - lambda python code to be executed
    - requirements.txt - required libraries needed for python application
    - buildspec.yml - File that CodeBuild would use to install, build, post_build instructions to create zip lambda deployment package
    - DATA_PARSER.py - Helper function class to parse data
3. 
$ git clone https://example.com
$ cd ../path/to/the/file
$ npm install
$ npm start
```
Side information: To use the application in a special environment