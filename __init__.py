#sqlite package
#Connection to sqlite using python
'''
The methods inside this modules:
connectdb(dbname): Connects to a database and returns the sqlite.connect() object
set_db(dbname): Connect to a new database from within the script without loading it again.
closedb(): closes the connection to a database whenever the user wants
get_dbname(): To get the database name.
createTable(): Create a table in the database with an example in the prompt
                so the user can copy it and edit it according to their needs.
fetch(): Fetchs or SELECTs data from the database. It uses fetchall.
        This also has an example in the prompt so the user can copy it and edit it according to their needs.
insertdb():Insert a new record in the table.
            This also has an example in the prompt so the user can copy it and edit it according to their needs.
update(): This method updates an already existing record.
            This method first asks for information from the user to select the row which you want to update,
            then asks for row name where you want the changes and then the new value.
delete():  This method deletes an already existing record.
            This method first asks for information from the user to select the row which you want to delete,
            then shows the record selected and deletes it from the table and shows the remaining records.
'''
from connect import *
from insert import *
from update import *
