import sqlite3
import sys
import os
import subprocess

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
            print(outputs)
            cursorObj.execute('DELETE FROM search')
            con.commit()
        elif (b == "title"):
            entities = ('NULL', 'NULL', 'NULL', c)
            cursorObj.execute('''INSERT INTO search(number, pName, poffice, ptitle) VALUES(?,?,?,?)''', entities)
            cursorObj.execute('''SELECT office From professor AS p INNER JOIN search AS s on p.professorN = s.ptitle''', c)
            outputs = cursorObj.fetchall()
            for output in outputs:
                print(output)
            cursorObj.execute('DELETE FROM search')
            con.commit()
    # course professor professor's name
    elif (a == "courses"):
        if (b == "professor"):
            entities = ('NULL', c, 'NULL', 'NULL')
            cursorObj.execute('''INSERT INTO search(number, pName, poffice, ptitle) VALUES(?,?,?,?)''', entities)
            cursorObj.execute('''SELECT name From course AS c INNER JOIN search AS s ON c.cprofessor = s.pName ''')
            outputs = cursorObj.fetchall()
            for output in outputs:
                print(output)
            cursorObj.execute('DELETE FROM search')
            con.commit()
    # title professor professor's name
    elif (a == "title"):
        entities = ('NULL', 'NULL', 'NULL', c)
        cursorObj.execute('''INSERT INTO search(number, pName, poffice, ptitle) VALUES(?,?,?,?)''', entities)
        cursorObj.execute('''SELECT title From professor AS p INNER JOIN search AS s ON p.title = s.ptitle''')
        outputs = cursorObj.fetchall()
        for output in outputs:
            print(output)
        cursorObj.execute('DELETE FROM search')
        con.commit()
    # room course course name or room CRN CRN number
    elif (a == "room"):
        if (b == "course"):
            entities = ('NULL', 'NULL', c, 'NULL')
            cursorObj.execute('''INSERT INTO search(number, pName, poffice, ptitle) VALUES(?,?,?,?)''', entities)
            cursorObj.execute('''SELECT location From course AS c INNER JOIN search AS s ON c.name = p.poffice ''')
            outputs = cursorObj.fetchall()
            for output in outputs:
                print(output)
            cursorObj.execute('DELETE FROM search')
            con.commit()
        elif (b == "CRN"):
            entities = (c, 'NULL', 'NULL', 'NULL')
            cursorObj.execute('''INSERT INTO search(number, pName, poffice, ptitle) VALUES(?,?,?,?)''', entities)
            cursorObj.execute('''SELECT location From course AS c INNER JOIN search AS s ON c.crn = s.number''')
            outputs = cursorObj.fetchall()
            for output in outputs:
                print(output)
            cursorObj.execute('DELETE FROM search')
            con.commit()
    # enrollment course course name or enrollment CRN CRN number
    elif (a == "enrollment"):
        if (b == "course"):
            entities = ('NULL', 'NULL', c, 'NULL')
            cursorObj.execute('''INSERT INTO search(number, pName, poffice, ptitle) VALUES(?,?,?,?)''', entities)
            cursorObj.execute('''SELECT registered From course AS c INNER JOIN search AS s ON c.name = p.poffice''')
            outputs = cursorObj.fetchall()
            for output in outputs:
                print(output)
            cursorObj.execute('DELETE FROM search')
            con.commit()
        elif (b == "CRN"):
            entities = (c, 'NULL', 'NULL', 'NULL')
            cursorObj.execute('''INSERT INTO search(number, pName, poffice, ptitle) VALUES(?,?,?,?)''', entities)
            cursorObj.execute('''SELECT registered From course AS c INNER JOIN search AS s ON c.crn = p.number''')
            outputs = cursorObj.fetchall()
            for output in outputs:
                print(output)
            cursorObj.execute('DELETE FROM search')
            con.commit()

