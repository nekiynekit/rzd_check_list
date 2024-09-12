import os


basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URL = 'sqlite:///' + os.path.join('app.db')


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'any_key'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///check_list.db'