import gradio as gr

def squareNum(x, y):
    return x+y


with gr.Blocks() as iface:
    with gr.Row():
        with gr.Column():
            entry = gr.Number(label = "Input a number")
        with gr.Column():
            entry2 = gr.Number(label = "Input a number")
    output = gr.Number()
    entry.change(fn = squareNum, inputs = [entry, entry2], outputs = output)
    entry2.change(fn = squareNum, inputs = [entry, entry2], outputs = output)
iface.launch()