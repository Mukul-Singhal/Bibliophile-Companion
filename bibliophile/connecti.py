import sqlite3
from PIL import ImageGrab
con = sqlite3.connect('example.db')
c = con.cursor()

c.execute(
    '''CREATE TABLE IF NOT EXISTS History( timestamp TEXT PRIMARY KEY, TYPE NUMBER NOT NULL ,ID INTEGER NOT NULL)'''
    '''CREATE TABLE IF NOT EXISTS Text(id INTEGER PRIMARY KEY AUTOINCREMENT , Text TEXT) '''
    '''CREATE TABLE IF NOT EXISTS Photo(id INTEGER PRIMARY KEY AUTOINCREMENT , Photo TEXT , size INTEGER , mode TEXT) ''')


def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        blobData = file.read()
    return blobData


def insertBLOB(empId):
    try:
        sqliteConnection = sqlite3.connect('example9.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")
        sqlite_insert_blob_query = """ INSERT INTO new_employee
                                  (id, photo) VALUES (?, ?)"""

        # Convert data into tuple format
        if (image_handler() == None):
            raise("ERROR")
        data_tuple = (empId, image_handler())
        cursor.execute(sqlite_insert_blob_query, data_tuple)
        sqliteConnection.commit()
        print("Image and file inserted successfully as a BLOB into a table")
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert blob data into sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("the sqlite connection is closed")


def image_handler():
    return ImageGrab.grabclipboard().tobytes()

