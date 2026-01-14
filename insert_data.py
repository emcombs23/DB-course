import sqlite3

conn = sqlite3.connect('points.db')
cursor = conn.cursor()

query = '''
    INSERT INTO points (x, y) 
    VALUES (6, 9);
'''

cursor.execute(query)

conn.commit()
conn.close()