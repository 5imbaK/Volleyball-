import pandas as pd
import boto3

pd.set_option('display.max_rows', 10)  
pd.set_option('display.max_columns', 20)  

try:
   
    excel_path = '/Users/halokanengiser/Desktop/library.xlsx'
    df = pd.read_excel(excel_path)
    print(df.head(10))  
except Exception as e:
    print(f"Error: {e}")

s3_client = boto3.client('s3', region_name='us-east-1')

bucket_name = 'spikedrills'
object_name = 'library.xlsx'

try:
    response = s3_client.upload_file(excel_path, bucket_name, object_name)
    print("File uploaded successfully to S3")
except Exception as e:
    print(f"Error uploading file to S3: {e}")