import gradio as gr

def squareNum(x):
    return x**2




iface = gr.Interface(fn=squareNum, inputs=gr.Number(), outputs=gr.Number())
iface.launch()