import pandas as pd
import awswrangler as aws

aws.dynamodb.put_df(
    df = pd.read_excel('library.xlsx'),
    table_name='Matrix'
)