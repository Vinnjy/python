import csv
import json

# Создаём контент для CSV
csv_content = """id,item,price
1,Apple,100
2,Banana,120
3,Orange,130
"""
with open("items.csv", "w", newline="") as f:
    f.write(csv_content)
data=[]
with open("items.csv", "r", newline="") as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        # Преобразуем числовые значения, если необходимо
        row['id'] = int(row['id'])
        row['price'] = int(row['price'])
        data.append(row)
with open("items.json", "w", encoding="utf-8") as json_file:
    json.dump(data, json_file, indent=4)
print(f"Данные из items.csv успешно конвертированы в json.csv.")
with open("items.json", "r") as f:
    print(f.read())