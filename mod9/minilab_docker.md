# コンテナでアプリケーションを起動してみましょう🚀

Lab1 の Command Host に セッションマネージャーでログインし、ターミナルで以下のコマンドを順に実行します。

- ラボ権限の関係で root ユーザに昇格します。
```
sudo su -
```

- 必要なソフトウェアをインストールします。
```
yum -y install docker git
```

- web2048 を git クローンします。
```
git clone https://github.com/gabrielecirulli/2048
cd 2048
```

- Dockerfile を作成します。webサーバーのコンテナをベースとして、web2048アプリケーションを含めてビルドする手順を定義します。
```
cat << EOF > Dockerfile
FROM nginx:latest

COPY . /usr/share/nginx/html

EXPOSE 80
EOF
```

- Docker サービスを起動します。
```
service docker start
```

- コンテナイメージをビルドします。Dockerfileに基づき、コンテナイメージがビルドされます。
```
docker build -t web2048 .
```

- ビルドされたコンテナイメージを確認します。
```
docker images
```

- コンテナイメージからコンテナを起動します
```
docker run -d -it -p 80:80 web2048
```

- EC2インスタンスのパブリックIPアドレスをメタデータから確認します。得られたIPアドレスにウェブブラウザから「http://xx.xx.xx.xx」で接続してみてください。
```
TOKEN=`curl -s -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600"`
curl -w'\n'  -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/meta-data/public-ipv4
```
