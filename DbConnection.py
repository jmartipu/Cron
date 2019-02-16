import psycopg2


class DbConnection:
    def __enter__(self):
        try:
            self.connection = psycopg2.connect(
                host="localhost",
                port="5000",
                database="contests",
                user="contests",
                password="Admin.01"
            )
            self.connection.autocommit = True
            self.cursor = self.connection.cursor()
            # print("Conectado")

        except ConnectionError:
            print("No se puede conectar a la base de datos")

        except:
            print("Error General")

    def query(self, query):
        results = []
        try:
            self.cursor.execute(query)
            results = self.cursor.fetchall()
        except:
            print("Error en consulta")

        return results

    def update(self, query):
        try:
            self.cursor.execute(query)
        except:
            print("Error en actualización")

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()
        # print("Conexion Terminada exit")







