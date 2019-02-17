from threading import Thread
from time import sleep
import Settings
import subprocess
from Email import Email
from DbConnection import DbConnection
from Voice import Voice


def ffmpeg(media_in, media_out, id_num, path_out, email, tittle, name):
    output = subprocess.call(['ffmpeg', '-i', media_in,
                     media_out, '-y'])
    if output < 0:
        print('error en conversion')
    else:
        try:
            database_connection = DbConnection()
            with database_connection:
                database_connection.update(Voice.create_update_converted_sql(id_num, path_out))
                Email.send_email(email=email, tittle=tittle, name=name)
        except:
            print('Error actualizando')


def convert():
    list_voices = []
    try:
        database_connection = DbConnection()
        with database_connection:
            query_voices = database_connection.query(Voice.UNCONVERTED_FILES)
            for voice in query_voices:
                list_voices.append(Voice(id_num=voice[0], voice_file=[1], email=voice[2],
                                         name=voice[3], tittle=voice[4]))
            if list_voices.__len__() != 0:
                database_connection.update(Voice.create_update_converting_sql(list_voices))
    except:
        print('error en la base de datos')

    for voice in list_voices:
        file_mp3 = voice.voice_file[:-3]

        if voice.voice_file[-3:] != 'mp3':
            try:
                media_in = Settings.MEDIA_DIR + voice.voice_file
                path_out = 'converted/' + file_mp3 + 'mp3'
                media_out = Settings.MEDIA_DIR + path_out
                my_thread = Thread(target=ffmpeg, args=[media_in, media_out, voice.id_num, path_out,
                                                        voice.email, voice.tittle, voice.name])

                my_thread.start()
                my_thread.join(60)

            except OSError as e:
                print('error de os')


if __name__ == '__main__':
    while True:
        Thread(target=convert).start()
        print('alive')
        sleep(3)



