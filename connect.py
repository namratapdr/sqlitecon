#sqlite package
#Connection to sqlite using python
import sqlite3
dbname = input("Enter the name of the database: ")

def connectdb(dbname):
    "Connects to DB"
    try:
        print("Connected to DB.")
        return sqlite3.connect(''+dbname+'.db')
    except:
        print("Error in connection.")
db=connectdb(dbname)
cursordb = db.cursor()
def set_db(dbname):
    db=connectdb(dbname)
    cursordb = db.cursor()
def closedb():
    print("Connection to database is closed.")
    db.close() #closes the connection
def get_dbname():
    return dbname
def createTable():
    sql = input('''Enter the sql instruction for creating a table for eg:
    CREATE TABLE Hogwarts (Id   INTEGER PRIMARY KEY,Name   TEXT,Patronus  TEXT,House  TEXT,OWLs  INTEGER); where Hogwarts is the name of the table and inside it are names of rows :
    ''')
    try:
        cursordb.execute(sql)
        print("Table Created")
    except:
        print("Error in operation.")
        closedb()

def fetch():
    "fetch records from the database"
    try:
        sql=input("Enter SELECT sqlite query for example: SELECT * FROM tablename WHERE rowname='some values'; :")
        cursordb.execute(sql)
        #fetchone : fetchs one record at a time
        '''while True:
            record= self.cursordb.fetchone();
            if record==None:
                break
            print(record)'''
        #fetchall:  fetchs as a list of tuple
        result=cursordb.fetchall()
        for rec in result:
            print(rec)
    except:
        print("Error in operation.")
