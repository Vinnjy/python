import tkinter as tk
class Interactive:
    def __init__(self, master):
        self.master = master
        master.title("Интерактивное приложение")

        self.canvas = tk.Canvas(master, width=500, height=400, bg="white", bd=2, relief="groove")
        self.canvas.pack(pady=10)

        self.start_x = None
        self.start_y = None

        self.current_figure = "line"

        self.current_item = None

        self.canvas.bind("<ButtonPress-1>", self.on_button_press)
        self.canvas.bind("<B1-Motion>", self.on_mouse_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_button_release)

        frame = tk.Frame(master)
        frame.pack(pady=10)

        line = tk.Button(frame, text="Линия", command=lambda: self.set_tool("line"))
        line.pack(side=tk.LEFT, padx=10)

        rectangle = tk.Button(frame, text="Прямоугольник", command=lambda: self.set_tool("rectangle"))
        rectangle.pack(side=tk.LEFT, padx=10)

        oval = tk.Button(frame, text="Овал", command=lambda: self.set_tool("oval"))
        oval.pack(side=tk.LEFT, padx=10)

        btn = tk.Button(frame, text="Очистить", command=self.clear_canvas)
        btn.pack(side=tk.LEFT, padx=10)

    def clear_canvas(self):
        self.canvas.delete("all")

    def set_tool(self, figure):
        self.current_figure = figure

    def on_button_press(self, event):
        self.start_x = event.x
        self.start_y = event.y
        self.current_item = None

    def on_mouse_drag(self, event):
        # Проверка, если кнопка нажата из вне
        if self.start_x is None and self.start_y is None:
            return

        # Удаляем элемент предыдущий, чтобы нарисовать следующий.
        if self.current_item:
            self.canvas.delete(self.current_item)

        # Рисуем
        if self.current_figure == "line":
            self.current_item = self.canvas.create_line(self.start_x, self.start_y, event.x, event.y, fill="blue", width=2)
        elif self.current_figure == "rectangle":
            self.current_item = self.canvas.create_rectangle(self.start_x, self.start_y, event.x, event.y, outline="red", width=2)
        elif self.current_figure == "oval":
            self.current_item = self.canvas.create_oval(self.start_x, self.start_y, event.x, event.y, outline="orange", width=2)

    def on_button_release(self, event):
        # Удаляем элемент предыдущий, чтобы нарисовать следующий.
        if self.current_item:
            self.canvas.delete(self.current_item)

        # Рисуем окончательный элемент
        if self.current_figure == "line":
            self.current_item = self.canvas.create_line(self.start_x, self.start_y, event.x, event.y, fill="blue",width=2)
        elif self.current_figure == "rectangle":
            self.current_item = self.canvas.create_rectangle(self.start_x, self.start_y, event.x, event.y, outline="red", width=2)
        elif self.current_figure == "oval":
            self.current_item = self.canvas.create_oval(self.start_x, self.start_y, event.x, event.y, outline="orange", width=2)

        self.start_x = None
        self.start_y = None
        self.current_item = None

root = tk.Tk()
app = Interactive(root)
root.mainloop()