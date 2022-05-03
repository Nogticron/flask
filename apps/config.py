from pathlib import Path


basedir = Path(__file__).parent.parent


# BaseConfigクラスを作成する
class BaseConfig:
    SECRET_KEY = "neeyoNio8UGhidoo"
    WTF_CSRF_SECRET_KEY = "toomichohmiwai0J"


# BaseConfigクラスを継承してLocalConfigクラスを作成する
class LocalConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{basedir / 'local.sqlite'}",
    SQLALCHEMY_TRACK_MODIFICATIONS = False,
    SQLALCHEMY_ECHO = True,


# BaseConfigクラスを継承してTestingConfigクラスを作成する
class TestingConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{basedir / 'testing.sqlite'}",
    SQLALCHEMY_TRACK_MODIFICATIONS = False,
    WTF_CSRF_ENABLED = False


# Config辞書にマッピングする
config = {
    "testing": TestingConfig,
    "local": LocalConfig,
}
