#creating records in DB
import sqlite3
from connect import *

def insertdb():
    """Creates records into the database."""
#error/exception handling using try-except
    try:
        #Change the values according the database if user input is preferd
        sql= input('''Enter sqlite commands to insert into a table according to your databse for example: INSERT INTO students (Id,Name,Patronus,House,OWLs) VALUES (12,"Harry Potter","Stag","Gryffindor",3); :
        ''')
        #change the table names according the database
        cursordb.execute(sql)
        db.commit()
        print("Record created succesfully")

    except:
        print("Error in operation")
        db.rollback()
