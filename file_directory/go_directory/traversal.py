import os
import shutil

# Функция для обхода директорий
def list_files_recursive(path):
    print(f"Вход в директорию: {path}")
    try:
        for i in os.listdir(path):
            i_path = os.path.join(path, i)
            if os.path.isfile(i_path):
                print(f"  Файл: {i_path}.\n")
            elif os.path.isdir(i_path):
                list_files_recursive(i_path) # Рекурсивный вызов для поддиректорий
    except PermissionError:
        print(f"  Ошибка: Нет прав доступа к директории '{path}'. Пропускаем.\n")
    except Exception as e:
        print(f"  Произошла ошибка при обходе '{path}': {e}.\n")

# Создаём тестовую структуру для обхода
if not os.path.exists("root_folder"):
    os.makedirs("root_folder/folder_a/sub_folder_a")
    os.makedirs("root_folder/folder_b")
    with open("root_folder/file_root.txt", "w") as f:
        f.write("root")
    with open("root_folder/folder_a/file_a.txt", "w") as f:
        f.write("a")
    with open("root_folder/folder_a/sub_folder_a/file_sub_a.txt", "w") as f:
        f.write("sub_a")
    print("Создана тестовая структура директорий для обхода.\n")

print("--- Рекурсивный обход с os.listdir() ---")
list_files_recursive("root_folder")

# Удаляем
if os.path.exists("root_folder"):
    shutil.rmtree("root_folder")
    print("Тестовая структура 'root_folder' удалена.")