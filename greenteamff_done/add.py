import sqlite3
from typing import Iterable

conn = sqlite3.connect('db.sqlite')
page_id = '10'
cur = conn.cursor()
data = cur.execute('SELECT * FROM Product WHERE id = ?',page_id).fetchall()
print(data)


