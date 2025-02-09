import sqlite3
from sys import argv
from os import getenv
from dotenv import load_dotenv
load_dotenv()


class Database:
    def __init__(self, database_name):
        self.connection = sqlite3.connect(database_name)
        self.cursor = self.connection.cursor()

    def __del__(self):
        self.connection.close()

    def create_table(self, sql: str):
        self.cursor.execute(sql)
        self.connection.commit()


if len(argv) == 2 and argv[1] == 'setup':
    print('Creating table in datebase...')
    db = Database(getenv('DB_NAME'))
    db.create_table('''CREATE TABLE urls (
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    category TEXT,
                                    url TEXT
                                );''')
    
if len(argv) == 4 and argv[1] == 'add':
    print('Adding new URL adres...')
    db = Database(getenv('DB_NAME'))
