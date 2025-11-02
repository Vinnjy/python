import sqlite3

with sqlite3.connect('mydatabase.db') as conn:
    cursor = conn.cursor()

    # Удаление записи по условию
    cursor.execute("DELETE FROM users WHERE name=?", ('Bonnie',))
    print(f"Удалено записей: {cursor.rowcount}")

    # Удаление всех продуктов с количеством на складе меньше 30
    cursor.execute("DELETE FROM products WHERE stock_quantity < ?", (30,))

    conn.commit()
    print("Данные успешно удалены.")

    # Проверка оставшихся пользователей
    cursor.execute("SELECT * FROM users")
    print("\nОставшиеся пользователи:")
    for user in cursor.fetchall():
        print(user)

    # Проверка оставшихся продуктов
    cursor.execute("SELECT * FROM products")
    print("\nОставшиеся продукты:")
    for product in cursor.fetchall():
        print(product)
