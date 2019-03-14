import os

MEDIA_DIR = './media/'
HOST = os.environ.get('DATABASE_HOST')
PORT = os.environ.get('DATABASE_PORT')
DATABASE = os.environ.get('DATABASE_NAME')
USER = os.environ.get('PGUSER')
PASSWORD = os.environ.get('PGPASSWORD')
EMAIL_ADDRESS = os.environ.get('EMAIL_ADDRESS')
EMAIL_USERNAME = os.environ.get('EMAIL_USERNAME')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')
EMAIL_SMTP_HOST = os.environ.get('EMAIL_SMTP_HOST')
EMAIL_SMTP_PORT = os.environ.get('EMAIL_SMTP_PORT')
SLEEP_TIME = 2