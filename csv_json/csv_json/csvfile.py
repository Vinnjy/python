import csv

with open("data.csv", "r", newline="") as f:
    reader = csv.reader(f)
    header = next(reader) # Читаем заголовок
    print(f"Заголовок {header}")
    for row in reader:
        print(row)
print("\n")
with open("data.csv", "r", newline="") as f:
    reader = csv.DictReader(f)
    print(f"Заголовки  столбцов: {reader.fieldnames}")
    for row in reader:
        print(row)
        print(f"Имя: {row["name"]}, Возраст: {row["age"]}")
print("\n")
data_to_write = [["product", "price", "quantity"], ["Laptop", 80000, 10], ["Mouse", 750, 15], ["Keyboard", 900, 23]]
with open("products.csv", "w", newline="") as f:
    writer = csv.writer(f) # Появляется пустой файл
    writer.writerows(data_to_write) # Записываем в файл все строки сразу
with open("products.csv", "r") as f:
    print(f.read())
print("\n")
data_to_write_dict = [{"name": "Tablet", "price": 300, "quantity" : 15}, {"name": "Monitor", "price": 200, "quantity": 16}]
with open("new_products.csv", "w", newline="") as f:
    fieldnames = ["name", "price", "quantity"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader() # Записываем заголовок
    writer.writerows(data_to_write_dict) # Записываем данные