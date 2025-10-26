import tkinter as tk
from tkinter import messagebox
import abc

# Абстрактный класс для уведомлений (Продукт)
class Notification(abc.ABC):
    abc.abstractmethod
    def show(self):
        pass

# Конкретные уведомления (Конкретные продукты)
class InfoNotification(Notification):
    def __init__(self, title, message):
        self.title = title
        self.message=message
    def show(self):
        messagebox.showinfo(self.title, self.message)

class WarningNotification(Notification):
    def __init__(self, title, message):
        self.title = title
        self.message = message
    def show(self):
        messagebox.showwarning(self.title, self.message)

class ErrorNotification(Notification):
    def __init__(self, title, message):
        self.title = title
        self.message = message
    def show(self):
        messagebox.showerror(self.title, self.message)

# Абстрактный класс Фабрики (Фабрика)
class NotificationFactory(abc.ABC):
    @abc.abstractmethod
    def create_notification(self, title, message) -> Notification:
        pass

# Конкретные фабрики
class InfoNotificationFactory(NotificationFactory):
    def create_notification(self, title, message) -> Notification:
        return InfoNotification(title, message)

class WarningNotificationFactory(NotificationFactory):
    def create_notification(self, title, message) -> Notification:
        return WarningNotification(title, message)

class ErrorNotificationFactory(NotificationFactory):
    def create_notification(self, title, message) -> Notification:
        return ErrorNotification(title, message)

class NotificationApp:
    def __init__(self, master):
        self.master = master
        master.title("Фабрика GUI")

        self.factories = {"info":InfoNotificationFactory(), "warning":WarningNotificationFactory(), "error":ErrorNotificationFactory()}

        self.message_entry = tk.Entry(master, width=40)
        self.message_entry.pack(pady=10)
        self.message_entry.insert(0, "Введите сообщение")

        i_btn = tk.Button(master, text="Показать инфо", command=lambda: self.show_notification("info"))
        i_btn.pack(pady=5)
        w_btn = tk.Button(master, text="Показать предупреждение", command=lambda: self.show_notification("warning"))
        w_btn.pack(pady=5)
        e_btn = tk.Button(master, text="Показать ошибку", command=lambda: self.show_notification("error"))
        e_btn.pack(pady=5)

    def show_notification(self, type):
        message = self.message_entry.get()
        if message == "Введите сообщение" or not message:
            message = f"Это {type} сообщение."
        factory = self.factories.get(type)
        if factory:
            notification = factory.create_notification(type.capitalize(), message)
            notification.show()

root = tk.Tk()
app = NotificationApp(root)
root.mainloop()