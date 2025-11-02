import sqlite3


def create_table():
    with sqlite3.connect('library.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS books(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                author TEXT NOT NULL,
                year INTEGER,
                isbn TEXT UNIQUE
            )
        ''')
        print("Таблицы 'books' успешно создана.\n")
        conn.commit()


def append_book(title, author, year, isbn):
    try:
        with sqlite3.connect('library.db') as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO books (title, author, year, isbn) VALUES (?, ?, ?, ?)", (title, author, year, isbn))  # Добавление записи
            print(f"Книга: {title}, {author}, {year} успешно добавлена.")
    except sqlite3.IntegrityError as e:
        print(f"Ошибка целостности данных: {e}")
        conn.rollback()


def show_books():
    with sqlite3.connect('library.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM books")  # Выборка
        print("\nВсе книги:")
        for book in cursor.fetchall():
            print(book)


def find_name_year(title, year):
    with sqlite3.connect('library.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM books WHERE title LIKE ? or year LIKE ?", (title, year,))  # Выборка с условием
        print(f"\nКнига: {cursor.fetchone()}")


def update_book(id, year):
    with sqlite3.connect('library.db') as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE books SET year=? WHERE id=?", (year, id))  # Обновление
        print(f"Обновлено записей: {cursor.rowcount}")
        conn.commit()
        cursor.execute("SELECT * FROM books WHERE id=?", (id,))
        print(f"\nОбновленная книга: {cursor.fetchone()}")


def delete_book(id):
    with sqlite3.connect('library.db') as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM books WHERE id=?", (id,))  # Удаление записи
        conn.commit()
        print("\nПроверка оставшихся:")
        cursor.execute("SELECT * FROM books")
        for book in cursor.fetchall():
            print(book)


# Создаём таблицу
create_table()

# Добавляем книги
append_book("Гарри Поттер и философский камень", "Джоан Роулинг", 1997, "978-5-699-35662-1")
append_book("Гарри Поттер и тайная комната", "Джоан Роулинг", 1998, "978-5-699-35663-2")
append_book("Дюна", "Френк Герберт", 1965, "980-5-699-35662-1")
append_book("Хоббит", "Д.Р.Р. Толкин", 1937, "980-5-700-35778-3")

# Пример для исключения
append_book("Дюна 1", "Френк Герберт", 1965, "980-5-699-35662-1")

# Все книги
show_books()

# Ищем по названию или году
find_name_year("Дюна", 1965)

# Обновляем книгу
update_book(1, 1996)

# Удаляем книгу
delete_book(2)
