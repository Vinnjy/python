import json

# Данные для сериализации
data = {
    "name": "Bob",
    "age": 30,
    "is_student": False,
    "courses": ["Math", "Science"]
}

# Сериализация в строку
json_string = json.dumps(data, indent=4)
print(json_string)

# Сериализация в файл
with open("data.json", "w") as f:
    json.dump(data, f, indent=4)

# Десериализация из файла
with open("data.json", "r") as f:
    loaded_data = json.load(f)

print(loaded_data)
