file_name = input()
file_name = file_name + ".txt"

try:
    with open(file_name, "r", encoding="utf-8") as f:
        content = f.readlines()
        print(f"Общее количество строк = {len(content)}.")
        result_words = sum([len(i.split()) for i in content])
        print(f"Общее количество слов (считайте слова разделенными пробелами) = {result_words}.")
        result_symbols = sum(len(line) for line in content)
        print(f"Общее количество символов (включая пробелы и символы новой строки) = {result_symbols}.")
except FileNotFoundError:
    print(f"Файл '{file_name}' не найден.")