import boto3
import sys

bucket_name = 'labsdk-bucket-XXXXX' # S3 バケット名
region = 'ap-northeast-1'  # 作成するAWSリージョン

# SDKでS3 リソースオブジェクトを作成
s3 = boto3.resource('s3')

# バケットを作成する関数 create_bucket を作成
def create_bucket(name, region):
    try:
        if region == 'us-east-1':
            s3.create_bucket(Bucket=name)
        else:
            s3.create_bucket(Bucket=name, CreateBucketConfiguration={'LocationConstraint': region})
        print(f"バケット '{name}' をリージョン '{region}' に作成しました！")
    except Exception as e:
        print(e)

# 関数を実行
create_bucket(bucket_name, region)
