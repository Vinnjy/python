import json
import csv

try:
    data_top_sum = []
    result_quantity, result_sum = 0, 0
    with open("sales.csv", "r") as csv_file:
        data = csv.DictReader(csv_file)
        for i, row in enumerate(data):
            print(f"Для записи {i+1} товара {row["product_name"]}, выручка составляет {int(row["quantity"]) * int(row["price_per_unit"])}")
            result_quantity = int(row["quantity"]) if i == 0 else max(int(row["quantity"]), result_quantity)
            result_sum = int(row["quantity"]) * int(row["price_per_unit"]) if i == 0 else max(int(row["quantity"]) * int(row["price_per_unit"]), result_sum)
    with open("sales.csv", "r") as csv_file:
        data_n = csv.DictReader(csv_file)
        for i, row in enumerate(data_n):
            if result_sum == int(row["quantity"]) * int(row["price_per_unit"]) or result_quantity == int(row["quantity"]):
                data_top_sum.append(row)
    with open("sales_summary.json", "w", encoding="utf-8") as jsonfile:
        json.dump(data_top_sum, jsonfile, indent=4)
    print(data_top_sum)
except FileNotFoundError:
    print("Добавьте файл для считывания\n")