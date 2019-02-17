import threading
from queue import Queue
import Settings
import subprocess
from DbConnection import DbConnection
from Voice import Voice

NUMBER_OF_THREADS = 5
JOB_NUMBER = [1]
queue = Queue()


def create_workers():
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()


def work():
    while True:
        x = queue.get()
        if x == 1:
            convert()
        queue.task_done()


def create_jobs():
    for x in JOB_NUMBER:
        queue.put(x)
    queue.join()


def convert():
    list_voices = []
    try:
        database_connection = DbConnection()
        with database_connection:
            query_voices = database_connection.query(Voice.UNCONVERTED_FILES)
            for voice in query_voices:
                list_voices.append(Voice(voice[0], voice[1]))
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

                output = subprocess.call(['ffmpeg', '-i', media_in,
                                          media_out, '-y'])
                if output < 0:
                    print('error en conversion')
                else:
                    try:
                        database_connection = DbConnection()
                        with database_connection:
                            database_connection.update(Voice.create_update_converted_sql(voice.id_num, path_out))
                    except:
                        print('Error actualizando')
            except OSError as e:
                print('error de os')


if __name__ == '__main__':
    create_workers()
    create_jobs()


