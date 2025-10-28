print("---Запись в файл (режим 'w')---")
try:
    with open("output.txt", "w", encoding="utf-8") as f:
        f.write("First string.\n")
        f.write("Second string.\n")
        f.write("Third string.\n")
    print("Файл 'output.txt' создан и записан.")
except Exception as e:
    print(f"Произошла ошибка: {e}")
print("---Дозапись файл (режим 'a')---")
try:
    with open("output.txt", "a", encoding="utf-8"):
        f.write("New string append to the end at the line.")
        f.writelines(["Ещё 1 строка.\n", "И ещё 1 строка.\n"])
    print("Данные добавлены в 'output.txt'.")
except Exception as e:
    print(f"Произошла ошибка: {e}")
print("Проверим содержимое")
try:
    with open("output.txt", "r", encoding="utf-8") as f:
        print(f.read())
except FileNotFoundError:
    print("Файл не найден.")
except Exception as e:
    print(f"Произошла ошибка: {e}")