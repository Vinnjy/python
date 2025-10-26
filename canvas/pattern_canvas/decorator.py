import tkinter as tk
import abc
 # Компонент: Базовый виджет (интерфейс)
class WidgetComponent(abc.ABC):
    @abc.abstractmethod
    def get_widget(self) -> tk.Widget:
        pass
    @abc.abstractmethod
    def get_description(self) -> str:
        pass
 # Конкретный Компонент: Простая метка
class SimpleLabel(WidgetComponent):
    def __init__(self, master, text):
        self._label = tk.Label(master, text=text, padx=10, pady=5, bg="lightgray")
    def get_widget(self) -> tk.Widget:
        return self._label
    def get_description(self) -> str:
        return "Простая метка"
 # Декоратор: Базовый класс для декораторов виджетов
class WidgetDecorator(WidgetComponent, abc.ABC):
    def __init__(self, decorated_widget: WidgetComponent):
        self._decorated_widget = decorated_widget
    def get_widget(self) -> tk.Widget:
        return self._decorated_widget.get_widget()
    @abc.abstractmethod
    def get_description(self) -> str:
        pass
 # Конкретные Декораторы: Добавление функциональности/визуальных эффектов
class BorderDecorator(WidgetDecorator):
    def __init__(self, decorated_widget: WidgetComponent, border_width=2, relief="solid"):
        super().__init__(decorated_widget)
        self._decorated_widget.get_widget().config(bd=border_width, relief=relief)
    def get_description(self) -> str:
        return self._decorated_widget.get_description() + " с рамкой"
class ClickableDecorator(WidgetDecorator):
    def __init__(self, decorated_widget: WidgetComponent, command):
        super().__init__(decorated_widget)
        self._command = command
        self._decorated_widget.get_widget().bind("<Button-1>", self._on_click)
        self._decorated_widget.get_widget().config(cursor="hand2") # Изменяем курсор
    def _on_click(self, event):
        self._command()
    def get_description(self) -> str:
        return self._decorated_widget.get_description() + " (кликабельная)"

# GUI-приложение, использующее декоратор
class DecoratedWidgetApp:
    def __init__(self, master):
        self.master = master
        master.title("Декоратор GUI")

        # Простая метка
        label1 = SimpleLabel(master, "Обычная метка")
        label1.get_widget().pack(pady=10)
        print(f"1. {label1.get_description()}")

        # Метка с рамкой
        label2 = BorderDecorator(SimpleLabel(master, "Метка с рамкой"), relief="groove")
        label2.get_widget().pack(pady=10)
        print(f"2. {label2.get_description()}")

        # Кликабельная метка с рамкой
        def on_label_click():
            print("Кликабельная метка была нажата!")
            tk.messagebox.showinfo("Клик", "Вы нажали на кликабельную метку!")
        label3 = ClickableDecorator(BorderDecorator(SimpleLabel(master, "Кликабельная метка с рамкой"), border_width=3, relief="ridge"),on_label_click)
        label3.get_widget().pack(pady=10)
        print(f"3. {label3.get_description()}")

root = tk.Tk()
app = DecoratedWidgetApp(root)
root.mainloop()