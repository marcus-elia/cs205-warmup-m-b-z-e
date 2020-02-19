# cited sources: https://likegeeks.com/python-sqlite3-tutorial/
# cited sources: https://www.pythonforbeginners.com/dictionary/python-split
# cited sources: https://www.sqlitetutorial.net/sqlite-drop-table/
import sqlite3
from sqlite3 import Error
import sys
import os
import subprocess

def sql_connect():
    try:
        con = sqlite3.connect('test7.db')
        return con
    except Error:
        print(Error)

def sql_table(con):
    cursorObj = con.cursor()
    cursorObj.execute("CREATE TABLE IF NOT EXISTS professor(professorN varchar(15) PRIMARY KEY, office varchar(15), title varchar(20))")
    cursorObj.execute("CREATE TABLE IF NOT EXISTS course(name varchar(30), crn INTEGER, registered INTEGER, location varchar(15), cprofessor varchar(15), FOREIGN KEY(cprofessor) REFERENCES professor(professorN))")
    con.commit()

def insert_row(con, entities):
    cursorObj = con.cursor()
    cursorObj.execute('''INSERT OR REPLACE INTO professor(professorN, office, title) VALUES(?,?,?)''', entities)
    con.commit()

def insert_row1(con, entities):
    cursorObj = con.cursor()
    cursorObj.execute('''INSERT OR REPLACE INTO course(name, crn, registered, location, cprofessor) VALUES(?,?,?,?,?)''', entities)
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

def greeting():
    print("Welcome to the UVM CS professor and course search engine for Spring 2020!")
    print("Please use the following format for search commands:")
    print("\t 1. office, professor, professor's name. Example: office, professor, Eddy")
    print("\t 2. office, title, title's name.         Example: office, title, Lecturer")
    print("\t 3. course, professor, professor's name. Example: course, professor, Erickson")
    print("\t 4. title, professor, professor's name.  Example: title, professor, Horton")
    print("\t 5. room, course, course's name.         Example: room, course, Intro to Web Site Dev")
    print("\t 6. room, CRN, CRN number.               Example: room, CRN, 10747")
    print("\t 7. enrollment, course, course's name.   Example: enrollment, course, Intro to Web Site Dev")
    print("\t 8. enrollment, CRN, CRN number.         Example: enrollment, CRN, 10747")
    try:
        executeSQL()
    except ValueError:
        print("Please follow the format from 1 of 8 command types, and please use commas between the entries.")
        con = sql_connect()
        cursorObj = con.cursor()
        cursorObj.execute('''PRAGMA foreign_keys = OFF;''')
        cursorObj.execute('''DROP TABLE professor;''')
        cursorObj.execute('''UPDATE course SET cprofessor = NULL;''')
        cursorObj.execute('''DROP TABLE course;''')
        cursorObj.execute('''PRAGMA foreign_keys = ON;''')
        subprocess.call("del test7.db", shell=True)

def executeSQL():
    con = sql_connect()
    sql_table(con)
    read_file(con)
    inputTable()
    run = input("Would you like to try out our engine? Enter y or n: ")
    while run == 'y' or run == 'Y':
        user_input = input("Enter your command here: ")
        a,b,c = user_input.split(',')
        a = a.strip()
        b = b.strip()
        c = c.strip()
        results = commandSQL(a, b, c)
        while results == 1:
            user_input = input("That command is invalid, please try another command or type n to quit: ")
            if user_input == 'n' or user_input == 'N':
                print("Goodbye!")
                cursorObj = con.cursor()
                cursorObj.execute('''PRAGMA foreign_keys = OFF;''')
                cursorObj.execute('''DROP TABLE professor;''')
                cursorObj.execute('''UPDATE course SET cprofessor = NULL;''')
                cursorObj.execute('''DROP TABLE course;''')
                cursorObj.execute('''PRAGMA foreign_keys = ON;''')
                subprocess.call("del test7.db", shell=True)
                exit()
            else:
                a,b,c = user_input.split(',')
                a = a.strip()
                b = b.strip()
                c = c.strip()
                results = commandSQL(a, b, c)
        if results:
            for result in results:
                print(result[0])
        else:
            print("That value you are searching for does not exist. Please try a different value.")
        run = input("Would you like to search again? Enter y or n: ")
    print("Goodbye!")
    cursorObj = con.cursor()
    cursorObj.execute('''PRAGMA foreign_keys = OFF;''')
    cursorObj.execute('''DROP TABLE professor;''')
    cursorObj.execute('''UPDATE course SET cprofessor = NULL;''')
    cursorObj.execute('''DROP TABLE course;''')
    cursorObj.execute('''PRAGMA foreign_keys = ON;''')
    subprocess.call("del test7.db", shell=True)

def inputTable():
    con = sqlite3.connect('test7.db')
    cursorObj = con.cursor()
    cursorObj.execute("CREATE TABLE IF NOT EXISTS search(number INTEGER, pName varchar(15), poffice varchar(15), ptitle varchar(20))")
    con.commit()

# a is what it asked (like office or class, etc.)
# b is which professor or known information
# c is the name
# a, b, c example would be "office professor Eddy"
def commandSQL(a, b, c):
    con = sqlite3.connect('test7.db')
    cursorObj = con.cursor()
    # office professor professor's name
    if (a == "office"):
        if (b == "professor"):
            entities = ('NULL', c, 'NULL', 'NULL')
            cursorObj.execute('''INSERT INTO search(number, pName, poffice, ptitle) VALUES(?,?,?,?)''', entities)
            cursorObj.execute('''SELECT p.office FROM professor AS p INNER JOIN search AS s ON p.professorN = s.pName''')
            outputs = cursorObj.fetchall()
            cursorObj.execute('DELETE FROM search')
            con.commit()
            return outputs
        elif (b == "title"):
            entities = ('NULL', 'NULL', 'NULL', c)
            cursorObj.execute('''INSERT INTO search(number, pName, poffice, ptitle) VALUES(?,?,?,?)''', entities)
            cursorObj.execute('''SELECT office From professor AS p INNER JOIN search AS s on p.title = s.ptitle''')
            outputs = cursorObj.fetchall()
            cursorObj.execute('DELETE FROM search')
            con.commit()
            return outputs
    # course professor professor's name
    elif (a == "course"):
        if (b == "professor"):
            entities = ('NULL', c, 'NULL', 'NULL')
            cursorObj.execute('''INSERT INTO search(number, pName, poffice, ptitle) VALUES(?,?,?,?)''', entities)
            cursorObj.execute('''SELECT name From course AS c INNER JOIN search AS s ON c.cprofessor = s.pName ''')
            outputs = cursorObj.fetchall()
            cursorObj.execute('DELETE FROM search')
            con.commit()
            return outputs
    # title professor professor's name
    elif (a == "title"):
        if (b == "professor"):
            entities = ('NULL', c, 'NULL', 'NULL')
            cursorObj.execute('''INSERT INTO search(number, pName, poffice, ptitle) VALUES(?,?,?,?)''', entities)
            cursorObj.execute('''SELECT title From professor AS p INNER JOIN search AS s ON p.professorN = s.pName''')
            outputs = cursorObj.fetchall()
            cursorObj.execute('DELETE FROM search')
            con.commit()
            return outputs
    # room course course name or room CRN CRN number
    elif (a == "room"):
        if (b == "course"):
            entities = ('NULL', 'NULL', c, 'NULL')
            cursorObj.execute('''INSERT INTO search(number, pName, poffice, ptitle) VALUES(?,?,?,?)''', entities)
            cursorObj.execute('''SELECT location From course AS c INNER JOIN search AS s ON c.name = s.poffice ''')
            outputs = cursorObj.fetchall()
            cursorObj.execute('DELETE FROM search')
            con.commit()
            return outputs
        elif (b == "CRN"):
            entities = (c, 'NULL', 'NULL', 'NULL')
            cursorObj.execute('''INSERT INTO search(number, pName, poffice, ptitle) VALUES(?,?,?,?)''', entities)
            cursorObj.execute('''SELECT location From course AS c INNER JOIN search AS s ON c.crn = s.number''')
            outputs = cursorObj.fetchall()
            cursorObj.execute('DELETE FROM search')
            con.commit()
            return outputs
    # enrollment course course name or enrollment CRN CRN number
    elif (a == "enrollment"):
        if (b == "course"):
            entities = ('NULL', 'NULL', c, 'NULL')
            cursorObj.execute('''INSERT INTO search(number, pName, poffice, ptitle) VALUES(?,?,?,?)''', entities)
            cursorObj.execute('''SELECT registered From course AS c INNER JOIN search AS s ON c.name = s.poffice''')
            outputs = cursorObj.fetchall()
            cursorObj.execute('DELETE FROM search')
            con.commit()
            return outputs
        elif (b == "CRN"):
            entities = (c, 'NULL', 'NULL', 'NULL')
            cursorObj.execute('''INSERT INTO search(number, pName, poffice, ptitle) VALUES(?,?,?,?)''', entities)
            cursorObj.execute('''SELECT registered From course AS c INNER JOIN search AS s ON c.crn = s.number''')
            outputs = cursorObj.fetchall()
            cursorObj.execute('DELETE FROM search')
            con.commit()
            return outputs
    else:
        return 1

greeting()