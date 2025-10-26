import tkinter as tk

root = tk.Tk()
root.title("Фигуры")
root.geometry("600x400")

canvas = tk.Canvas(root, width=580, height=380, bg="white", bd=2, relief="groove")
canvas.pack(pady=10, padx=10)

canvas.create_line(70, 70, 200, 70, fill="red", width=5, dash=(2,5))
canvas.create_text(135, 50, text="Линия", fill="blue", font=("Arial", 20))

canvas.create_rectangle(70, 120, 200, 200, fill="red", outline="black", width=2)
canvas.create_text(140, 220, text="Прямоугольник", fill="blue", font=("Arial", 20))

canvas.create_oval(350, 30, 500, 100, fill="orange", outline="chocolate3", width=2)
canvas.create_text(425, 120, text="Овал", fill="blue", font=("Arial", 20))

canvas.create_polygon(350, 250, 420, 150, 500, 250, fill="orange", outline="chocolate3", width=2)
canvas.create_text(425, 270, text="Треугольник", fill="blue", font=("Arial", 20))

canvas.create_arc(70, 250, 200, 350, start=0, extent=180, fill="purple", outline="darkviolet", width=2, style=tk.ARC)
canvas.create_text(135, 285, text="Дуга", fill="blue", font=("Arial", 20))

root.mainloop()