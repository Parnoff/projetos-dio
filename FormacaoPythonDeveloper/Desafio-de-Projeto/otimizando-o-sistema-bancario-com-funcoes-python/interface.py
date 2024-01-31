import tkinter as tk

# Criar uma instância da classe Tkinter
root = tk.Tk()

# Adicionar um rótulo (label)
label = tk.Label(root, text="Olá, Tkinter!")
label.pack()

# Adicionar um botão
button = tk.Button(root, text="Clique em mim!", command=on_button_click)
button.pack()

# Iniciar o loop principal da interface gráfica
root.mainloop()