import os
import shutil

# Создаём директории и файлы
if not os.path.exists("source_dir"):
    os.makedirs("source_dir/sub_dir")
    with open("source_dir/file1.txt", "w") as f:
        f.write("Содержимое файла 1.\n")
    with open("source_dir/sub_dir/file2.txt", "w") as f:
        f.write("Содержимое файла 2.\n")

# Копирование файлов
shutil.copy("source_dir/file1.txt", "copied_file1.txt")
print("Файл 'source_dir/file1.txt' скопирован в 'copied_file1.txt'.\n")

# Копирование директории
if os.path.exists("destination_dir"):
    shutil.rmtree("destination_dir") # Удаляем, если уже существует
shutil.copytree("source_dir", "destination_dir")
print("Директория 'source_dir' скопирована в 'destination_dir'.\n")

# Перемещение файла
shutil.move("copied_file1.txt", "destination_dir/move_file1.txt")
print("Файл 'copied_file1.txt' перемещен в 'destination_dir/moved_file.txt'.\n")

# Удаляем директорию
if os.path.exists("source_dir"):
    shutil.rmtree("source_dir")
    print("Директория 'source_dir' и ее содержимое удалены.\n")

# Проверка содержимого destination_dir
print("Содержимое 'destination_dir' после операций: ")
for root, dirs, files in os.walk("destination_dir"):
    # Вычисляем вложенность ткущей директории
    level = root.replace("destination_dir", '').count(os.sep) # Заменяет в пути "destination_dir" на '' и подсчитывает разделители / или \
    # Создает отступ для текущей директории
    indent = ' ' * 4 * (level)
    print(f'{indent}{os.path.basename(root)}/')
    # Создает отступ для файлов (на 1 уровень глубже)
    subindent = ' ' * 4 * (level + 1)
    for f in files:
        print(f'{subindent}{f}')

# Удаляем
if os.path.exists("destination_dir"):
    shutil.rmtree("destination_dir")
    print("\nДиректория 'destination_dir' и ее содержимое удалены.")