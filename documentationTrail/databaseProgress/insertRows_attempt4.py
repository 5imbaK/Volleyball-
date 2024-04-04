import pandas as pd
import boto3
import os

os.environ['AWS_DEFAULT_REGION'] = 'us-east-1'
os.environ['AWS_SECRET_ACCESS_KEY'] = 'SlWltRDg+Nal59TIgc7Fs+dko54cve5WSJ9iLDJW'
os.environ['AWS_ACCESS_KEY_ID'] = 'AKIA3FLDYCJ24FAKUIXD'

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('tempor')

df = pd.read_excel('library.xlsx')
print(df.head())

chunk_size = 100

for i in range(0, len(df), chunk_size):
    chunk = df.iloc[i:i + chunk_size]
    for index, row in chunk.iterrows():
        table.put_item(
            Item = {
                'Drill Name': row['Name of Drill'],
                'Catagory': row['Catagory']
            }
        )

'''for index, row in chunk.iterrows():
        table.put_item(
            Item = {
                'Drill Name': row['Name of Drill'],
                'Catagory': row['Catagory']
            }
        )'''