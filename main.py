from database import Database
from sys import argv
from os import getenv
from dotenv import load_dotenv
load_dotenv()


if len(argv) == 2 and argv[1] == 'setup':
    '''
        Initialize DAtabase
        Usage: python main.py setup
    '''
    print('Creating table in datebase...')
    db = Database(getenv('DB_NAME'))
    db.create_table('''CREATE TABLE urls (
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    category TEXT,
                                    url TEXT
                                );''')
    
if len(argv) == 4 and argv[1] == 'add':
    '''
        Adding new resource
        python main.py add http://[website.com]
    '''
    print('Adding new URL adres...')
    category = argv[2]
    url = argv[3]
    db = Database(getenv('DB_NAME'))
    db.insert('urls', None, category, url)

if len(argv) == 3 and argv[1] == 'list':
    category = argv[2]
    print(f'Link list from category {category}:')
    db = Database(getenv('DB_NAME'))
    links = db.fetch_all('urls', category=category)

    for link in links:
        print(link[2])
