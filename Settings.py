import os

MEDIA_DIR = '../contests/Grupo02/supervoices/contests/media/'
MEDIA_COMPLETED_DIR = '../contests/Grupo02/supervoices/contests/media/completed'
HOST = os.environ.get('DATABASE_HOST')
PORT = os.environ.get('DATABASE_PORT')
DATABASE = os.environ.get('DATABASE_NAME')
USER = os.environ.get('PGUSER')
PASSWORD = os.environ.get('PGPASSWORD')
