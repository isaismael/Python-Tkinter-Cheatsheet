import tkinter as tk;

root = tk.Tk();
root.title("App Tkinter");
root.geometry("650x400");
root.resizable(width=False, height=False);

label = tk.Label(root, text="Hola desde Tkinter!");
label.pack();

root.mainloop();

#el metodo mainloop es crucial, representa un loop infinito
#lo necesitamos para que la app se inicialice
#este loop infinito espera por eventos (button click, press key, mouse movements)