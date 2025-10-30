import json

data = {"name": "John Doe", "age": 20, "courses": ["History", "Math", "Art"], "address": {"street": "123 Main St", "city": "Washington", "zip": "12345678"}}

# Сериализация в строку JSON
json_string = json.dumps(data, indent=4)
print("Сериализация в строку JSON:")
print(json_string)

# Сериализация в файл JSON
with open("output.json", "w", encoding="utf-8") as json_file:
    json.dump(data, json_file, indent=4)
print(f"\nФайл output.json создан")

# Вывод содержимого
with open("output.json", "r") as f:
    print(f.read())

# JSON-строка для десериализации
json_string_to_load = """
{
    "name": "Kathryn Janeway",
    "age": 40,
    "occupation": "Capitan"
}
"""

# Десериализация из строки
load_data_from_string = json.loads(json_string_to_load)
print(f"\nДесериализация из строки: ")
print(load_data_from_string)
print(f"Имя: {load_data_from_string["name"]}")

# Десериализация из файла
with open("output.json", "r", encoding="utf-8") as json_file:
    load_data_from_file = json.load(json_file)
print(f"\nДесериализация из файла: ")
print(load_data_from_file)
print(f"Курсы: {load_data_from_file["courses"]}")