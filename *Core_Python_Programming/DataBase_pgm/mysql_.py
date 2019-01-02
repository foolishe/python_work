import pymysql

cxn = pymysql.connect('localhost',user='root',passwd='',db='mysql',port=3306)

cur = cxn.cursor()
cur.execute('DROP TABLE users')
cur.execute('CREATE TABLE users(login VARCHAR(8),userid INT)')
cur.execute('INSERT INTO users VALUES("john",7000)')
cur.execute("INSERT INTO users VALUES('jane',7001)")
cur.execute('INSERT INTO users VALUES("bob",7200)')
cur.execute("SELECT*FROM users WHERE login LIKE'j%'")
for data in cur.fetchall():
    print('%s\t%s' % data)
cur.execute("UPDATE users SET userid=7100 WHERE userid=7000")
cur.execute('SELECT*FROM users')
for data in cur.fetchall():
    print('%s\t%s' % data)
