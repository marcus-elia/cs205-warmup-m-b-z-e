# cited sources: https://likegeeks.com/python-sqlite3-tutorial/
# cited sources: https://www.pythonforbeginners.com/dictionary/python-split
import sqlite3
from sqlite3 import Error
def sql_connect():
    try:
        con = sqlite3.connect('test7.db')
        return con
    except Error:
        print(Error)

def sql_table(con):
    cursorObj = con.cursor()
    cursorObj.execute("CREATE TABLE professor(professorN varchar(15) PRIMARY KEY, office varchar(15), title varchar(20))")
    cursorObj.execute("CREATE TABLE course(name varchar(30), crn INTEGER, registered INTEGER, location varchar(15), cprofessor varchar(15), FOREIGN KEY(cprofessor) REFERENCES professor(professorN))")
    con.commit()

def insert_row(con, entities):
    cursorObj = con.cursor()
    cursorObj.execute('''INSERT INTO professor(professorN, office, title) VALUES(?,?,?)''', entities)
    con.commit()

def insert_row1(con, entities):
    cursorObj = con.cursor()
    cursorObj.execute('''INSERT INTO course(name, crn, registered, location, cprofessor) VALUES(?,?,?,?,?)''', entities)
    con.commit()

def read_file(con):
    f = open("professors.csv")
    for line in f:
        a,b,c = line.split(",")
        c = c.rstrip()
        entities = (a, b, c)
        insert_row(con, entities)
    f.close()
    f1 = open("courses.csv")
    for l in f1:
        a,b,c,d,e = l.split(",")
        e = e.rstrip()
        entities1 = (a, b, c, d, e)
        insert_row1(con, entities1)

def sql_fetch(con):
    cursorObj = con.cursor()
    cursorObj.execute('SELECT * FROM course')
    rows = cursorObj.fetchall()
    for row in rows:
        print(row)

con = sql_connect()
sql_table(con)
read_file(con)
#sql_fetch(con)
