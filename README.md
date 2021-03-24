# mailaddress_scraper

メールアドレスを含むWebサイトから、メールアドレスを取得するプログラム

## ライブラリのインストール
`requests`モジュールを利用するので、インストールが必要です。  
以下のコマンドを実行しましょう。

```
pip install -r requirements.txt
```

## プログラムの実行の仕方
`python scraper.py [メールアドレスを取得したいWebサイトのURL]` というコマンドを実行しましょう。

### 実行例
``` 
$ python scraper.py https://yts-inc.net/
support@yts-inc.net
```
