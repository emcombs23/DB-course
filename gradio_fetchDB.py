import gradio as gr
import sqlite3
import pandas as pd

def fetchPoints():
    conn = sqlite3.connect('points.db')
    cursor = conn.cursor()
    query = '''
        SELECT *
        FROM points;
    '''
    cursor.execute(query)
    result = cursor.fetchall()
    conn.close()
    df = pd.DataFrame(result, columns=['id', 'x', 'y'])
    return df




iface = gr.Interface(fn=fetchPoints, inputs=[], outputs=gr.Dataframe(headers = ['id', 'x', 'y']))
iface.launch()