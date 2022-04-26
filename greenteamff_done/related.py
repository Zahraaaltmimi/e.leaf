from cs50 import SQL
import sqlite3

page_id =5
db = SQL("sqlite:///db.sqlite")
data = db.execute('SELECT * FROM Product WHERE id = ?', page_id)
print(data[0]['id'])
conn = sqlite3.connect('db.sqlite')
cursor = conn.cursor()
related = cursor.execute('SELECT * FROM Product WHERE id != ? AND categories = ?', (data[0]['id'], data[0]['categories'])).fetchall()
print(related[1])