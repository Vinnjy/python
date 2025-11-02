import sqlite3

with sqlite3.connect('mydatabase.db') as conn:
    cursor = conn.cursor()

    # Обновление записи
    cursor.execute("UPDATE users SET email=? WHERE name=?", ('Alice@doctor.com', 'Alice'))
    print(f"Обновлено записей: {cursor.rowcount}")  # Количество затронутых строк


    # Проверка обновления
    cursor.execute("SELECT * FROM users WHERE name = 'Alice'")
    print("\nОбновленный пользователь Alice:")
    print(cursor.fetchone())

    cursor.execute("SELECT product_name, stock_quantity FROM products WHERE price < 100.00")
    print("\nОбновленные продукты:")
    for product in cursor.fetchall():
        print(product)