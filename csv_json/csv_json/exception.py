import json

# Некорректная JSON-строка
json_string = "{\"name\": \"Test\", \"age\": 23,"

try:
    data = json.loads(json_string)
    print(data)
except json.JSONDecodeError as e:
    print(f"Ошибка декодирования JSON: {e}")

# Попытка прочитать несуществующий файл
try:
    with open("jknfivnfdn.json", "r") as f:
        data = json.load(f)
except FileNotFoundError:
    print("Файл не найден.")
except json.JSONDecodeError as e:
    print(f"Ошибка декодирования JSON из файла: {e}")