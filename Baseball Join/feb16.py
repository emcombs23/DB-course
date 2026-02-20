import sqlite3
import pandas as pd  
import gradio as gr  

conn = sqlite3.connect('../baseball.db')
cursor = conn.cursor()
query = """
WITH top_hitters AS (SELECT nameFirst,nameLast, people.playerID
    FROM batting INNER JOIN people
    ON batting.playerID = people.playerID
    WHERE teamID = 'PHI'
    GROUP BY batting.playerID
    ORDER BY sum(HR) desc
    LIMIT 10)
SELECT CONCAT(nameFirst,' ',nameLast) as player,  playerID
FROM top_hitters
ORDER BY nameLast
"""
cursor.execute(query)
records = cursor.fetchall()
conn.close()

players = []
ids = []
for record in records:
    players.append((record[0],record[1]))
print(players)
print(records)


def getHomers(playerID):
    conn = sqlite3.connect('../baseball.db')
    cursor = conn.cursor()
    query = f"""
    SELECT CAST(yearID AS TEXT) AS yearID, sum(HR) as total_HR
    FROM batting
    WHERE playerID = '{playerID}' AND teamID = 'PHI'
    GROUP BY yearID
    """
    cursor.execute(query)
    results = cursor.fetchall()
    df = pd.DataFrame(results, columns=['Year', 'HomeRuns'])
    conn.close()
    return df






with gr.Blocks() as iface:
    playerOptions = gr.Dropdown(choices = players,interactive = True)
    plot = gr.LinePlot(x="Year", y="HomeRuns", title="Home Runs by Year")
    playerOptions.change(fn = getHomers,  inputs=[playerOptions],  outputs=[plot])

iface.launch()
