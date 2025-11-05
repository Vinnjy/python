import numpy as np

# Задание 1
#####################################################################################################################################
print("Задание 1")
with open("minutes_n_ingredients.csv") as file_name:
    # dtype = втоматически определить тип данных # delimiter = указывает на разделитель в файле # names = True = позволяет использовать 1-ую строку, как  имена столбцов.
    array = np.genfromtxt(file_name, delimiter=",", dtype = None, names = True) 

print(f"Строка 1: {array[0]}, Строка 2: {array[1]}, Строка 3: {array[2]}, Строка 4: {array[3]}, Строка 5: {array[4]} \n")

# Задание 2
#####################################################################################################################################
print("Задание 2")

# с.з.
means_two = np.mean(array['minutes'])
means_three = np.mean(array['n_ingredients'])
print(f"Столбец минут: {means_two}. Столбец ингридиентов: {means_three}")

# m..
min_two = np.min(array['minutes'])
min_three = np.min(array['n_ingredients'])
print(f"Столбец минут минка: {min_two}. Столбец ингридиентов минка: {min_two}")

# median
median_two = np.median(array['minutes'])
median_three = np.median(array['n_ingredients'])
print(f"Столбец минут медианка: {median_two}. Столбец ингридиентов медианка: {median_two}")

# max
max_two = np.max(array['minutes'])
max_three = np.max(array['n_ingredients'])
print(f"Столбец минут максималка: {max_two}. Столбец ингридиентов максималка: {max_two} \n")

# Задание 3
#####################################################################################################################################
print("Задание 3")
quantiles = np.quantile(array['minutes'], 0.75)
print(quantiles)

# Задание 4
#####################################################################################################################################
print("Задание 4")
with open('minutes_n_ingredients.csv')  as file_name:
    arr = np.genfromtxt(file_name, delimiter=",", skip_header=1, dtype = None)

column_index = 1
result = arr[:, 1] == 0 # проверка
arr[result, 1] = 1 # запись, где 0 ставим 1
print(arr[:,1])

# Задание 5 ?????
#####################################################################################################################################
print("Задание 5")
column_index = array['id']
values, counts = np.unique(column_index, return_counts = True) # возвращает 2 массива, уникальных значений, количество вхождений
print(values)
print(counts)

# Задание 6
#####################################################################################################################################
print("Задание 6")
column_index = array['n_ingredients']
values, counts = np.unique(column_index, return_counts = True) # возвращает 2 массива, уникальных значений, количество вхождений
print(values)
print(counts)

# Задание 7
#####################################################################################################################################
print("Задание 7")
with open('minutes_n_ingredients.csv')  as file_name:
    arr = np.genfromtxt(file_name, delimiter=",", skip_header=1, dtype = None)
column_index = 2
column = arr[:, column_index] # выбирает соответствующий столбец
mask = column <= 5 # создание булевой маски для значений < 5
result = column[mask] # применение маски к столбцу

print(result)

# Задание 8
#####################################################################################################################################
print("Задание 8")
column_index_minutes = array['minutes']
column_index_ingredients = array['n_ingredients']
result = column_index_minutes/column_index_ingredients

print(f"Скольлко ингрeдиентов на 1 минуту: {result}")
max_result = np.max(result)
print(f"MAX: {max_result}")

# Задание 9
#####################################################################################################################################
print("Задание 9")
sorted_arr = np.mean(arr[arr[:, 1].argsort()[::-1][:100]][:, 2])
print(sorted_arr)

# Задание 10
#####################################################################################################################################
print("Задание 10")
with open('minutes_n_ingredients.csv') as file_name:
    arr = np.genfromtxt(file_name, delimiter=",", skip_header=1, dtype=None)

with open('minutes_n_ingredients.csv', 'r', encoding='utf-8') as file_name:
    headers = file_name.readline().strip()

nums_rows = arr.shape[0] # возвращает количество строк в датасете
random_indicies = np.random.choice(nums_rows, size=10,replace=False) # 10 уникальных индексов; replace=False = не повторяться
random_rows = arr[random_indicies] # выбор строк по случайным индексам
print(random_rows)

# Задание 11
#####################################################################################################################################
print("Задание 11")
means_three = np.mean(array['n_ingredients'])

column_index = 2 # столбец
column = arr[:, column_index] # выбирает соответствующий столбец
mask = column < means_three # создание булевой маски для значений < means_three
result = column[mask] # применение маски к столбцу

print(f"с.з.: {means_three}")
print(f"Столбец по условию: {result}")

values, counts = np.unique(result, return_counts = True) # возвращает 2 массива, уникальных значений, количество вхождений
print(f"Уникальных значений{values}")
print(f"Количество вхождений{counts}")

# Задание 12
#####################################################################################################################################
print("Задание 12")
with open('minutes_n_ingredients.csv') as file_name:
    arr = np.genfromtxt(file_name, delimiter=",", skip_header=1, dtype=None) # dtype = данные интерпретируются, как ....

with open('minutes_n_ingredients.csv', 'r', encoding='utf-8') as file_name:
    headers = file_name.readline().strip()

filter_arr = arr[(arr[:, 1] < 20) & (arr[:, 2] < 5)]
print(filter_arr)
np.savetxt('filter_12.csv', filter_arr, delimiter=',', fmt='%s', header = headers, comments='')
#####################################################################################################################################
print("Задание 12.1")
with open('minutes_n_ingredients.csv') as file_name:
    arr = np.genfromtxt(file_name, delimiter=",", skip_header=1, dtype=None) # dtype = данные интерпретируются, как ....

with open('minutes_n_ingredients.csv', 'r', encoding='utf-8') as file_name:
    headers = file_name.readline().strip()

filter_arr = np.where((arr[:, 1] < 20) & (arr[:, 2] < 5), 1, 0) # создаём новый столбец
data = np.column_stack((arr, filter_arr))
np.savetxt('filter_12_12.csv', data, delimiter=',', fmt='%s', header = 'id,minutes,n_ingredients,simple', comments='')
print(data)
# Задание 13
#####################################################################################################################################
print("Задание 13")
with open('filter_12_12.csv') as file_name:
    data_13 = np.genfromtxt(file_name, delimiter=",", skip_header=1, dtype=None) # dtype = данные интерпретируются, как ....

filter_data = data_13[(data_13[:, 1] < 20) & (data_13[:, 2] < 5)]
print(filter_data)
# Задание 14
#####################################################################################################################################
filename='minutes_n_ingredients.csv'
massive = np.genfromtxt(filename, delimiter=',', skip_header=1, dtype=int)

duration = massive[:,1]
short = massive[duration<10] # группы
middle = massive[(duration>=10) & (duration<20)]
long = massive[duration >= 20]

min_recipes = min(len(short), len(middle), len(long)) # определ... мин количество рецептов в каждой группе
short = short[:min_recipes] # огр. количество рецептов до мин... в каждой группе
middle = middle[:min_recipes]
long = long[:min_recipes]

result_massive = np.array([short, middle, long]) # создаём 3-мерный массив (Ось 1 - группы; 2 - рецепты; 3 - характеристики рецепта
print("Форма 3-мерного массива: ", result_massive.shape)
