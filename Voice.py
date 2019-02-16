class Voice:

    UNCONVERTED_FILES = "SELECT id, voice_file FROM contests_voice WHERE state = 'INP'"

    def __init__(self, id_num, voice_file):
        self.id_num = id_num
        self.voice_file = voice_file
        self.voice_file_converted = ""

    def __str__(self):
        return str(self.id_num)

    @staticmethod
    def create_update_sql(list_voices):
        sql = None
        if list_voices is not None:
            sql = "UPDATE contests_voice SET state = 'CVG' WHERE id in("
            for voice in list_voices:
                sql = sql + str(voice.id_num) + ","
            sql = sql[:-1]
            sql = sql + ")"
        return sql

