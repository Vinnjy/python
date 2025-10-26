import tkinter as tk
class DrawingApp:
    def __init__(self, master):
        self.master = master
        master.title("Простое рисование")

        self.canvas = tk.Canvas(master, width=400, height=300, bg="white")
        self.canvas.pack(pady=10)

        # Координаты для хранения начальных коо
        self.old_x = None
        self.old_y = None

        # Привязка событий мыши
        self.canvas.bind("<Button-1>", self.start_draw) # Нажатие левой кнопки мыши
        self.canvas.bind("<B1-Motion>", self.draw) # Перемещение мыши с зажатой левой кнопкой
        self.canvas.bind("<ButtonRelease-1>", self.reset_coords) # Отпускание левой кнопки мыши

        # Кнопка отчистки окна
        self.clear_button = tk.Button(master, text="Очистить", command=self.clear_canvas)
        self.clear_button.pack(pady=5)

    # Сохраняем начальные координаты при нажатии кнопки мыши
    def start_draw(self, event):
        self.old_x = event.x
        self.old_y = event.y

    # Рисуем линию от предыдущих координат до текущих
    def draw(self, event):
        if self.old_x and self.old_y:
            self.canvas.create_line(self.old_x, self.old_y, event.x, event.y, width=2, fill="blue", capstyle=tk.ROUND, smooth=tk.TRUE)
        self.old_x = event.x
        self.old_y = event.y

    # Сбрасываем координаты при отпускании кнопки мыши
    def reset_coords(self, event):
        self.old_x = None
        self.old_y = None

    # Очищаем Canvas (окно)
    def clear_canvas(self):
        self.canvas.delete("all")

root = tk.Tk()
app = DrawingApp(root)
root.mainloop()