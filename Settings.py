import os

MEDIA_DIR = '../contests/Grupo02/supervoices/contests/media/'
HOST = os.environ.get('DATABASE_HOST')
PORT = os.environ.get('DATABASE_PORT')
DATABASE = os.environ.get('DATABASE_NAME')
USER = os.environ.get('PGUSER')
PASSWORD = os.environ.get('PGPASSWORD')
EMAIL_ADDRESS = os.environ.get('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')
SLEEP_TIME = 5