import os
import shutil

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

print("\n--- Обход с os.walk() ---")

for root, dirs, files in os.walk("root_folder"):
    # root = current directory
    # dirs = list of names subdirectories in root
    # files = list of names files in root
    level = root.replace("root_folder", '').count(os.sep)  # Уровень вложенности для отступа
    indent = ' ' * 4 * (level)

    print(f'{indent}[{os.path.basename(root)}/]')  # Выводим текущую директорию
    subindent = ' ' * 4 * (level + 1)
    for d in dirs:
        print(f'{subindent}: {d}')  # Выводим поддиректории
    for f in files:
        print(f'{subindent}F: {f}')  # Выводим файлы

# Удаляем
if os.path.exists("root_folder"):
    shutil.rmtree("root_folder")
    print("Тестовая структура 'root_folder' удалена.")