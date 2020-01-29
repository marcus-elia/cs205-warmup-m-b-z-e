import csv, sqlite3

# Initializing variables
sqliteFile1 = 'courses.csv'
sqliteFile2 = 'professors.csv'
table1 = 'Table1'
table2 = 'Table2'
id = 'Rank'
course = 'Courses'
crn = 'CRN'
classSize = 'Number of Students'
professor = 'Professor'
office = 'Office Location'
columnType = 'TEXT'

cur.execute("CREATE TABLE t1 (id, courses, crn, classSize, professor);")
cur.execute("CREATE TABLE t2 (id, professor, office);")

with open('courses.csv','rb') as fin:
    dr = csv.DictReader(fin)
    toDB = [(i['id'],i['courses'],i['crn'],i['classSize'],i['professor']) for i in dr]

with open('professors.csv','rb') as fin:
    dr = csv.DictReader(fin)
    toDB = [(i['id'],i['professor'],i['office']) for i in dr]

# Establishing connection
def connect(sqliteFile):
    conn = sqlite3.connect(":memory:")
    c = conn.cursor()
    return conn, c

# Closing the connection
def close(conn):
    conn.close()
    
# Getting total number of rows
def total_rows(cursors, tableName, printOut=False):
    cursor.execute('SELECT COUNT(*) FROM {}'.format(tableName))
    count = cursor.fetchall()
    if printOut:
        print('\nTotal rows: {}'.format(count[0][0]))
    return count[0][0]










