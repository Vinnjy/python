import json
import os.path
import pickle
import xml.etree.ElementTree as ET
import pandas as pd

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







# Задание 1
# Задание 1.1
print("Задание 1")
print(f"1.1 Считайте файл contributors_sample.json. "
      "Воспользовавшись модулем json, преобразуйте содержимое файла в соответствующие объекты python. "
      "Выведите на экран информацию о первых 3 пользователях.\n")
with open('contributors_sample.json', 'r', encoding='utf-8') as file1:
    contributors_sample = json.load(file1)
for user in contributors_sample[:3]:
    print(user)
print()



# Задание 1.2
print(f"1.2 Выведите уникальные почтовые домены, содержащиеся в почтовых адресах людей\n")
domains = set()
for user in contributors_sample:
    email = user['mail']
    if '@' in email:
        domain = email.split('@')[1] # то, что после @
        domains.add(domain)
print(f"{domains}\n")



# Задание 1.3
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



# Задание 1.4
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



# Задание 1.5
print(f"1.5 Создайте pd.DataFrame contributors, имеющий столбцы id, username и sex.\n")
contributors = pd.DataFrame(contributors_sample)[['id', 'username', 'sex']]
print(contributors)



# Задание 1.6
print("1.6 Загрузите данные из файла recipes_sample.csv (ЛР2) в таблицу recipes. Объедините recipes с таблицей contributors с сохранением строк в том случае, если информация о человеке отсутствует в JSON-файле. Для скольких человек информация отсутствует?\n")
recipes = pd.read_csv('recipes_sample (3).csv')
merged = pd.merge(
    recipes,
    contributors,
    on = 'id',
    how = 'left' # соединение
)
missing_count = merged['username'].isna().sum() # подсчёт строк с отсутствующей информацией о пользователе
print(f"Количество людей с отсутствующей информацией: {missing_count}\n")








# Задание 2
# pickle
# Задание 2.1
print("Задание 1")
print(f"2.1 На основе файла contributors_sample.json создайте словарь следующего вида:\n")
# {
#     должность: [список username людей, занимавших эту должность]
# }
job_people = dict()
for person in contributors_sample:
    positions = person.get('jobs', [])
    username = person.get('username')

    if not username:
        continue
    if isinstance(positions, str):
        positions = [positions]
    # Добавляем username для каждой должности а списке
    for position in positions:
        if position: # игнор пустых строк
            job_people.setdefault(position.strip(), []).append(username) # удаляет лишние проблеы в названии должностей
print(f"Словарь: {job_people}\n")



# Задание 2.2
print("2.2 Сохраните результаты в файл job_people.pickle и в файл job_people.json с использованием форматов pickle и JSON соответственно. Сравните объемы получившихся файлов. При сохранении в JSON укажите аргумент indent\n")
with open('job_people.pickle', 'wb') as file2:
    pickle.dump(job_people, file2) # Сохранение в pickle
with open('job_people.json', 'w', encoding='utf-8') as file22: # Сохранение в JSON
    json.dump(job_people, file22, indent = 4) # запись с 4 пропусками
pickle_size = os.path.getsize('job_people.pickle')
json_size = os.path.getsize('job_people.json')
print(f"Pickle size: {pickle_size}; JSON size: {json_size}")



# Задание 2.3
print(f"2.3 Считайте файл job_people.pickle и продемонстрируйте, что данные считались корректно\n")
with open('job_people.pickle', 'rb') as file23:
    loaded = pickle.load(file23)
assert job_people == loaded, "Не совпали"
print("Данные загружены и идентичны")