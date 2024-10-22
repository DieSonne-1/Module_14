import sqlite3

connection = sqlite3.connect('Users.db')
cursor = connection.cursor()


def initiate_db():
    # cursor.execute('''
    # CREATE TABLE IF NOT EXISTS Products(
    # id INTEGER PRIMARY KEY,
    # title TEXT NOT NULL,
    # description TEXT,
    # price INT NOT NULL
    # )
    # ''')
    #
    # cursor.execute('CREATE INDEX IF NOT EXISTS idx_email ON Products(id)')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INT NOT NULL,
    balance INT NOT NULL
    );
    ''')

    cursor.execute('CREATE INDEX IF NOT EXISTS idx_email ON Users(id)')


initiate_db()
#
# for i in range(1, 5):
#     cursor.execute('INSERT INTO Products (title, description, price) Values(?,?,?)',
#                    (f'Продукт {i}', f'Описание {i}', i * 100))
#     connection.commit()


def get_all_products():
    cursor.execute('SELECT * FROM Products')
    return cursor.fetchall()


def add_user(username, email, age):
    cursor.execute('INSERT INTO Users (username, email, age, balance) Values (?,?,?,1000)',
                   (username, email, age))
    connection.commit()


def is_included(username):
    cursor.execute('SELECT * FROM Users WHERE username=?', (username,))
    user = cursor.fetchone()

    return user is not None
