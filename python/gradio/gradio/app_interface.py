import gradio as gr


def customize_text(text, background_color, color, font_size, font_family):
    style = (
        f"color: {color};"
        f"background-color: {background_color};"
        f"font-size: {font_size}px;"
        f"font-family: {font_family};"
    )
    return f'<div style="{style}">{text}</div>'


customize_text(
    text="Kael, o cruel",
    background_color="#000000",
    color="#ffffff",
    font_size=12,
    font_family="Arial",
)

iface = gr.Interface(
    fn=customize_text,
    inputs=[
        gr.Textbox(label="Text", placeholder="Enter with your text here..."),
        gr.ColorPicker(label="Select your background color..."),
        gr.ColorPicker(label="Select your text color..."),
        gr.Slider(minimum=10, maximum=100, label="Font-size...", value=20),
        gr.Radio(
            label="Font-family...",
            choices=["Arial", "Courier New", "Georgia", "Times New Roman", "Verdana"],
        ),
    ],
    outputs=gr.HTML(label="Custom text"),
    title="Customize text",
    description="Customize your text...",
)

iface.launch()
