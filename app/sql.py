import psycopg2

class Db():
    def __init__(self) -> None:
        self.connection = psycopg2.connect(dbname='app', user='app', 
                                            password='1234', host='db')
        self.cursor = self.connection.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS List (
            id SERIAL PRIMARY KEY,
            model varchar(50) NOT NULL,
            num varchar(50) NOT NULL,
            description varchar(500) NOT NULL
            )'''
                       )
        self.connection.commit()

    def get(self, order="id"):
        self.cursor.execute('SELECT id, model, num, description FROM List ORDER BY '+order)
        results = self.cursor.fetchall()
        return results
    
    def write(self, data):
        sql = """INSERT INTO List (model, num, description) VALUES (%s, %s, %s)"""
        self.cursor.execute(sql,data)
        self.connection.commit()

    def __del__(self):
        self.connection.close()
    