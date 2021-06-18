import sqlite3
from PIL import Image
import re
sqliteConnection = sqlite3.connect('example.db')
cursor = sqliteConnection.cursor()
print("Connected to SQLite")
sql_fetch_blob_query = """SELECT * from photo where id = ?"""
cursor.execute(sql_fetch_blob_query, (1,))
record = cursor.fetchall()

for row in record:
    print("Id = ", row[0])
    photo = row[1]
    size = [int(re.search(r'\d+', i).group()) for i in row[2].split(",")]
    mode = row[3]
    im = Image.frombytes(mode, size, photo)
    im.show()
