import sqlite3

with sqlite3.connect('mydatabase.db') as conn:
    cursor = conn.cursor()

    # SQL-запрос для создания таблицы users
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL
        )
    ''')

    # SQL-запрос для создания таблицы products(
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products(
            product_id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_name TEXT NOT NULL,
            price REAL NOT NULL,
            stock_quantity INTEGER DEFAULT 0
        )
    ''')

    # Сохранение изменений
    conn.commit()
    print("Таблицы 'users' и 'products' успешно созданы (или уже существовали).")