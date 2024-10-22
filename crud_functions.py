import sqlite3

connection = sqlite3.connect('products_.db')
cursor = connection.cursor()


def initiate_db():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INT NOT NULL
    )
    ''')

    cursor.execute('CREATE INDEX IF NOT EXISTS idx_email ON Products(id)')


initiate_db()

for i in range(1, 5):
    cursor.execute('INSERT INTO Products (title, description, price) Values(?,?,?)',
                   (f'Продукт {i}', f'Описание {i}', i * 100))
connection.commit()

def get_all_products():
    cursor.execute('SELECT * FROM Products')
    return cursor.fetchall()