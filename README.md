# emo_body_temp
   emo&konashiの作例emo体温管理用リポジトリ

##環境構築
### konashi5のpython sdkインストール
[konashi5 python sdk](https://github.com/YUKAI/konashi5-sdk-python/tree/develop)
### emo python sdkインストール
```bash
# Python 3.7+ required
pip3 install emo-platform-api-sdk
```
### emoアクセストークンの設定
[このページ](https://platform-api.bocco.me/dashboard/login)にアクセスしてアクセストークンとリフレッシュトークンを
取得し，以下のように設定する.
```bash
export EMO_PLATFORM_API_ACCESS_TOKEN="your access token"
export EMO_PLATFORM_API_REFRESH_TOKEN="your refresh token"
```
