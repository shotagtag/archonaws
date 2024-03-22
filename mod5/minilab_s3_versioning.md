# S3 バージョニングを触ってみよう

## ⚒️ 前準備 ⚒️
- テキストファイル arch-s3-mini-lab.txt の中身を確認します。（インストラクターから配布します。）
- ラボ7を開き、 S3 のサービス画面へ移動します。

## (1)バージョニングを有効化したバケットを作成
- 「バケットを作成」をクリックします。バケット作成画面で以下の設定を行います。
  - バケット名 : ‘my-s3-bucket-[今日の日付]-[お名前]’ , 例 my-s3-bucket-20230101-taro
  - バケットのバージョニング : 「有効にする」へ変更します。
  - 「バケットの作成」をクリックします。

## (2)バケットにテスト用ファイルをアップロード
- バケット一覧から作成したバケット名をクリックします。
- 「アップロード」をクリックします。
- 「ファイルを追加」をクリック、アップロードする arch-s3-mini-lab.txt を選択します。
- 「アップロード」をクリックします。アップロードの成功画面が出たら「閉じる」をクリックします。

## (3)同名のファイルで既存ファイルを上書き
- arch-s3-mini-lab.txt の中身をメモ帳などで自由に書き換え(半角英数字で)上書き保存します。
- 再度、arch-s3-mini-lab.txt を バケットにアップロードします。
- バージョニングが無効の場合、完全に上書きされます😨

## (4)古いバージョンのオブジェクトも保管されていることを確認
- オブジェクトの一覧画面でファイル名の左チェックボックスを選択し、「開く」をクリックします。
  - 最新のファイル内容が表示されることを確認します。
- オブジェクトの一覧画面で「バージョンの表示」トグルボタンをONにします。
- 古いバージョンのオブジェクトが存在していることを確認します。
- 古いバージョンのオブジェクトにチェックを入れ「開く」を押します。
-   古いバージョンのファイル内容が表示されることを確認します。
- これでバージョニングの動作が確認できました🎉🎉🎉

---
※権限の関係上実施しませんが、復旧させる場合には、以下の2通りの方法があります。
- [参考資料]( https://docs.aws.amazon.com/ja_jp/AmazonS3/latest/userguide/RestoringPreviousVersions.html )
- 復旧したい旧バージョンが最新になるまで、新バージョンを削除する。
- 復旧したい旧バージョンの内容を読みとり、新バージョンとして上書きする。