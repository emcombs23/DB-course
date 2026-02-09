import sqlite3
import pandas as pd

conn = sqlite3.connect('../baseball.db')
cursor = conn.cursor()
query = '''
SELECT teamID, SUM(HR) as HRs
FROM batting
WHERE yearID = 2025
GROUP BY teamID
HAVING Hrs > 200
ORDER BY HRs desc;
'''
cursor.execute(query)
results = cursor.fetchall()
for row in results:
    print(row)
df = pd.DataFrame(results, columns=['team', 'HRs'])
print(df)
cursor.close()
