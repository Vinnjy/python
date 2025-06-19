# 1.
# Датасет: addres-book-q.xml
# По данным из файла addres-book-q.xml сформировать словарь, в котором по должности можно получить список людей с данной должностью и
# для каждого человека по соответствующему ключу можно получить имя, компанию и список всех доступных телефонов.
# Сохранить данную структуру данных в файл формата json и прочитать ее, показав идентичность структуры данных после сохранения/загрузки.
#
# 1
#
import xml.etree.ElementTree as ET
import json

# Чтение XML-файла
tree = ET.parse('addres-book-q.xml')
root = tree.getroot()

# Создание словаря для хранения данных
position_dict = {}

# Обработка данных из XML
for country in root.findall('country'):
    for address in country.findall('address'):
        position = address.find('position').text
        name = address.find('name').text
        company = address.find('company').text
        phones = [phone.text for phone in address.find('phones').findall('phone')]

        person_info = {
            'name': name,
            'company': company,
            'phones': phones
        }

        if position not in position_dict:
            position_dict[position] = []
        position_dict[position].append(person_info)

# Сохранение в JSON-файл
with open('address_book.json', 'w', encoding='utf-8') as f:
    json.dump(position_dict, f, ensure_ascii=False, indent=4)

# Загрузка из JSON-файла для проверки
with open('address_book.json', 'r', encoding='utf-8') as f:
    loaded_data = json.load(f)

# Проверка идентичности данных
print("Идентичность данных после сохранения/загрузки:", position_dict == loaded_data)

#
# 2.Датасет: addres-book-q.xml
# По данным из файла addres-book-q.xml сформировать два списка кортежей.
# В первом будет информация только о мужчинах и кортеж будет состоять из имени, названия компании и рабочего телефона,
# а во втором списке будет только информация о женщинах и кортеж будет состоять из имени и личного телефона.
# Сохранить списки в два разных файла формата pickle и загрузить их оттуда.
#
# 2
#
import pickle

# Парсинг XML-файла
tree2 = ET.parse('addres-book-q.xml')
root2 = tree2.getroot()

# Списки для хранения данных
men_info = []
women_info = []

# Перебор элементов XML
for country in root2.findall('country'):
    for address in country.findall('address'):
        gender = address.find('gender').text
        name = address.find('name').text
        company = address.find('company').text

        # Поиск телефонов
        phones = address.find('phones')
        work_phone = None
        personal_phone = None

        for phone in phones.findall('phone'):
            if phone.get('type') == 'work':
                work_phone = phone.text
            elif phone.get('type') == 'personal':
                personal_phone = phone.text

        # Формирование кортежей
        if gender == 'm':
            men_info.append((name, company, work_phone))
        elif gender == 'f':
            women_info.append((name, personal_phone))

# Сохранение списков в файлы pickle
with open('men_info.pickle', 'wb') as f:
    pickle.dump(men_info, f)

with open('women_info.pickle', 'wb') as f:
    pickle.dump(women_info, f)

# Загрузка списков из файлов pickle
with open('men_info.pickle', 'rb') as f:
    loaded_men_info = pickle.load(f)

with open('women_info.pickle', 'rb') as f:
    loaded_women_info = pickle.load(f)

# Вывод результатов для проверки
print("Информация о мужчинах:", loaded_men_info)
print("Информация о женщинах:", loaded_women_info)

#
# 3.
# Считать файлы addres-book-q, litw-win, countries-of-the-world.
# Вывести результаты считывания в виде массивов Numpy и Pandas.
# Отобразить содержимое массивов данных, построить графики и рассчитать средние значения по столбцам там, где это применимо.
#
# 3
#
import xml.etree.ElementTree as ET
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Считывание XML-файла
tree3 = ET.parse('addres-book-q.xml')
root3 = tree3.getroot()

# Сбор данных
data = []
for country in root3.findall('country'):
    country_name = country.get('name')
    for address in country.findall('address'):
        gender = address.find('gender').text
        name = address.find('name').text
        email = address.find('email').text
        position = address.find('position').text
        company = address.find('company').text
        phones = [phone.text for phone in address.findall('phones/phone')]
        phone_work = phones[0] if len(phones) > 0 else None
        phone_personal = phones[1] if len(phones) > 1 else None

        data.append([country_name, gender, name, email, position, company, phone_work, phone_personal])

# Создание DataFrame Pandas
columns = ['Country', 'Gender', 'Name', 'Email', 'Position', 'Company', 'Phone Work', 'Phone Personal']
df = pd.DataFrame(data, columns=columns)

# Преобразование в массив NumPy
numpy_array = df.to_numpy()

# Отображение данных
print("DataFrame Pandas:")
print(df.head())

print("\nМассив NumPy:")
print(numpy_array[:5])  # Вывод первых 5 строк для примера

# Построение графиков
# Распределение по странам
plt.figure(figsize=(10, 5))
df['Country'].value_counts().plot(kind='bar', color='skyblue')
plt.title('Распределение контактов по странам')
plt.xlabel('Страна')
plt.ylabel('Количество контактов')
plt.show()

# Распределение по полу
plt.figure(figsize=(6, 4))
df['Gender'].value_counts().plot(kind='pie', autopct='%1.1f%%', colors=['lightcoral', 'lightblue'])
plt.title('Распределение контактов по полу')
plt.ylabel('')
plt.show()

# Расчет средних значений (если бы были числовые данные)
# Например, если бы был столбец с возрастом:
# print("\nСредний возраст:", df['Age'].mean())
# В данном примере нет числовых столбцов для расчета средних значений.