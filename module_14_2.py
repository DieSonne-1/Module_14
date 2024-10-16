import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

# for i in range(1, 11):
#     cursor.execute('INSERT INTO Users(username, email, age, balance) Values(?,?,?,?)',
#                    (f'User{i}', f'example{i}@gmail.com', f'{i}0', '1000'))
# for i in range(1, 11, 2):
#     cursor.execute('UPDATE Users SET balance = 500 WHERE id = ?', (i,))
#
# for i in range(1, 11, 3):
#     cursor.execute('DELETE FROM Users WHERE id = ?', (i,))
#
# cursor.execute('SELECT username, email, age, balance FROM Users WHERE age != ?', (60,))
# us = cursor.fetchall()
# for user in us:
#     print(f'Имя:{user[0]}| Почта:{user[1]}| Возраст:{user[2]}| Баланс:{user[3]}')


cursor.execute('DELETE FROM Users WHERE id = ?', (6,))

cursor.execute('SELECT COUNT(*) FROM Users')
total_users = cursor.fetchone()[0]

cursor.execute('SELECT SUM(balance) FROM Users')
all_balances = cursor.fetchone()[0]
print(all_balances / total_users)

connection.commit()
connection.close()
