import sqlite3
import pandas as pd

conn = sqlite3.connect('../baseball.db')
cursor = conn.cursor()
query = '''
SELECT yearID, SUM(HR) as HRs
FROM batting
WHERE teamID = 'PHI'
GROUP BY yearID
ORDER BY yearID;
'''
cursor.execute(query)
results = cursor.fetchall()
for row in results:
    print(row)
df = pd.DataFrame(results, columns=['playerID', 'HRs'])
print(df)
cursor.close()
