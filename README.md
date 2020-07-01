# sqlitecon
Connect , CREATE , INSERT , UPDATE, SELECT and DELETE your SQLite Database with  running just one script.<br><br>
To use thsis method run the __init__.py script in IDLE <br>
<p>The methods inside this modules:<br><br>
  <strong>connectdb(dbname)</strong>: Connects to a database and returns the sqlite.connect() object <br>
<strong>set_db(dbname)</strong>: Connect to a new database from within the script without loading it again.<br>
<strong>closedb()</strong>: closes the connection to a database whenever the user wants <br>
<strong>get_dbname()</strong>: To get the database name.<br>
<strong>createTable()</strong>: Create a table in the database with an example in the prompt
                so the user can copy it and edit it according to their needs.<br>
<strong>fetch()</strong>: Fetchs or SELECTs data from the database. It uses fetchall.
        This also has an example in the prompt so the user can copy it and edit it according to their needs.<br>
<strong>insertdb()</strong>:Insert a new record in the table.
            This also has an example in the prompt so the user can copy it and edit it according to their needs.<br>
<strong>update()</strong>: This method updates an already existing record.
            This method first asks for information from the user to select the row which you want to update,
            then asks for row name where you want the changes and then the new value.<br>
<strong>delete()</strong>:  This method deletes an already existing record.
            This method first asks for information from the user to select the row which you want to delete,
            then shows the record selected and deletes it from the table and shows the remaining records.<br></p>
