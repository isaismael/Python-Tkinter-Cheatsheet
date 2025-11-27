#los widget son creados como una istancia de una class
#el primer argumento siempre es el parent container
#osea el contenedor padre donde estará, ej; root o tk.Frame
#todas las otros argumentos son opciones de configuraciones
#tmb llamados keyword arguments

import tkinter as tk

root = tk.Tk()

tk.Label(root, 
         text="Esto es un label", 
         font=("Arial", 20),
         fg="black",
         bg="grey"
         ).pack();

entry = tk.Entry(root, width=30, show="*");
entry.pack();


def on_click():
    input_entry = entry.get()
    print(f'El valor de entry: {input_entry}');

tk.Button(root, text="Click", command=on_click, activebackground="grey").pack();


root.mainloop();
