import sqlite3
import pandas as pd

conn = sqlite3.connect('baseball.db')
cursor = conn.cursor()


query = '''
    SELECT playerID, teamID, yearID, HR
    FROM batting
    WHERE yearID = 1976 AND teamID = 'PHI' AND HR>0
    ORDER BY HR DESC;
'''

cursor.execute(query)

records = cursor.fetchall()

conn.close()
df = pd.DataFrame(records, columns = ['playerID', 'team', 'year', 'HRs'])
print(df)