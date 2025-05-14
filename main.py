import pandas as pd
import re

print('Разминка')
print(f"\nЗадание 1\n")
# Вывести на экран данные из словаря obj построчно в виде k = v,
# задав формат таким образом, чтобы знак равенства оказался на одной и той же позиции во всех строках. Строковые литералы обернуть в кавычки.
obj = {
    "home_page": "https://github.com/pypa/sampleproject",
    "keywords": "sample setuptools development",
    "license": "MIT",
}
for key,value in obj.items(): # items() = возвращает всё в виде нескольких кортежей, с его помощью перебираем
    print(f"{key} = '{value}'".format(key=key, value=value))
print(f"\nФорматирование строк")
print(f"\nЗадание 1\n")
recipes = pd.read_csv('recipes_sample.csv')
random_recipes = recipes.sample(5, random_state=0)[['id', 'minutes']] # 5 рандомных рецептов
print("|      id     |  minutes |")
print("|------------------------|")
for _, row in random_recipes.iterrows():
    print(f"|   {row['id']}    |    {row['minutes']}    |")