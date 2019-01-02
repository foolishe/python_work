from distutils.log import warn as printf
import os
import random import randrange as rand

if isinstance(__builtins__,dict) and 'raw_input' in __builtins__:
    scanf = raw_input
elif hasattr(__builtins__,'raw_input'):
    scanf = raw_input
else:
    scanf = input

COLSIZ = 10
FIELDS = ('login','userid','project_id')
RDBMSs = {'s':'sqlite3','m':'mysql','p':'postgresql'}
DBNAME = 'test'
DB_EXC = None
NAMELEN = 16

tformat = lambda s:str(s).title().l just(COLSIZ)
cformat = lambda s:s.uppuer().ljust(COLSIZ)

def setup():
    return RDBMSs[scanf('''
        choose a database system:
        (M)ySQL
        (P)ostgreSQL
        (S)OLite3
        Enter choice:''').strip().lower()[0]]

def connect(db):
    global DB_EXC
    dbDir = '%s_%s' % (db,DBNAME)
    if db == 'sqlite3':
        try:
            import sqlite3
        except ImportError:
            try:
                from pysql2 import dbapi2 as sqlite3
            except ImportError:
                return None
        DB_EXC = sqlite3
        if not os.path.isdir(dbDir):
            os.mkdir(dbDir)
        cxn = sqlite3.connect(os.path.join(dbdir,DBNAME))

    elif db == 'mysql':
        try:
            import pymysql

            cxn = pymysql.connect(db=DBNAME)
        except DB_EXC.OperationalError:
            try:
                cxn = pymysql.connect(user=DBNAME)
                cxn.query('CREATE DATABASE %s' % DBNAME)
                cxn.commit()
                cxn.close()
                cxn = pymysql.connect(db=DBNAME)
            except DB_EXC.OperationalError:
                return None
        except ImportError:
            try:
                import mysql.connector
                import mysql.connector.errors as DB_EXC
                try:
                    cxn = mysql.connector.connect(**{'database':DBNAME,
                    'user':DBUSER,})
                except: DB_EXC.InterfaceError:
                    return None
    elif db == 'postgresql':
        try:
            import psycopg2
            cxn = psycopg2.connect(port=5433,dbname='postgres',
            user='postgres',password='')

def create(cur):
    try:
        cur.execute('''
            CREATE TABLE users(
            login VARCHAR(%d),
            userid INTRGER,
            project_id INTEGER,)
            ''' % NAMELEN
            ))
    except DB_EXC.OperationalError,e:
        drop(cur)
        create(cur)

drop = lambda cur: cur.execute('DROP TABLE users')

NAMES =(
    ('aaron',8760),('angela',7603),('dave',6435)
    ('juess',5356),('jjlj',5453),('fkjl',6546)
)

def randName():
    pick = set(NAMES)
    while pick:
        yield pick.pop()

def insert(cur,db):
    if db == 'sqlite':
        cur.executemany("INSERT INTO users VALUES(?,?,?)",
        [(who,uid,rand(1,5)) for who,uid in randName()])
    elif db == 'postgres':
        for who,uid in randName():
            cur.executemany('INSERT INTO users VALUES(?,?,?)',
            (who,uid,rand(1,5)))
    elif db =='mysql':
        cur.executemany("INSERT INTO users VALUES(%s,%s,%s)",
        [(who,uid,rand(1,5)) for who,uid in randName()])

getRC = lambda cur: cur.rowcount if hasattr(cur,'rowcount') else -1

def update(cur):
    fr = rand(1,5)
    to = rand(1,5)
    cur.execute('UPDATE users SET project_id=%d WHERE project_id=%d' % (to,fr))
    return fr,to,getRC(cur)

def delete(cur):
    rm = rand(1,5)
    cur.execute('DELETE FROM users WHERE project_id=%d' % rm)
    return rm,getRC(cur)

def dbDump(cur):
    cur.execute('SELECT*FROM users')
    print('\n%s' %''.join(map(cformat,FIELDS)))
    for data in cur.fetchall():
        printf(''.join(map(tformat,data)))

def main():
    db = setup()
    print('*** Connect to %r database' % db)
    cxn = connect(db)
    if not cxn:
        print('ERROR:%r not supported of unreachable,exit' % db)
        return
    cur = cxn.cursor()

    printf('\n*** Inserting names into table')
    insert(cur,db)
    dbDump(cur)
    printf('\n*** Randomly moving folks')
    fr,to,num = updata(cur)
    printf('\t(%d users moced) from (%d) to (%d)' %(num,fr,to))
    dbdump(cur)
    printf('\n*** Randomly chossing group')
    rm,num = delete(cur)
    printf('\t (group #%d; %d users removed)' % (rm,num))
    dbDump(cur)

    printf('\n*** Dropping users table')
    drop(cur)
    printf('\n*** Close cxns')
    cur.close()
    cxn.commit()
    cxn.close()
