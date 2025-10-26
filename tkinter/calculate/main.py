import tkinter as tk
def show(x):
    value = entry_1.get()
    entry_1.insert(tk.END, str(x))
def show_C():
    entry_1.delete(0, tk.END)
def show_equals():
    res = entry_1.get()
    entry_1.delete(0, tk.END)
    try:
        result = eval(res)
        entry_1.insert(0, str(result))
    except:
        entry_1.insert(0, "Error")

root = tk.Tk()
root.title("Calculate")
root.geometry("300x300")
root.config(bg="gray15")
entry_1 = tk.Entry(root, bd=0, font=("Arial", 20), fg="white smoke", bg="gray20")
entry_1.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)
buttons = ["+", "-", "*", "/", "1", "2", "3", "C", "4", "5", "6", "=", "7", "8", "9", "0"]
row = 1
column = 0
for i in range(len(buttons)):
    if i != 0 and i % 4 == 0:
        row += 1
        column = 0
    if i < 4:
        button = tk.Button(root, bd=0, text=buttons[i], font=('Arial', 20), fg="gray10", bg='chocolate2', command=lambda x=buttons[i]: show(x))
        button.grid(row=row, column=column, sticky="nsew", ipadx=20, ipady=5, padx=2, pady=2) # ipadx=20, ipady=5,
    else:
        if i == 7:
            button = tk.Button(root, bd=0, text=buttons[i], font=('Arial', 20), fg='black', bg='gray70', command=show_C)
            button.grid(row=row, column=column, sticky="nsew", ipadx=20, ipady=5, padx=2, pady=2)
        elif i == 11:
            button = tk.Button(root, bd=0, text=buttons[i], font=('Arial', 20), fg='black', bg='gray70',command=show_equals)
            button.grid(row=row, column=column, sticky="nsew", ipadx=20, ipady=5, padx=2, pady=2)
        else:
            button = tk.Button(root, bd=0, text=buttons[i], font=('Arial', 20), fg='black', bg='gray57', command=lambda x=buttons[i]: show(x))
            button.grid(row=row, column=column, sticky="nsew", ipadx=20, ipady=5, padx=2, pady=2)
    column += 1
for i in range(5):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

root.mainloop()