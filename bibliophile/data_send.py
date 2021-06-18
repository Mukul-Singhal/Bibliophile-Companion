import sqlite3
from PIL import ImageGrab
import io
from PIL import Image
con = sqlite3.connect('example.db')
c = con.cursor()

c.execute(
    '''CREATE TABLE IF NOT EXISTS new_employee( id INTEGER PRIMARY KEY, photo BLOB NOT NULL, size text NOT NULL, mode text NOT NULL)''')
def insertBLOB(empId):
    try:
        sqliteConnection = sqlite3.connect('example.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")
        sqlite_insert_blob_query = """ INSERT INTO new_employee
                                  (id, photo,size,mode) VALUES (?, ?,?,?)"""
        im = ImageGrab.grabclipboard()
        if (im == None):
            raise ("No Image Found")
        data_tuple = (empId, im.tobytes(), str(im.size), im.mode)

        cursor.execute(sqlite_insert_blob_query, data_tuple)
        sqliteConnection.commit()
        print("Image and file inserted successfully as a BLOB into a table")
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert blob data into sqlite table,", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("the sqlite connection is closed")
insertBLOB(1)
