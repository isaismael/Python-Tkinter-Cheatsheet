import tkinter as tk

root = tk.Tk()
root.geometry("450x250")
root.title("Tkinter Text")

is_checked = tk.IntVar();

check = tk.Checkbutton(root, text="Acepto", variable=is_checked)
check.pack()

text_widget = tk.Text(root, height=10, width=50)
text_widget.pack()


def get_text():
    text = text_widget.get("1.0", tk.END)
    check_var = is_checked.get()
    if check_var == 1:
        print("el check esta presionado")
    else:
        print("El check no está presionado")
    print(text)


tk.Button(root, text="click", command=get_text).pack()

root.mainloop()