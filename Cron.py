import Settings
import subprocess
from DbConnection import DbConnection
from Voice import Voice


if __name__ == '__main__':

    list_voices = []
    try:
        database_connection = DbConnection()
        with database_connection:
            query_voices = database_connection.query(Voice.UNCONVERTED_FILES)
            for voice in query_voices:
                list_voices.append(Voice(voice[0], voice[1]))
            if list_voices.__len__() != 0:
                database_connection.update(Voice.create_update_sql(list_voices))
    except:
        print('error en la base de datos')
        
    for voice in list_voices:
        file = voice.voice_file.rsplit('/', 1)[-1]
        file_mp3 = file[:-3]

        if file[-3:] != 'mp3':
            try:
                output = subprocess.call(['ffmpeg', '-i', Settings.MEDIA_DIR + file,
                                          Settings.MEDIA_COMPLETED_DIR + file_mp3 + 'mp3', '-y'])
                if output < 0:
                    print('error')
                else:
                    print('ok')
            except OSError as e:
                print('error de os')


