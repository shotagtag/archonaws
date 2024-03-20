# インスタンスメタデータでどのようなデータが取得できるか確認してみましょう
- EC2のインスタンスメタデータは、インスタンス個々のEC2情報を、個々のインスタンス内部(OS側)から参照できる機能です。
- インスタンスメタデータを活用できる場面はさまざまあり、例えば次のような要件に活用できます。
  - ユーザデータの処理過程(初期セットアップ)で、インスタンスが起動しているリージョンやアベイラビリティゾーンを含める形で、OS設定としてのホスト名を設定したい。
  - バックアップファイルの生成処理で、インスタンスIDをファイル名の一部に使いたい。  
- どのような情報が取得できるのか詳細はドキュメントも参考にしてください。
  - [インスタンスメタデータのカテゴリ] (https://docs.aws.amazon.com/ja_jp/AWSEC2/latest/UserGuide/instancedata-data-categories.html)
- インスタンスメタデータの取得に特別なIAM権限は必要ありません。
- インスタンスメタデータで取得できる情報は、自身のインスタンス情報のみです(例えばインスタンスAから、インスタンスBのメタデータを取得するｊこことはできません。)

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
