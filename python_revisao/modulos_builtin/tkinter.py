import tkinter as tk


# Criando uma janela
window = tk.Tk()
window.geometry("600x450")
window.title("Manage Phrases")

# Adiciona um Frame
frame = tk.Frame(window)
frame.pack(padx=10, pady=10, fill="x", expand=True)

# Adicionando o Label
label = tk.Label(frame, text="Olá mundo")
label.pack(fill="x", expand=False)

# Adicionando o input text
label_phrase = tk.Label(frame, text="Phrase")
label_phrase.pack(fill="x", expand=True)

phrase_input = tk.Entry(frame)
phrase_input.pack(fill="x", expand=True)

# Função para alterar label
def click():
    label.config(text=phrase_input.get())
    return None

# Adicionando botão 
button = tk.Button(frame, text="Enviar", command=click)
button.pack()

window.mainloop()
