# インスタンスメタデータでどのようなデータが取得できるか確認してみましょう
## 概要
- EC2のインスタンスメタデータは、インスタンス個々のEC2情報を、個々のインスタンス内部(OS側)から参照できる機能です。
- インスタンスメタデータを活用できる場面は様々あり、例えば次のような場面で活用できます。
  - 初期セットアップ中、インスタンスが起動しているリージョンやアベイラビリティゾーンを含めたOSのホスト名を設定したい。
  - バックアップファイルの生成処理で、インスタンスIDをファイル名の一部に使いたい。  
- どのような情報が取得できるのか詳細はドキュメントも参考にしてください。
  - [インスタンスメタデータのカテゴリ] (https://docs.aws.amazon.com/ja_jp/AWSEC2/latest/UserGuide/instancedata-data-categories.html)

### 制約等
- インスタンスメタデータで取得できる情報は、自身のインスタンス情報のみです(例えばインスタンスA内部から、インスタンスBのメタデータを取得することはできません)。
- インスタンスメタデータの取得に特別なIAM権限は必要ありません。
- インスタンスメタデータにはv1,v2があり、v2を使用する場合にはセキュリティトークンが必要です。詳細はドキュメントも参考にしてください。
  - [IMDSv2 の使用] (https://docs.aws.amazon.com/ja_jp/AWSEC2/latest/UserGuide/configuring-instance-metadata-service.html)

## 🛠️ 事前準備 🛠️
- ラボ1の環境にアクセスし、マネジメントコンソールでEC2のインスタンス一覧ページへアクセスします。
- Command Host にセッションマネージャーで接続します。

## 🚀 CommandHostのインスタンスメタデータを取得してみよう
- インスタンスメタデータ(v2)の照会に必要なトークンを取得します。取得したトークンはメタデータの取得リクエストにHTTPヘッダーに含めるようにします。
```
TOKEN=`curl -s -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600"`
```

- インスタンスメタデータサービス( http://169.254.169.254 )にアクセスし、EC2インスタンスIDを確認
```
curl -w'\n'  -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/meta-data/instance-id
```

- EC2インスタンスがどのアベイラビリティゾーンで起動しているのか確認
```
curl -w'\n'  -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/meta-data/placement/availability-zone
```

- EC2インスタンスがどのリージョンで起動しているのか確認
```
curl -w'\n'  -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/meta-data/placement/region
```

- EC2インスタンスに関連づけられているパブリックIPアドレスを確認したい
```
curl -w'\n'  -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/meta-data/public-ipv4
```

- インスタンスタイプを確認
```
curl -w'\n'  -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/meta-data/instance-type
```
