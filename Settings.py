import os

MEDIA_DIR = '/home/ec2-user/apps/Cron/'
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
AWS_ACCESS_KEY_ID_DYN = os.environ.get('AWS_ACCESS_KEY_ID_DYN') #os.environ.get('AWS_ACCESS_KEY_ID_DYN')
AWS_SECRET_ACCESS_KEY_DYN = os.environ.get('AWS_SECRET_ACCESS_KEY_DYN') #os.environ.get('AWS_SECRET_ACCESS_KEY_DYN')
REGION_NAME_DYN = os.environ.get('REGION_NAME_DYN') #os.environ.get('REGION_NAME_DYN')
DATABASE_NAME_DYN = os.environ.get('DATABASE_NAME_DYN')
AWS_STORAGE_BUCKET_NAME_S3 = os.environ.get('AWS_STORAGE_BUCKET_NAME_S3')
AWS_ACCESS_KEY_ID_S3 = os.environ.get('AWS_ACCESS_KEY_ID_S3') #os.environ.get('AWS_ACCESS_KEY_ID_S3')
AWS_SECRET_ACCESS_KEY_S3 = os.environ.get('AWS_SECRET_ACCESS_KEY_S3') # os.environ.get('AWS_SECRET_ACCESS_KEY_S3')
AWS_QUEUE_URL = os.environ.get('AWS_QUEUE_URL') #'https://us-east-2.queue.amazonaws.com/942770429245/supervoices_sqs.fifo'
EMAIL_SEND = 'Y'
SLEEP_TIME = 5
