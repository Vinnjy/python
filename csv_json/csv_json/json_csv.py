import json
import csv

# Создаём контент JSON
json_content = """[ 
    { "name": "Laptop",
        "category": "Electronic",
        "stock": 10
    },
    {
        "name": "Desk",
        "category": "Furniture",
        "stock": 5
    }
]
"""
with open("productss.json", "w", encoding="utf-8") as f:
    f.write(json_content)
with open("productss.json", "r", encoding="utf-8") as json_file:
    data = json.load(json_file)
if data:
    # Получаем заголовки из ключей первого словаря
    fieldnames = list(data[0].keys())
    with open("productss.csv", "w", newline="") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
    print(f"Данные из products.json успешно конвертированы в products.csv.\n")
    with open("productss.csv", "r") as f:
        print(f.read())
else:
    print("JSON-файл пуст или содержит некорректные данные.")