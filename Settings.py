import os

MEDIA_DIR = '/home/ec2-user/apps/Cron/media/'
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
AWS_ACCESS_KEY_ID_DYN = 'AKIAINJKO4HDBSO2FB3A' #os.environ.get('AWS_ACCESS_KEY_ID_DYN')
AWS_SECRET_ACCESS_KEY_DYN = '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' #os.environ.get('AWS_SECRET_ACCESS_KEY_DYN')
REGION_NAME_DYN = 'us-east-2' #os.environ.get('REGION_NAME_DYN')
DATABASE_NAME_DYN = 'dynamodb' #os.environ.get('DATABASE_NAME_DYN')
AWS_STORAGE_BUCKET_NAME_S3 = 'supervoicescloud' #os.environ.get('AWS_STORAGE_BUCKET_NAME_S3')
AWS_ACCESS_KEY_ID_S3 = 'AKIAYIHZ36WNQ4XF7YUV' #os.environ.get('AWS_ACCESS_KEY_ID_S3')
AWS_SECRET_ACCESS_KEY_S3 = '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' # os.environ.get('AWS_SECRET_ACCESS_KEY_S3')
SLEEP_TIME = 2