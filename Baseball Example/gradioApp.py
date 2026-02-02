import sqlite3
import gradio as gr
import pandas as pd

def getPlayers():
    conn = sqlite3.connect('baseball.db')
    cursor = conn.cursor()

    query = '''
        SELECT DISTINCT playerID
        FROM batting
        WHERE yearID = 1976 AND teamID = 'PHI';
    '''

    cursor.execute(query)

    records = cursor.fetchall()
    conn.close()
    result = []
    for record in records:
        result.append(record[0])
    return result

def getHomers(player):
    conn = sqlite3.connect('baseball.db')
    cursor = conn.cursor()
    query = """
        SELECT HR
        FROM batting
        WHERE playerID = ? AND yearID = 1976 AND teamID = 'PHI'
    """
    cursor.execute(query,[player]) 
    records = cursor.fetchall()
    return records[0][0] if records else 0


#players = getPlayers()
#print(players,len(players))

with gr.Blocks() as iface:
    playerID = gr.Dropdown(choices = getPlayers(),interactive = True)
    homeruns = gr.Number()
    playerID.change(fn = getHomers,  inputs=[playerID],  outputs=[homeruns])

iface.launch()