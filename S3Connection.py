import boto3
import botocore
import Settings


class S3Connection:
    def __init__(self):
        self.exists = True

    def __enter__(self):
        try:
            self.session = boto3.Session(
                aws_access_key_id=Settings.AWS_ACCESS_KEY_ID_S3,
                aws_secret_access_key=Settings.AWS_SECRET_ACCESS_KEY_S3,
            )
            self.s3 = self.session.resource('s3')
            self.bucket = self.s3.Bucket(Settings.AWS_STORAGE_BUCKET_NAME_S3)
            self.exists = True
        except ConnectionError:
            print("No se puede conectar a la base de datos")

        except:
            print("Error General")

    def read(self, key, download_key):
        try:
            self.bucket.download_file(key, download_key)

        except botocore.exceptions.ClientError as e:
            # If a client error is thrown, then check that it was a 404 error.
            # If it was a 404 error, then the bucket does not exist.
            error_code = e.response['Error']['Code']
            if error_code == '404':
                self.exists = False

        except Exception as e:
            print('Error Leyendo')

    def upload(self, key, upload_key):
        try:
            self.bucket.upload_file(upload_key, key)

        except botocore.exceptions.ClientError as e:
            # If a client error is thrown, then check that it was a 404 error.
            # If it was a 404 error, then the bucket does not exist.
            error_code = e.response['Error']['Code']
            if error_code == '404':
                self.exists = False

        except Exception as e:
            print('Error Cargando')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("S3 Terminada exit")




