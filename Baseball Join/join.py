import sqlite3
import pandas as pd

conn = sqlite3.connect('../baseball.db')
cursor = conn.cursor()
query = '''
SELECT batting.yearID, name, batting.HR
FROM batting
INNER JOIN teams ON batting.teamID = teams.teamID and batting.yearID = teams.yearID
WHERE playerID = 'ruthba01';
'''
cursor.execute(query)
results = cursor.fetchall()
'''
for row in results:
    print(row)
'''
df = pd.DataFrame(results)
print(df)
cursor.close()