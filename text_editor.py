import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

def open_file(window, text_edit):
    filepath = askopenfilename(filetypes=[("Text Files", "*.txt")])

    if not filepath:
        return
    
    text_edit.delete(1.0, tk.END)
    with open(filepath, "r") as f:
        content = f.read()
        text_edit.insert(tk.END, content)
    window.title("Open file: {filepath}")
    

def save_file(window, text_edit):
    filepath = asksaveasfilename(filetypes=[("Text files", "*.txt")])

    if not filepath:
        return
    
    with open(filepath, "w") as f:
        content = text_edit.get(1.0, tk.END)
        f.write(content)
    window.title("Open File: {filepath}")


def main():
    window = tk.Tk()
    window.title("Text Editor")
    window.rowconfigure(0, minsize = 400)
    window.columnconfigure(1, minsize = 500)


    text_edit = tk.Text(window, font="Helvetica 18")
    text_edit.grid(row = 0, column = 1)

    frame = tk.Frame(window, relief = tk.RAISED, bd=2)
    save_buttom = tk.Button(frame, text="Save", command = lambda: save_file(window, text_edit))
    open_buttom = tk.Button(frame, text="Open", command = lambda: open_file(window, text_edit) )

    save_buttom.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
    open_buttom.grid(row=1, column=0, padx=5, sticky="ew")
    frame.grid(row=0, column=0, sticky="ns")

    window.bind("<Control-s>", lambda x: save_file(window, text_edit))
    window.bind("<Control-o>", lambda x: open_file(window, text_edit))



    window.mainloop()

main()