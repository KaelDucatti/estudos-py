import gradio as gr


def converter_temp(temp, scale):
    if scale == "C˚":
        return (temp * 9/5) + 32
    else:
        return (temp - 32) * 5/9
    
iface = gr.Interface(
    fn=converter_temp,
    inputs=[
        gr.Number(label="Temperature value: "),
        gr.Radio(
            choices=["C˚", "F˚"],
            label="Convert from ",
        ),
    ],
    outputs=gr.Number(label="Result", precision=2),
    title="Temperature Converter",
    description="Easy way to convert C° to F° and vice versa",
)

iface.launch()
