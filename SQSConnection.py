import boto3
import botocore
import Settings


class SQSConnection:
    session = boto3.Session(
                aws_access_key_id=Settings.AWS_ACCESS_KEY_ID_DYN,
                aws_secret_access_key=Settings.AWS_SECRET_ACCESS_KEY_DYN,
            )
    sqs = session.client('sqs', region_name='us-east-2')
    queue_url = Settings.AWS_QUEUE_URL
    exists = True
    message = ''
    receipt_handle = ''

    def __enter__(self):
        try:
            self.session = boto3.Session(
                aws_access_key_id=Settings.AWS_ACCESS_KEY_ID_DYN,
                aws_secret_access_key=Settings.AWS_SECRET_ACCESS_KEY_DYN,
            )
            self.sqs = self.session.client('sqs', region_name='us-east-2')
            self.queue_url = Settings.AWS_QUEUE_URL

        except ConnectionError:
            print("No se puede conectar a SQS")

        except Exception as e:
            print(e)

    def receive(self):
        try:
            response = self.sqs.receive_message(
              QueueUrl=self.queue_url,
              AttributeNames=[
                  'ALL'
              ],
              MaxNumberOfMessages=1,
              MessageAttributeNames=[
                  'All'
              ],
              VisibilityTimeout=20,
              WaitTimeSeconds=2
            )
            if response is not None:
              self.message = response['Messages'][0]
              self.receipt_handle = self.message['ReceiptHandle']
             
            
        except botocore.exceptions.ClientError as e:
            # If a client error is thrown, then check that it was a 404 error.
            # If it was a 404 error, then the bucket does not exist.
            error_code = e.response['Error']['Code']
            if error_code == '404':
                self.exists = False

        except Exception as e:
            print(e)
        

    def delete(self):
        try:
            print(self.receipt_handle)
            self.sqs.delete_message(
              QueueUrl=self.queue_url,  
              ReceiptHandle=self.receipt_handle
            )
            self.message = ''
            self.receipt_handle = ''

        except botocore.exceptions.ClientError as e:
            # If a client error is thrown, then check that it was a 404 error.
            # If it was a 404 error, then the bucket does not exist.
            error_code = e.response['Error']['Code']
            if error_code == '404':
                self.exists = False

        except Exception as e:
            print('Error Cargando SQS')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("SQS Terminada exit")




