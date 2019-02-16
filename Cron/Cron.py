import subprocess
from Cron.DbConnection import DbConnection
from Cron.Voice import Voice


if __name__ == '__main__':
    list_voices = []
    database_connection = DbConnection()
    with database_connection:
        query_voices = database_connection.query(Voice.UNCONVERTED_FILES)
        for voice in query_voices:
            list_voices.append(Voice(voice[0], voice[1]))
        if list_voices.__len__() != 0:
            database_connection.update(Voice.create_update_sql(list_voices))

    for voice in list_voices:
        if voice.voice_file[-3:] != 'mp3':
            subprocess.call(['ffmpeg', '-i', voice.voice_file, voice.voice_file[:-3] + "mp3"])

