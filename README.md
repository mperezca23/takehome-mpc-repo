# takehome-mpc-repo

## Table of Contents
1. [General Info](#general-info)
2. [Technologies](#technologies)
3. [Installation](#installation)

### General Info
***
This serverless python application is a lambda function in AWS that takes a tsv input file and outptus a tsv file based on the following business requirements.

Assumptions:

- Data would be filtered for confirmed purchases or 'event_list'  == 1.0 
- I'm taking the 'product_list' attribute and parsing it out to come up with Number of Items and Total Revenue.   
- I would use 'referrer' attribute to determine the Search Engine domains
- I would use the 'referrer' attribute to determine the Search Keyword
- 'Search Engines Domain' are limited to Google, Yahoo and MSN to calculate revenue.  However, if there are no matches for determined search engines then, I categorized the revenue under “OTHER”.


### Application Design Architecture
![Image text](https://takehome-martin.s3.us-east-1.amazonaws.com/sys_design/sys_design_mpc.PNG?response-content-disposition=inline&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJGMEQCICSWZZ84lJdLzNuNrwmz2rXumtNq0oaKMfq2EnNPmfG6AiBfpRBmfDRjTO1JYp%2Bv2Ph%2BDSU71nGAVPbFx%2FXGIHUUPiroAghOEAEaDDQ1NTc4NjkzNzIwOCIMRglX7vlvpwrny7KZKsUC3%2FJawb4F%2FZccfEOqaXMqdL%2BWTELq9DGvkVo0HJSOiWtvyDb0Hk0qFkJMYnfCQi21DEsZAYl0W1pdrv5mCsQ8%2F13D6fIJKxdGvMFC3FxWOSGVV3%2FGCrXpN1x8bjru4SN4J4tcaYYDCSbRaOpS89VlMnMjUF7lbpMzei%2Ff6Ha397L%2BrBiaecSdLarVtb9tbrfX%2Fj7Zm%2Bgf3LqijMcFzyKXs06ykLqsrbptswDkqWXE1D6yniqggyiXIS0Gk4ulZYDX8l4h5TbaqsNR3UbLPbqVgvPRDXt04N5v6P7h269%2FX3pJOYbW%2BGpq7qGbM1urYwAy3%2B3%2B6s7k7HKrOOVXxHsUxFeFCXzYSPEplG0SsLLA3EVzMrt7ESSuuqTTooRr2pNtRseDNNrVN77Kjlsu1VH2B9uJSfXt9KhPdzV3F0ct7EXXfxZi2DCpvNCXBjq0AgoVdGEH46v2fUIYa7VdAoOQz9SQBd7fo5HojGRyESxzDvdDuDWBqHMGBafDwz9Cf0ckQSsF%2BS9HeVUbkh6SQVvpamCFpA8xvBIpPYt5K9PiU14YQPZuEpez7MFx8oFucJ8BRrljcgrUrfgsML1y3GPzohEpumvuT9v8XeAYZkZ0BHxipnTGIfXAI1tAISnAjlaTHzETGZ1h%2F0I2RpJEJUUfWH9j9ogFOP%2BT4%2BCluJjqBHduYvmu%2FNRIc0GflKStgOvajhjyGOLhRPJcXleXDvUa0skr9FdVySp4LIfAZozbIaFqvITNtoSBpLYITyxupJMHDH6bnfh%2FYXeR%2FCqGSK%2FohKuGxJRL2nNnkd%2BKTi%2Faf3s2e%2BJlktbl6Z0zfeYYnARl8IpzW344l%2Bf2D9U03kK%2BWSby&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20220810T211054Z&X-Amz-SignedHeaders=host&X-Amz-Expires=43200&X-Amz-Credential=ASIAWUHYEXN4OKN63SGG%2F20220810%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=3a34a5c753b45e699435f87cea4a2ad2a977e7e516f9f0eec04967230f411089)
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
1. Create empty Lambda function - Update IAM permissions for Lambda to access S3 
2. Create github repo to host python code and clone repo locally:
    Repo Content:
    - lambda_function.py - lambda python code to be executed
    - requirements.txt - required libraries needed for python application
    - buildspec.yml - File that CodeBuild would use to install, build, post_build instructions to create zip lambda deployment package
    - DATA_PARSER.py - Helper function class to parse data
3. Create CodeBuild project - Go to AWS Console and connect to Github repo. Add IAM permissions to access lambda and make changes 

```