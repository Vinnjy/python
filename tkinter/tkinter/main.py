import tkinter as tk
from tkinter import messagebox

# Button
def button_on_click():
    messagebox.showinfo("Hello", "Hello world")

root = tk.Tk()
root.title("Hello world app")
root.geometry("500x300")

button = tk.Button(root, text="Click on me", command=button_on_click)
button.pack(pady=50)

root.mainloop()




# Label

root = tk.Tk()
root.title("Метка")
root.geometry("500x300")

label = tk.Label(root, text="Текст на метке", font=("Arial", 18), fg="blue", bg="white")
label.pack(pady=20)

root.mainloop()





# Entry (Поле ввода)
def submit_name():
    name = entry.get()
    if name:
        messagebox.showinfo("Hello", f"Hello, {name}")
    else:
        messagebox.showwarning("Warning", "Пожалуйста, введите имя")
root = tk.Tk()
root.title("Поле ввода")
root.geometry("500x300")

label = tk.Label(root, text="Введите имя", font=("Arial", 18), fg="blue", bg="white")
label.pack(pady=20)

entry = tk.Entry(root, width=30) # Ширина поля
entry.pack(pady=5)

button = tk.Button(root, text="Click on me", command=submit_name)
button.pack(pady=10)

root.mainloop()





# Text - текстовое поле

root = tk.Tk()
root.title("Пример Text")
root.geometry("400x300")

text = tk.Text(root, height=10, width=40, wrap="word")
text.pack(pady=20)
text.insert(tk.END, "Многострочное текстовое поле")
text.insert(tk.END, "Введите текст")

def get_text():
 content = text.get("1.0", tk.END)
 print("Содержимое окна:")
 print(content)

button = tk.Button(root, text="Click on me", command=get_text)
button.pack(pady=5)

root.mainloop()





# Checkbutton (Флажок)

def selection_options():
    selection_options = []
    if var1.get():
        selection_options.append("Вариант 1")
    if var2.get():
        selection_options.append("Вариант 2")
    if var3.get():
        selection_options.append("Вариант 3")
    if selection_options:
        print("Выбрано: ", ", ".join(selection_options))
    else:
        print("Выбирай")
root = tk.Tk()
root.title("Флажки")
root.geometry("500x300")

var1 = tk.BooleanVar()
var2 = tk.BooleanVar()
var3 = tk.BooleanVar()

check1 = tk.Checkbutton(root, text="Опция 1", variable=var1, onvalue=True, offvalue=False)
check2 = tk.Checkbutton(root, text="Опция 2", variable=var2, onvalue=True, offvalue=False)
check3 = tk.Checkbutton(root, text="Опция 3", variable=var3, onvalue=True, offvalue=False)

check1.pack(anchor='w', padx=20, pady=5)
check2.pack(anchor='w', padx=20, pady=5)
check3.pack(anchor='w', padx=20, pady=5)

button = tk.Button(root, text="Click on me", command=selection_options)
button.pack(pady=20)

root.mainloop()





# Radiobutton (Переключатель)
def show_selection():
 print("Выбран цвет:", selected_color.get())

root = tk.Tk()
root.title("Переключатель")
root.geometry("500x300")

selected_color = tk.StringVar()
selected_color.set("Красный")

radio1 = tk.Radiobutton(root, text="Красный", variable=selected_color, value="Красный", command=show_selection)
radio2 = tk.Radiobutton(root, text="Зеленый", variable=selected_color, value="Зеленый", command=show_selection)
radio3 = tk.Radiobutton(root, text="Синий", variable=selected_color, value="Синий", command=show_selection)

radio1.pack(anchor="w", padx=20, pady=5)
radio2.pack(anchor="w", padx=20, pady=5)
radio3.pack(anchor="w", padx=20, pady=5)

root.mainloop()





# Scale (Ползунок)

def show_value(val):
 print("Выбранное значение:", int(float(val)))

root = tk.Tk()
root.title("Ползунок")
root.geometry("500x300")

scale = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, label="Выберите значение:", command=show_value)

scale.set(50)
scale.pack(pady=20)

root.mainloop()





# pack()

root = tk.Tk()
root.title("Метод pack()")
root.geometry("500x300")

button_one = tk.Button(root, text="Кнопка 1")
button_one.pack(pady=5)

button_two = tk.Button(root, text="Кнопка 2")
button_two.pack(pady=5)

frame = tk.Frame(root, bd=2, relief="groove")
frame.pack(pady=10)

button_1 = tk.Button(frame, text="Левая")
button_1.pack(side=tk.LEFT, padx=10)

button_2 = tk.Button(frame, text="Правая")
button_2.pack(side=tk.RIGHT, padx=10)

root.mainloop()





# grid()

root = tk.Tk()
root.title("Метод grid()")
root.geometry("500x300")

label_name = tk.Label(root, text="Имя:")
entry_name = tk.Entry(root)

label_email = tk.Label(root, text="Email:")
entry_email = tk.Entry(root)

label_name.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
entry_name.grid(row=0,column=1,padx=5,pady=5,sticky=tk.EW)

label_email.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
entry_email.grid(row=1, column=1, padx=5, pady=5, sticky=tk.EW)

button = tk.Button(root, text="Отправить")
button.grid(row=2, column=0, columnspan=2, pady=10)

root.grid_columnconfigure(1, weight=1)

root.mainloop()





# place()

root = tk.Tk()
root.title("Метод place()")
root.geometry("500x300")

button_1 = tk.Button(root, text="Абсолютное позиционирование")
button_1.place(x=10,y=10)

button_2 = tk.Button(root, text="Относительное позиционирование")
button_2.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

root.mainloop()




# Frame

root = tk.Tk()
root.title("Frame")
root.geometry("400x300")

top_frame = tk.Frame(root, bd=2, relief="raised")
top_frame.pack(side=tk.TOP, fill=tk.X, pady=10, padx=10)

label_top = tk.Label(top_frame, text="Верхняя панель")
label_top.pack(pady=5)
button_top = tk.Button(top_frame, text="Кнопка вверху")
button_top.pack(pady=5)

bottom_frame = tk.Frame(root, bd=2, relief="sunken")
bottom_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True, pady=10, padx=10)

label_bottom = tk.Label(bottom_frame, text="Нижняя панель")
label_bottom.pack(pady=5)
entry_bottom = tk.Entry(bottom_frame, width=30)
entry_bottom.pack(pady=5)

root.mainloop()