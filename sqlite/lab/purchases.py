import sqlite3


def append_purchase(item_name, quantity, price_per_unit):
    with sqlite3.connect('purchases.db') as connection:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO transactions (item_name, quantity, price_per_unit, purchase_date) VALUES (?, ?, ?, CURRENT_TIMESTAMP)", (item_name, quantity, price_per_unit,))
        connection.commit()
        print("Покупка успешно добавлена:")
        cursor.execute("SELECT * FROM transactions WHERE item_name=?", (item_name,))
        print(cursor.fetchone())


def show():
    with sqlite3.connect('purchases.db') as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM transactions")
        print("\nВсе покупки: ")
        for purchase in cursor.fetchall():
            print(purchase)


def costs_purchase():
    with sqlite3.connect('purchases.db') as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT transaction_id, item_name, (quantity*price_per_unit) FROM transactions")
        print("\nCтоимость покупки: ")
        for purchase in cursor.fetchall():
            print(purchase)


def costs_purchases():
    with sqlite3.connect('purchases.db') as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT SUM(quantity*price_per_unit) FROM transactions")
        print(f"\nCтоимость всех покупок: {cursor.fetchone()}")


def find(date):
    with sqlite3.connect('purchases.db') as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM transactions WHERE DATE(purchase_date)=DATE(?)", (date,))
        print("\nНайденные покупки: ")
        for purchase in cursor.fetchall():
            print(purchase)


def delete(id):
    with sqlite3.connect('purchases.db') as connection:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM transactions WHERE transaction_id=?", (id,))
        print(f"\nУдалили покупку.")
        connection.commit()
        print("Оставшиеся покупки:")
        cursor.execute("SELECT * FROM transactions")
        for purchase in cursor.fetchall():
            print(purchase)


# Создаём бд и таблицу
with sqlite3.connect('purchases.db') as conn:
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS transactions(
            transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
            item_name TEXT NOT NULL,
            quantity INTEGER NOT NULL CHECK(quantity > 0),
            price_per_unit REAL NOT NULL CHECK(price_per_unit > 0),
            purchase_date TEXT DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    print("Бд и таблица созданы.\n")
    conn.commit()

# Записываем покупки
append_purchase("notebook", 5, 100000)
append_purchase("laptop", 10, 120000)
append_purchase("mouse", 10, 1000)
append_purchase("earflaps", 10, 5000)

# Показ всех покупок
show()

# Стоимость покупки
costs_purchase()

# Стоимость всех покупок
costs_purchases()

# Показ покупки за определенную дату
print("\n")
find(input())

# Удаляем покупку по id
delete(3)
delete(4)