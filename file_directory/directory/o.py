import os
import shutil

# Получение текущей директории
current_dir = os.getcwd()
print(f"Текущая директория: {current_dir}.\n")

# Создание новой директории
new_dir = "new_directory"
if not os.path.exists(new_dir):
    os.mkdir(new_dir)
    print(f"Новая директория '{new_dir}' создана.\n")
else:
    print(f"Директория '{new_dir}' уже существует.\n")

# Создание вложенных директорий
nested_dir = os.path.join(new_dir, "sub_dir1", "sub_dir2")
if not os.path.exists(nested_dir):
    os.makedirs(nested_dir, exist_ok=True)
    print(f"Вложенные директории '{nested_dir}' созданы.\n")
else:
    print(f"Вложенные директории '{nested_dir}' уже существуют.\n")

# Создание файла внутри директории
file_in_new_dir = os.path.join(new_dir, "test_file.txt")
with open(file_in_new_dir, "w") as f:
    f.write("Это тестовый файл.")
print(f"Новая файл в директории '{file_in_new_dir}' создан.\n")

# Переименуем файл
old_file_name = file_in_new_dir
new_file_name = os.path.join(new_dir, "renamed_file.txt")
os.rename(old_file_name, new_file_name)
print(f"Файл '{old_file_name}' переименован '{new_file_name}'.\n")

# Получение списка содержимого директории
print(f"Содержимое директории '{new_dir}':")
for i in os.listdir(new_dir):
    full_path = os.path.join(new_dir, i)
    if os.path.isfile(full_path):
        print(f"Файл: {i}.")
    elif os.path.isdir(full_path):
        print(f"Директория: {i}.")

# Проверка существование пути
print(f"\nСуществует ли '{new_dir}'? {os.path.exists(new_dir)}.")
print(f"Является ли {new_file_name} файлом? {os.path.isfile(new_file_name)}.")
print(f"Является ли {new_dir} директорией? {os.path.isfile(new_dir)}.\n")

# Удаление файла
os.remove(new_file_name)
print(f"Файл {new_file_name} удалён.\n")

# Удаление пустой директории
os.rmdir(nested_dir)
os.rmdir(os.path.join(new_dir, "sub_dir1"))
print(f"Пустые директории '{nested_dir}' и '{os.path.join(new_dir, "sub_dir1")}' удалены.\n")

# Попытка удалить непустую директорию вызовет => вызовет ошибку shutil.rmtree.
# os.rmdir(new_dir) вызовет OSError, так как папка не пуста.
if not os.path.exists(new_dir):
    shutil.rmtree(new_dir)
    print(f"Удалена {new_dir} и всё её содержимое.")
