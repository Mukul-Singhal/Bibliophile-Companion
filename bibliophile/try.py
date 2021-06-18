import sqlite3
import datetime
from PIL import ImageGrab
con = sqlite3.connect('example.db')
c = con.cursor()
c.execute(
    '''CREATE TABLE IF NOT EXISTS History( timestamp TEXT PRIMARY KEY, TYPE NUMBER NOT NULL ,ID INTEGER NOT NULL)''')
c.execute('''CREATE TABLE IF NOT EXISTS Text(id INTEGER PRIMARY KEY AUTOINCREMENT , Text TEXT) ''')
c.execute('''CREATE TABLE IF NOT EXISTS Photo(id INTEGER PRIMARY KEY AUTOINCREMENT , Photo TEXT , size INTEGER , mode TEXT) ''')
def history(timestamp , TYPE , ID ):
    sqliteConnection = sqlite3.connect('example.db')
    cursor = sqliteConnection.cursor()
    print("Connected to SQLite")
    sqlite_insert_blob_query = """ INSERT INTO History
                                  (timestamp, TYPE,ID) VALUES (?, ?,?)"""

        # Convert data into tuple format
#if (image_handler() == None):
 #   raise("ERROR")
    data_tuple = (timestamp , TYPE , ID)
    cursor.execute(sqlite_insert_blob_query, data_tuple)
    sqliteConnection.commit()
    print("Image and file inserted successfully as a BLOB into a table")
    cursor.close()
type=1
id=1
history(str(datetime.datetime.now()),type,id)