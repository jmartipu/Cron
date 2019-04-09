import boto3
import botocore
import Settings


class SQSConnection:
    def __init__(self):
        self.exists = True

    def __enter__(self):
        try:
            self.session = boto3.Session(
                aws_access_key_id=Settings.AWS_ACCESS_KEY_ID_DYN,
                aws_secret_access_key=Settings.AWS_SECRET_ACCESS_KEY_DYN,
            )
            self.sqs = self.session.resource('sqs')
            self.queue_url = 'SQS_QUEUE_URL'

        except ConnectionError:
            print("No se puede conectar a SQS")

        except:
            print("Error General SQS")

    def receive(self, key, download_key):
        try:
            
            response = sqs.receive_message(
              QueueUrl=self.queue_url,
              AttributeNames=[
                  'SentTimestamp'
              ],
              MaxNumberOfMessages=1,
              MessageAttributeNames=[
                  'All'
              ],
              VisibilityTimeout=0,
              WaitTimeSeconds=0
            )
            message = response['Messages'][0]
            receipt_handle = message['ReceiptHandle']

        except botocore.exceptions.ClientError as e:
            # If a client error is thrown, then check that it was a 404 error.
            # If it was a 404 error, then the bucket does not exist.
            error_code = e.response['Error']['Code']
            if error_code == '404':
                self.exists = False

        except Exception as e:
            print('Error Leyendo')

    def delete(self, receipt_handle):
        try:
            sqs.delete_message(
              QueueUrl=self.queue_url,
              ReceiptHandle=receipt_handle
            )

        except botocore.exceptions.ClientError as e:
            # If a client error is thrown, then check that it was a 404 error.
            # If it was a 404 error, then the bucket does not exist.
            error_code = e.response['Error']['Code']
            if error_code == '404':
                self.exists = False

        except Exception as e:
            print('Error Cargando S3')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("S3 Terminada exit")




