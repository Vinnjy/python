import sqlite3

with sqlite3.connect('mydatabase.db') as conn:
    cursor = conn.cursor()

    # Вставка 1 записи
    cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", ('Alice', 'alice@doctor.com'))

    # Вставка нескольких записей с помощью executemany()
    users_data = [('Bob', 'bob@gmail.com'), ('Charlie', 'charlie@gmail.com'), ('Bonnie', 'bonnie@mail.ru')]
    cursor.executemany("INSERT INTO users (name, email) VALUES (?, ?)", users_data)

    # Вставка данных в таблицу товаров
    products_data = [
        ('Laptop', 1200.00, 10),
        ('Mouse', 25.50, 50),
        ('Keyboard', 75.00, 30)
    ]
    cursor.executemany("INSERT INTO products (product_name, price, stock_quantity) VALUES(?, ?, ?)", products_data)
    conn.commit()
    print("Данные успешно вставлены в таблицы 'users' и 'products'.")
