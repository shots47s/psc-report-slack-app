import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
  SECRET_KEY = os.environ.get('SECRET_KEY')
  CSRF_ENABLED = True
  DEBUG = False
  TESTING = False

  SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or 'sqlite:///' + os.path.join(basedir, 'app.db')
  SQLALCHEMY_TRACK_MODIFICATIONS = False

  MAIL_SERVER = os.environ.get('MAIL_SERVER')
  MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
  MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
  MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
  MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
  MAIL_DEFAULT_SENDER = '"Shawn Brown" <shawntbrown@gmail.com>'
  ADMINS = ['shawntbrown@gmail.com']
  LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')

  SLACK_TOKEN = os.environ.get('SLACK_TOKEN')
  SLACK_CHAT_TOKEN = os.environ.get('SLACK_CHAT_TOKEN')
  SLACK_CALLBACK = '/slack_callback'


class ProductionConfig(Config):
  DEBUG = False


class StagingConfig(Config):
  DEVELOPMENT = True
  DEBUG = True


class DevelopmentConfig(Config):
  DEVELOPMENT = True
  DEBUG = True


class TestingConfig(Config):
  TESTING = True
