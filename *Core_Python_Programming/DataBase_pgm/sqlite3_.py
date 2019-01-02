import sqlite3

cxn = sqlite3.connect('test.db')
cur = cxn.cursor()
cur.execute('CREATE TABLE users(login VARCHAR(8),userid INTEGER)')
cur.execute('INSERT INTO users VALUES("john",88)')
cur.execute('INSERT INTO users VALUES("jane",110)')
cur.execute('SELECT*FROM users')
for eachUser in cur.fetchall():
    print(eachUser)
cur.execute('DROP TABLE users')
cur.close()
cxn.commit()
cxn.close()
