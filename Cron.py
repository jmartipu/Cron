import decimal
import os
from time import sleep
import datetime
import Settings
import json
import subprocess
from Email import Email
from DbConnection import DbConnection
from S3Connection import S3Connection
from SQSConnection import SQSConnection
from Voice import Voice
from threading import Thread


def ffmpeg(media_in, media_out):
    output = subprocess.call(['/home/ec2-user/bin/ffmpeg', '-i', media_in,
                     media_out, '-y'])
    if output < 0:
        print('error en conversion Cron')

def convert():
    list_voices = []
    voice_ids = []
    try:
        database_connection = DbConnection()
        s3_connection = S3Connection()
        sqs_connection = SQSConnection()

        with sqs_connection:
            sqs_connection.receive()
            if sqs_connection.message is not '':
              message_attributes = sqs_connection.message.get('MessageAttributes')
              voice_key = message_attributes.get('voice_key').get('StringValue')
              voice_ext = message_attributes.get('voice_ext').get('StringValue')
              voice_file = message_attributes.get('voice_file').get('StringValue')
              voice_id = message_attributes.get('voice_id').get('StringValue')
              voice_id_dec = decimal.Decimal(voice_id)              
              tittle = message_attributes.get('tittle').get('StringValue')
              email = message_attributes.get('email').get('StringValue')
              user_first_name = message_attributes.get('user_first_name').get('StringValue')
              user_last_name = message_attributes.get('user_last_name').get('StringValue')
              contest = message_attributes.get('contest').get('StringValue')
              contest_dec = decimal.Decimal(contest)
              converted_date_end = ''
              creation_date = message_attributes.get('creation_date').get('StringValue')
              voice_converted_file = ''
              winner = 'False'
              notes = ''
              converted_date_start = datetime.datetime.utcnow().isoformat()
              
              with s3_connection:
                print(message_attributes)
                
                media_in = Settings.MEDIA_DIR + 'media/' +  voice_file
                dir_out = Settings.MEDIA_DIR + 'media/converted/'
                s3_connection.read('media/' + voice_file, media_in)
                file_mp3 = voice_key
                
                if voice_ext != '.mp3':
                    try:          
                        path_out = 'media/converted/' + file_mp3 + '.mp3'
                        db_path_out = 'converted/' + file_mp3 + '.mp3'
                        media_out = Settings.MEDIA_DIR + path_out
                        if not os.path.exists(dir_out):
                            os.makedirs(dir_out)

                        #1
                                                
                        database_connection.update('Voice', {'voice_key': voice_key},'SET #st = :sta, converted_date_start = :cds', {'#st': 'state'}, {':sta': 'CVG', ':cds':converted_date_start})
                        
                        ffmpeg(media_in, media_out)
                        converted_date_end = datetime.datetime.utcnow().isoformat()
                        s3_connection.upload(path_out , media_out)
                        
                        database_connection.update('Voice', {'voice_key': voice_key},'SET #st = :sta, converted_date_end = :cde, voice_converted_file = :vcf', {'#st': 'state'}, {':sta': 'CVD', ':cde':converted_date_end, ':vcf':db_path_out})
                        
                        os.remove(media_out)
                    except OSError as e:
                        print(e)
                if Settings.EMAIL_SEND == 'Y':
                    Email.send_email(email=email, tittle=tittle, name=user_first_name)

                os.remove(media_in)
              sqs_connection.delete()
                
    except Exception as e:
        print(e)


if __name__ == '__main__':
    while True:
        Thread(target=convert).start()
        #convert()
        st = str(datetime.datetime.now())
        print(st + ' : alive')
        sleep(Settings.SLEEP_TIME)
