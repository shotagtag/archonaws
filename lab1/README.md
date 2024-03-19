# AWS SDK を 使ってみましょう
AWSSDKを使用すると、さまざまなプログラム言語からAWSのサービス(API)を呼び出して操作することができます。
- 参考 : [AWS での構築のための SDK とプログラミングツールキット](https://aws.amazon.com/jp/developer/tools/)
- python のサンプルプログラムを使用して AWSSDKを体験してみましょう！

## 🛠️ 事前準備 🛠️

### ユーザーを切り替える
- 権限の関係で、ユーザを ssm-user から ec2-user に切り替えます。次のコマンドを実行します。
```
sudo su - ec2-user
```

### 必要なツールをインストール ###
- 次のコマンドを実行して、必要なツールをインストールします。
```
sudo yum install -y git pip
```
- python用の AWS SDK (boto3) をインストールします。
  - 参考 : [Boto3 documentation — Boto3 Docs 1.26.65 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
```
pip3 install boto3
```

- サンプルプログラムを clone します。
```
git clone https://github.com/shotagtag/archonaws.git
cd archonaws/lab1/
```

## 🚀 S3 を python SDK で操作する 🚀

###  S3 バケットの作成
- S3バケットを作成するサンプルプログラムを確認してみましょう。
```
cat create_s3bucket.py
```

- バケットを作成するリージョンと、作成するS3バケットの名前をコマンドで書き換えます。
  - メモ帳などで、次のコマンドの `作成したいバケット名` をバケット名に書き換えて実行してください。
  ```
  sed -i -e "s/labsdkbucket-XXXXX/作成したいバケット名/g" create_s3bucket.py
  ```
  - メモ帳などで、次のコマンドの `リージョン名` をリージョン名(ap-northeast-1 など)に書き換えて実行してください。
  ```
  sed -i -e "s/REGION_NAME/リージョン名/g" create_s3bucket.py
  ```

- プログラムを実行します。実行後、S3バケットが作成されたかマネジメントコンソールで確認してみましょう。
```
python3 create_s3bucket.py
```

### S3 バケットにオブジェクトをアップロードする
- バケットにHappyFace.jpgをアップロードするサンプルプログラムを確認してみましょう。
```
cat upload_file.py
```

- アップロードするバケットをコマンドで書き換えます。
  - メモ帳などで、次のコマンドの `アップロードするバケット名` をバケット名に書き換えて実行してください。
  ```
  sed -i -e "s/labsdkbucket-XXXXX/アップロードするバケット名/g" create_s3bucket.py
  ```

- プログラムを実行します。実行後、ファイルがアップロードされたかマネジメントコンソールで確認してみましょう。
```
python3 file_upload.py
```
