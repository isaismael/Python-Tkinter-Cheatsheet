# en este caso vemos como centrar nuestra ventada en el screen
import tkinter as tk;
import os

root = tk.Tk();
#primero declaramos la variables que las dimensiones que queremos
window_width = 400;
window_height = 300;

screen_width = root.winfo_screenwidth();
screen_height = root.winfo_screenheight();

center_x = int(screen_width/2 - window_width/2);
center_y = int(screen_height/2 - window_height/2);

#usamos el path para guardar en una variable la ruta del icon
icon = os.path.join(os.path.dirname(__file__), "icon.ico")

root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}');
root.title("Ventana centrada en el screen");
root.iconbitmap(icon);
root.config(bg="grey")

root.mainloop();

#vimos camo hacer el calculo para centrar nuestra ventana 
#cambiar icon personalizado usando tmb el path 
#cambio de color de bg