import tkinter as tk;

root = tk.Tk();
root.geometry("450x250");
root.title("Tkinter Text");

text_widget = tk.Text(root, height=10, width=50);
text_widget.pack();

def get_text():
    text = text_widget.get("1.0", tk.END);
    print(text)

tk.Button(root,text="click" ,command=get_text).pack();

root.mainloop();