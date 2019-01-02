import psycopg2

cxn = psycopg2.connect(port=5433,dbname='postgres',user='postgres',password='')

cur = cxn.cursor()
cur.execute('SELECT*FROM pg_database')
rows = cur.fetchall()
for i in rows:
    print(i)

cur.close()
cxn.commit()
cxn.close()
