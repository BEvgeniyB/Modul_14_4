import sqlite3
from itertools import product

#from pythonProject.Modul_14.modul_14_1 import connect

connection = sqlite3.connect("database_14_4.db")
cursor = connection.cursor()
def initiate_db():

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT ,
    photo_path TEXT,
    price INTEGER NOT NULL
    )
    ''')
    connection.commit()

def add_products(title,price,description='',photo_path=''):
    if len(title) > 0 and isinstance(price, int):
        cursor.execute("INSERT INTO Products (title,description,price,photo_path) VALUES (?,?,?,?)", (title,description, price,photo_path))
        connection.commit()
    else:
        raise ValueError('Не правильные данные,запись невозможна')

def get_all_products():
    cursor.execute("SELECT * FROM Products")
    return cursor.fetchall()

initiate_db()
cursor.execute('SELECT * FROM Products')
if cursor.fetchone() == None:
    add_products("Omega 3",100,'описание 1','files/1.jpg')
    add_products("Vitamin C", 200, 'описание 2', 'files/2.jpg')
    add_products("Vitamin B6", 300, 'описание 3', 'files/3.jpg')
    add_products("Zinc citrate", 400, 'описание 4', 'files/4.jpg')
    add_products("Omega 3 + Vitamin C", 280, 'комплект 4', 'files/11.jpg')
    connection.commit()