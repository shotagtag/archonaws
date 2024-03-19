import boto3
import os

bucket_name = 'labsdkbucket-XXXXX' # S3 バケット名
file_name = 'HappyFace.jpg' # アップロードするファイル
s3_key_name = 'HappyFace.jpg' # S3 にアップロードする際の名前

# S3クライアントオブジェクトの作成
s3_client = boto3.client('s3')

# ファイルをアップロードする関数 upload_file_to_s3 を作成
def upload_file_to_s3(file_name, bucket, s3_key_name):
    try:
        s3_client.upload_file(file_name, bucket, s3_key_name)
        print(f"'{file_name}' をバケット '{bucket}' にアップロードしました。")
    except Exception as e:
        print(e)

# 関数実行
upload_file_to_s3(file_name, bucket_name, s3_key_name)
