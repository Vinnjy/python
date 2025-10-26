import tkinter as tk
from tkinter import filedialog, messagebox
import abc
import json

# Интерфейс Стратегии: Сохранение данных
class SaveStrategy(abc.ABC):
    @abc.abstractmethod
    def save(self, data: str, filename: str):
        pass
# Конкретные Стратегии: Различные способы сохранения
class TextSaveStrategy(SaveStrategy):
    def save(self, data: str, filename: str):
        try:
            with open(filename, "w", encoding="utf-8") as f:
                f.write(data)
            messagebox.showinfo("Сохранение", f"Данные успешно сохранены в {filename} (TXT).")
        except Exception as e:
            messagebox.showerror("Ошибка сохранения", f"Не удалось сохранить файл: {e}")
class JsonSaveStrategy(SaveStrategy):
    def save(self, data: str, filename: str):
        try:
            # Попытка распарсить данные как JSON, если не удается, сохраняем как строку
            try:
                json_data = json.loads(data)
            except json.JSONDecodeError:
                json_data = {"content": data}
            with open(filename, "w", encoding="utf-8") as f:
                json.dump(json_data, f, indent=4, ensure_ascii=False)
            messagebox.showinfo("Сохранение", f"Данные успешно сохранены в {filename} (JSON).")
        except Exception as e:
            messagebox.showerror("Ошибка сохранения", f"Не удалось сохранить файл: {e}")

# Контекст: Приложение для сохранения текста
class TextEditorApp:
    def __init__(self, master):
        self.master = master
        master.title("Текстовый Редактор со Стратегиями")
        self.text_area = tk.Text(master, height=15, width=60, wrap="word")
        self.text_area.pack(pady=10)
        self.save_strategy = TextSaveStrategy() # Стратегия по умолчанию

        # Кнопки для выбора стратегии сохранения
        strategy_frame = tk.Frame(master)
        strategy_frame.pack(pady=5)
        text_btn = tk.Button(strategy_frame, text="Сохранить как TXT", command=lambda: self.set_save_strategy(TextSaveStrategy()))
        text_btn.pack(side=tk.LEFT, padx=5)
        json_btn = tk.Button(strategy_frame, text="Сохранить как JSON", command=lambda: self.set_save_strategy(JsonSaveStrategy()))
        json_btn.pack(side=tk.LEFT, padx=5)

        # Кнопка сохранения
        save_btn = tk.Button(master, text="Сохранить", command=self.save_content)
        save_btn.pack(pady=10)
    def set_save_strategy(self, strategy: SaveStrategy):
        self.save_strategy = strategy
        messagebox.showinfo("Стратегия", f"Выбрана стратегия сохранения: {strategy.__class__.__name__}")
    def save_content(self):
        content = self.text_area.get("1.0", tk.END).strip()
        if not content:
            messagebox.showwarning("Внимание", "Текстовое поле пусто.")
            return

        # Запрашиваем имя файла у пользователя
        file_path = filedialog.asksaveasfilename(defaultextension=".txt" if isinstance(self.save_strategy, TextSaveStrategy) else ".json", filetypes=[("Text files", "*.txt"), ("JSON files", "*.json"), ("All files", "*.*")])
        if file_path:
            self.save_strategy.save(content, file_path)

root = tk.Tk()
app = TextEditorApp(root)
root.mainloop()
