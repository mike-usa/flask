import os

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from tokenize import String


def set_host():
  global db_host
  db_host = os.environ.get('SQL_HOST') if 'SQL_HOST' in os.environ else 'localhost'


def set_user():
  global db_user
  db_user = os.environ.get('SQL_USER') if 'SQL_USER' in os.environ else 'dev_acct'


def set_pw():
  global db_pw
  db_pw = os.environ.get('SQL_PW') if 'SQL_PW' in os.environ else ''


def set_schema():
  global db_schema
  db_schema = os.environ.get('SQL_SCHEMA') if 'SQL_SCHEMA' in os.environ else 'public'


set_host()
set_user()
set_pw()
set_schema()

class Config(object):
  SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://{user}:{pw}@{host}/app_db".format(user=db_user, pw=db_pw, host=db_host)

class TestConfig(Config):
  def __init__(self):
    pass

engine = create_engine(
  Config.SQLALCHEMY_DATABASE_URI,
  connect_args = {
    'options': "-csearch_path={}".format(db_schema)
  },
  echo = True
)

db = SQLAlchemy()  # <-- how to assign engine?