import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    if os.environ.get('DB_HOST'):
        SQLALCHEMY_DATABASE_URI = f'postgresql+psycopg2://{os.environ.get("DB_USER")}:{os.environ.get("DB_PASSWORD")}' \
                                  f'@{os.environ.get("DB_HOST")}:{os.environ.get("DB_PORT")}/' \
                                  f'{os.environ.get("DB_NAME")}'
    else:
        SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['admin@blog.com']

    POSTS_PER_PAGE = 25

    if os.environ.get('SEARCH_HOST'):
        ELASTICSEARCH_URL = f'http://{os.environ.get("SEARCH_HOST")}:{os.environ.get("SEARCH_PORT")}'
    else:
        ELASTICSEARCH_URL = None
