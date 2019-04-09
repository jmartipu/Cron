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
from Voice import Voice


def ffmpeg(media_in, media_out, id_num, path_out, email, tittle, name):
    print('ff1')
    output = subprocess.call(['/home/ec2-user/bin/ffmpeg', '-i', media_in,
                     media_out, '-y'])
    print('ff2')
    if output < 0:
        print('error en conversion Cron')
    else:
        try:
            database_connection = DbConnection()
            with database_connection:
                database_connection.update(Voice.create_update_converted_sql(id_num, path_out))
                Email.send_email(email=email, tittle=tittle, name=name)
        except:
            print('Error actualizando Cron')


def convert():
    list_voices = []
    voice_ids = []
    try:
        database_connection = DbConnection()
        s3_connection = S3Connection()

        with database_connection:
            query_voices = database_connection.scan('Voice', 'state', 'INP')
            
            for voice in query_voices:
                voice_file = voice['voice_file']
                voice_id = voice['voice_id']
                email = voice['email']
                name = voice['user_first_name']
                tittle = voice['tittle']
                list_voices.append(Voice(id_num=voice_id, voice_file=voice_file, email=email, name=name, tittle=tittle))
                with s3_connection:
                    s3_connection.read(voice_file, Settings.MEDIA_DIR + voice_file)
                    file_mp3 = voice_file[:-3]
                    if voice_file[-3:] != 'mp3':
                        try:
                            media_in = Settings.MEDIA_DIR + voice_file
                            dir_out = Settings.MEDIA_DIR + 'converted/'
                            path_out = 'converted/' + file_mp3 + 'mp3'
                            media_out = Settings.MEDIA_DIR + path_out
                            if not os.path.exists(dir_out):
                                os.makedirs(dir_out)

                            item = {
                                'user_last_name':
                                    voice['user_last_name'] if voice['user_last_name'] != '' else "Vacio",
                                'user_first_name':
                                    voice['user_first_name'] if voice['user_first_name'] != '' else "Vacio",
                                'contest':
                                    decimal.Decimal(voice['contest']) if voice['contest'] != '' else "Vacio",
                                'converted_date_end':
                                    voice['converted_date_end'] if voice['converted_date_end'] != '' else "Vacio",
                                'email':
                                    voice['email'] if voice['email'] != '' else "Vacio",
                                'creation_date':
                                    voice['creation_date'] if voice['creation_date'] != '' else "Vacio",
                                'state':
                                    'CVG',
                                'voice_converted_file':
                                    voice['voice_converted_file'] if voice['voice_converted_file'] != '' else "Vacio",
                                'winner':
                                    voice['winner'] if voice['winner'] != '' else "Vacio",
                                'notes':
                                    voice['notes'] if voice['notes'] != '' else "Vacio",
                                'voice_file':
                                    voice['voice_file'] if voice['voice_file'] != '' else "Vacio",
                                'tittle':
                                    voice['tittle'] if voice['tittle'] != '' else "Vacio",
                                'voice_id':
                                    voice['voice_id'] if voice['voice_id'] != '' else "Vacio",
                                'converted_date_start':
                                    datetime.datetime.utcnow().isoformat()
                            }

                            database_connection.update('Voice', item)
                            print('5')
                            ffmpeg(media_in, media_out, voice_id, path_out, email, tittle, name)
                            print('6')
                            s3_connection.upload(file_mp3 + 'mp3', media_out)
                            print('7')

                            item = {
                                'user_last_name':
                                    voice['user_last_name'] if voice['user_last_name'] != '' else "Vacio",
                                'user_first_name':
                                    voice['user_first_name'] if voice['user_first_name'] != '' else "Vacio",
                                'contest':
                                    decimal.Decimal(voice['contest']) if voice['contest'] != '' else "Vacio",
                                'converted_date_end':
                                    datetime.datetime.utcnow().isoformat(),
                                'email':
                                    voice['email'] if voice['email'] != '' else "Vacio",
                                'creation_date':
                                    voice['creation_date'] if voice['creation_date'] != '' else "Vacio",
                                'state':
                                    voice['state'] if voice['state'] != '' else "Vacio",
                                'voice_converted_file':
                                    file_mp3 + 'mp3',
                                'winner':
                                    voice['winner'] if voice['winner'] != '' else "Vacio",
                                'notes':
                                    voice['notes'] if voice['notes'] != '' else "Vacio",
                                'voice_file':
                                    voice['voice_file'] if voice['voice_file'] != '' else "Vacio",
                                'tittle':
                                    voice['tittle'] if voice['tittle'] != '' else "Vacio",
                                'voice_id':
                                    voice['voice_id'] if voice['voice_id'] != '' else "Vacio",
                                'converted_date_start':
                                    voice['converted_date_start'] if voice['converted_date_start'] != '' else "Vacio",
                            }
                            print('8')
                            database_connection.update('Voice', item)
                            print('9')
                        except OSError as e:
                            print("Error en sistema operativo Cron")

    except Exception as e:
        print(e)


if __name__ == '__main__':
    # while True:
        # Thread(target=convert).start()
        convert()
        # st = str(datetime.datetime.now())
        # print(st + ' : alive')
        # sleep(Settings.SLEEP_TIME)



