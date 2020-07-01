#fetching records in DB
import sqlite3
from connect import *
def update():
    """Update records in the database."""
    #error/exception handling using try-except
    "Updates the values of a row in database"
    tablename = input("Enter the name of the table: ")
    rowname=input("Enter the row name which has unique values (Name,Id,Number) by which you want to select the row: ")
    rowvalue = input("Enter the unique value of the row you just entered to select an entry: ")

    sql="SELECT * FROM "+tablename+" WHERE "+rowname+"='"+rowvalue+"';"
    cursordb.execute(sql)
    record = cursordb.fetchone()
    print(record)
    try:
        rowname=input("Enter the name of the row which you want to change: ")
        updated=input("Enter new value of : ")
        sql="UPDATE "+tablename+" SET "+rowname+"='"+str(updated)+"' WHERE Name='"+rowvalue+"';"
        cursordb.execute(sql)
        db.commit()
        cursordb.execute("SELECT * FROM "+tablename+";")
        print("Updated records:")
        result = cursordb.fetchall()
        for rec in result:
            print(rec)
    except:
        print("Error in operation")
        db.rollback()
def delete():
    "Deletes a record from the database"
    "Updates the values of a row in database"
    tablename=input("Enter the name of the table: ")
    rowname=input("Enter the row name which has unique values (Name,Id,Number) by which you want to select the row: ")
    rowvalue =input("Enter the unique value of the row you just entered to select an entry: ")

    sql="SELECT * FROM "+tablename+" WHERE "+rowname+"='"+rowvalue+"';"
    cursordb.execute(sql)
    record = cursordb.fetchone()
    print(record)
    try:
        sql="DELETE FROM "+tablename+" WHERE "+rowname+"='"+rowvalue+"';"
        cursordb.execute(sql)
        db.commit()
        cursordb.execute("SELECT * FROM "+tablename+";")
        print("Updated records:")
        result = cursordb.fetchall()
        for rec in result:
            print(rec)
    except:
        print("Error in operation")
        db.rollback()
