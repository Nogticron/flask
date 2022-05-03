# flask

## ローカル環境構築
- `pip`, `pyenv`が使えている前提

```sh
# 必須
$ pip install \
flask \
email-validator \
flask-debugtoolbar \
flask-mail \
flask-sqlalchemy \
flask-migrate

# オプション
$ pip install python-dotenv
```

- コードチェッカー・フォーマッターなど
  - インストール後、各エディタで有効化する
```sh
pip install flake8 black isort mypy
```

- メール機能を使う場合はGmailなどでアプリ用パスワードの取得などを済ませる
  - https://myaccount.google.com/signinoptions/two-step-verification/enroll-welcome
  - https://security.google.com/settings/security/apppasswords
  - .envのユーザー情報を埋める
