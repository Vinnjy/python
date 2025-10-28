import os

# 1. FileNotFoundError
print("---FileNotFoundError---")
try:
    with open("non_existent_file.txt", "r") as f:
        content = f.read()
        print(content)
except FileNotFoundError:
    print("Ошибка файл 'non_existent_file.txt' не найден.\n")

# 2. FileNotExistsError
print("---FileNotExistsError---")
try:
    os.mkdir("temp_dir")
    os.mkdir("temp_dir") # Попытка создать существующую директорию
except FileExistsError:
    print("Директория 'temp_dir' уже существует.\n")
finally:
    if os.path.exists("temp_dir"):
        os.rmdir("temp_dir") # Удаляем

# 3. PermissionError
print("---PermissionError---")
protected_path = "C:/test.txt"
try:
    with open(protected_path, "w") as f:
        f.write("Тест")
    print(f"Файл создан в защищённой директории: {protected_path}.\n")
except PermissionError:
    print(f"Ошибка: Отказано в доступе для создания файла в '{protected_path}'.\n")
except Exception as e:
    print(f"Произошла другая ошибка: {e}")

# 4. IsADirectoryError/NotADirectoryError
print("---IsADirectoryError/NotADirectoryError---")
# Создаём тестовую директорию и файл
if not os.path.exists("test_dir_for_errors"):
    os.mkdir("test_dir_for_errors")
with open("test_file_for_errors.txt", "w") as f:
    f.write("test")

try:
    with open("test_dir_for_errors", "r") as f: # Попытка открыть директорию как файл
        pass
except IsADirectoryError:
    print("Ошибка: Попытка открыть директорию как файл.")
except PermissionError as e:
    print(f"Исключение срабатывает раньше: {e}.\n")

try:
    os.rmdir("test_file_for_errors") # Попытка удалить файл как директорию
except NotADirectoryError:
    print("Ошибка: Попытка удалить файл как директорию.")
except FileNotFoundError as e:
    print(f"Исключение срабатывает раньше: {e}.\n")
finally:
    if os.path.exists("test_dir_for_errors"):
        os.rmdir("test_dir_for_errors")
    if os.path.exists("test_file_for_errors"):
        os.remove("test_file_for_errors")

# 5. OSError
print("---Обработка OSError---")
try:
    # Попытка удалить несуществующий файл
    os.remove("another_file.txt")
except OSError as e:
    print(f"Произошла ошибка операционной системы: {e}")
    print(f"Код ошибки: {e.errno}")
    print(f"Сообщение об ошибке: {e.strerror}")