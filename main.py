import json
import requests
import pandas as pd
#from bs4 import BeautifulSoup
print(f"Разминка\n")
print(f"1. Вывести все адреса электронной почты, содержащиеся в адресной книге addres-book.json\n")
with open('addres-book.json', 'r', encoding='utf-8') as file:
    reading = json.load(file) # открываем файл на чтение
for i in reading:
    print(i['email'])
print()
print(f"2. Вывести телефоны, содержащиеся в адресной книге addres-book.json\n")
for i in reading:
    print(i['phones'])
print()
#print(f"По данным из файла addres-book-q.xml сформировать список словарей с телефонами каждого из людей.\n")

print(f"1.1 Считайте файл contributors_sample.json. "
      "Воспользовавшись модулем json, преобразуйте содержимое файла в соответствующие объекты python. "
      "Выведите на экран информацию о первых 3 пользователях.\n")
with open('contributors_sample.json', 'r', encoding='utf-8') as file1:
    contributors_sample = json.load(file1)
for user in contributors_sample[:3]:
    print(user)
print()
print(f"1.2 Выведите уникальные почтовые домены, содержащиеся в почтовых адресах людей\n")
domains = set()
for user in contributors_sample:
    email = user['mail']
    if '@' in email:
        domain = email.split('@')[1] # то, что после @
        domains.add(domain)
print(f"{domains}\n")
print(f"1.3 Напишите функцию, которая по username ищет человека и выводит информацию о нем. "
      f"Если пользователь с заданным username отсутствует, возбудите исключение ValueError\n")
def find_user(username, sample):
    for user in sample:
        if user['username'] == username: # по полю username ищем
            return user
    return ValueError("Пользовтаеля нет")
try:
    print(find_user('jean_winchester', contributors_sample))
    print(find_user('ljohnson', contributors_sample))
    print()
except ValueError as e:
    print(e)
print(f"1.4 Посчитайте, сколько мужчин и женщин присутсвует в этом наборе данных.\n")
male_count = 0
female_count = 0

for user in contributors_sample:
    if user['sex'] == 'F':
        female_count += 1
    elif user['sex'] == 'M':
        male_count += 1
    else:
        continue
print(f"Men {male_count}")
print(f"Women {female_count}\n")
print(f"1.5 Создайте pd.DataFrame contributors, имеющий столбцы id, username и sex.\n")
contributors = pd.DataFrame(contributors_sample)[['id', 'username', 'sex']]
print(contributors)
print(f"1.6 Загрузите данные из файла recipes_sample.csv (ЛР2) в таблицу recipes. "
      f"Объедините recipes с таблицей contributors с сохранением строк в том случае, если информация о человеке отсутствует в JSON-файле. "
      f"Для скольких человек информация отсутствует?\n")
recipes = pd.read_csv('recipes_sample (3).csv')

merged = pd.merge(
    recipes,
    contributors,
    left_on
)