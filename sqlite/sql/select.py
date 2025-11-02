import sqlite3

with sqlite3.connect('mydatabase.db') as conn:
    cursor = conn.cursor()

    # Выборка всех записей
    cursor.execute("SELECT * FROM users")
    all_users = cursor.fetchall() # Получить все строки
    print("\nВсе пользователи:")
    for user in all_users:
        print(user)

    # Выборка записей с условием WHERE
    cursor.execute("SELECT name, email FROM users WHERE id > ?", (2,))
    selected_users = cursor.fetchall()
    print("\nПользователи с ID > 2:")
    for user in all_users:
        print(user)

    # Выборка 1 записи
    cursor.execute("SELECT * FROM users WHERE name LIKE ?", ('Alice',))
    alice = cursor.fetchone() # Получить 1 строку
    print("\nПользователь Alice:")
    print(alice)

    # Выборка данных из таблицы products
    cursor.execute("SELECT product_name, price FROM products WHERE price < ?", (100.00,))
    cheap_products = cursor.fetchall()
    print("\nПродукты дешевле 100.00:")
    for product in cheap_products:
        print(product)

    # Итерация по результатам запроса (более эффективно для больших наборов данных)
    print("\nВсе продукты (итерация по курсору):")
    for row in cursor.execute("SELECT product_name, stock_quantity FROM products"):
        print(row)
