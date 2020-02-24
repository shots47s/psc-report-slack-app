import os

from flask import Flask
from config import *

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from slackeventsapi import SlackEventAdapter


app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Function to initialize the email and logs
from app import routes, models  # noqa


def init_email_and_logs_error_handler(app):
  if app.debug and not app.testing:
    return

  import logging
  from logging.handlers import SMTPHandler

  if app.config['MAIL_SERVER']:
    auth = None

    if app.config['MAIL_USERNAME'] or app.config['MAIL_PASSWORD']:
      auth = (app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])

      secure = None
      if app.config['MAIL_USE_TLS']:
        secure = 90

      mail_handler = SMTPHandler(mailhost=(app.config['MAIL_SERVER'], app.config['MAIL_PORT']),
                                 fromaddr='no-reply@' + app.config['MAIL_SERVER'],
                                 toaddrs=app.config['ADMINS'], subject='Microblog Failure',
                                 credentials=auth, secure=secure)
      mail_handler.setLevel(logging.ERROR)
      app.logger.addHandler(mail_handler)

      if app.config['LOG_TO_STDOUT']:
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.INFO)
        app.logger.addHandler(stream_handler)
      else:
        if not os.path.exists('logs'):
          os.mkdir('logs')
        file_handler = RotatingFileHandler('logs/microblog.log',
                                           maxBytes=10240, backupCount=10)
        file_handler.setFormatter(logging.Formatter(
            '%(asctime)s %(levelname)s: %(message)s '
            '[in %(pathname)s:%(lineno)d]'))
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)

      app.logger.setLevel(logging.INFO)
      app.logger.info('PSC Reporting startup')
