import sqlite3

with sqlite3.connect('mydatabase.db') as conn:
    cursor = conn.cursor()

    # Попытка вставить пользователя с уже существующим email (нарушение UNIQUE)
    try:
        cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", ('New User', 'bob@gmail.com'))
        conn.commit()
        print("Пользователь успешно добавлен.")
    except sqlite3.IntegrityError as e:
        print(f"Ошибка целостности данных: {e}")
        conn.rollback() # Откатываем изменения при ошибке

    # Попытка выполнить некорректный SQL-запроc
    try:
        cursor.execute("SELECT * FROM labdulabda")
        conn.commit()
    except sqlite3.OperationalError as e:
        print(f"Операционная ошибка SQL: {e}")
        conn.rollback()

    # Пример общей ошибки sqlite3.Error
    try:
        # Имитация ошибки, например, открыть повреждённую БД (повреждённый файл 'mydatabase.db')
        # Для демонстрации, мы просто вызовем ошибку вручную
        raise sqlite3.Error("Имитация общей ошибки базы данных")
    except sqlite3.Error as e:
        print(f"Общая ошибка SQLite: {e}")
        conn.rollback()