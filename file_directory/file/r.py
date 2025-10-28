# 1. Чтение файла

with open("example.txt", "w", encoding="utf-8") as f: # Создадим текстовый файл
    f.write("Первая строка.\n")
    f.write("Вторая строка.\n")
    f.write("Третья строка.\n")
print("---Чтение всего файла = read()---")
try:
    with open("example.txt", "r", encoding="utf-8") as f:
        content = f.read()
        print(content)
except FileNotFoundError:
    print("Файл не найден.")
except Exception as e:
    print(f"Произошла ошибка: {e}")
print("---Чтение файла построчно = readline()---")
try:
    with open("example.txt", "r", encoding="utf-8") as f:
        line1 = f.readline()
        line2 = f.readline()
        print(line1.strip())
        print(line2.strip())
except FileNotFoundError:
    print("Файл не найден.")
except Exception as e:
    print(f"Произошла ошибка: {e}")
print("---Чтение всех строк в список = readlines()---")
try:
    with open("example.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            print(f"Строка {i+1}: {line.strip()}") # удаляет начальные и конечные символы.
except FileNotFoundError:
    print("Файл не найден.")
except Exception as e:
    print(f"Произошла ошибка: {e}")
print("---Итерация по файловому объекту---")
try:
    with open("example.txt", "r", encoding="utf-8") as f:
        for i, line in enumerate(f):
            print(f"Строка {i+1}: {line.strip()}")
except FileNotFoundError:
    print("Файл не найден.")
except Exception as e:
    print(f"Произошла ошибка: {e}")