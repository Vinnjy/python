import pandas as pd

# Задание 1
print("Разминка")
print(f"\nЗадание 1\nЗагрузите данные из файла sp500hst.txt и обозначьте столбцы в соответствии с содержимым: date, ticker, open, high, .., close, volume")
print(f"\nЗадание 1 Вариант 1")
columns_1 = ['date', 'ticker', 'open', 'high', 'low', 'close', 'volume']
df = pd.read_csv('sp500hst.txt', delimiter=',', names=columns_1)
print(df)
dataframe = pd.DataFrame(df)
print(f"\nЗадание 1 Вариант 2")
print(dataframe)

# Задание 2
print(f"\nЗадание 2\nРассчитайте среднее значение показателей для каждого из столбцов c номерами 3-6.")
print(f"\nЗадание 2 Вариант 1")
avg_3 = dataframe['open'].mean()
avg_4 = dataframe['high'].mean()
avg_5 = dataframe['low'].mean()
avg_6 = dataframe['close'].mean()
print(f"Среднее значения по столбцам: 3 - {avg_3} 4 - {avg_4} 5 - {avg_5} 6 - {avg_6}")
df_1 = pd.read_csv('sp500hst.txt', delimiter=',', header=None)
avg_3_1 = df_1[2].mean()
avg_4_1 = df_1[3].mean()
avg_5_1 = df_1[4].mean()
avg_6_1 = df_1[5].mean()
print(f"\nЗадание 2 Вариант 2")
print(f"Среднее значения по столбцам: 3 - {avg_3_1} 4 - {avg_4_1} 5 - {avg_5_1} 6 - {avg_6_1}")

# Задание 3
print(f"\nЗадание 3\nДобавьте столбец, содержащий только число месяца, к которому относится дата")
df_3 = pd.read_csv('sp500hst.txt', delimiter=',', names=columns_1)
df_3['date'] = pd.to_datetime(df['date'], format = '%Y%m%d') # преобразование столбца со датой в формат datetime
df_3['day'] = df_3['date'].dt.day # добавляет новый столбец 'day', извлекая день из даты
print(df_3)

# Задание 5
print(f"\nЗадание 5\nЗагрузите данные из файла sp500hst.txt и обозначьте столбцы в соответствии с содержимым. Добавьте столбец с расшифровкой названия тикера, используя данные из файла sp_data2.csv . В случае нехватки данных об именах тикеров корректно обработать их")
df_5 = pd.read_csv('sp500hst.txt', delimiter=',', names=columns_1, parse_dates=['date']) # Парсинг даты сразу  формате datetime
columns_ticker = ['ticker', 'name', 'pro']
df_ticker = pd.read_csv('sp_data2.csv', delimiter=';', names=columns_ticker)
result_df = df_5.merge(df_ticker[['ticker','name', 'pro']].drop_duplicates('ticker'), on='ticker',how='left') # объединение данных, выбор нужных колонок
result_df['name'] = result_df['name'].fillna('Увы...') # замена Nan значений в солбце на написанное
result_df['pro'] = result_df['pro'].fillna('Ля...')
print(result_df)














# Лабороторная работа по pandas
# Задание 1
# Базовые операции с DataFrame
# Задание 1.1
print(f"\nЗадание 1.1")
print(f"1 В файлах recipes_sample.csv и reviews_sample.csv находится информация об рецептах блюд и отзывах на эти рецепты соответственно. Загрузите данные из файлов в виде pd.DataFrame с названиями recipes и reviews. Обратите внимание на корректное считывание столбца с индексами в таблице reviews (безымянный столбец).\n")
df_recipes = pd.read_csv('recipes_sample.csv') # read_csv = по умолчанию игнорирует кавычки, как символы обрамления полей (игнорирование запятых внутри)
pd.set_option('display.max_columns', None)
print(f"\nRECIPES")
print(df_recipes.head()) # только первые строки
df_reviews = pd.read_csv('reviews_sample.csv', header=0)
print(f"\nREVIEWS")
print(df_reviews)

# Задание 1.2
print(f"\nЗадание 1.2")
print(f" Для каждой из таблиц выведите основные параметры: количество точек данных (строк); количество столбцов; тип данных каждого столбца\n")
dataframe_recipes = pd.DataFrame(df_recipes)
dataframe_reviews = pd.DataFrame(df_reviews)
rows_recipes, columns_recipes = dataframe_recipes.shape # shape = возвращает кортеж (количество строк, количество столбцов)
# Вариант 1
print(f"\nВариант через 'dtype' с использованием датафрейм:")
print(f"Количество строк рецепты: {rows_recipes}")
print(f"Количество столбцов рецепты: {columns_recipes}")
rows_reviews, columns_reviews = dataframe_reviews.shape
print(f"Количество строк обзоров: {rows_reviews}")
print(f"Количество столбцов обзоров: {columns_reviews}")
# Вариант 2
print(f"\nВариант через 'len()' с использованием датафрейм:")
print(f"Количество строк рецепты: {len(dataframe_recipes)}")
print(f"Количество столбцов рецепты: {len(dataframe_recipes.columns)}")
print(f"Количество строк обзоров: {len(dataframe_reviews)}")
print(f"Количество столбцов обзоров: {len(dataframe_reviews.columns)}")
# Вариант 3
print(f"\nВариант через атрибуты 'index, columns' с использованием датафрейм:")
print(f"Количество строк рецепты: {dataframe_recipes.index.size}")
print(f"Количество столбцов рецепты: {dataframe_recipes.columns.size}")
print(f"Количество строк обзоров: {dataframe_reviews.index.size}")
print(f"Количество столбцов обзоров: {dataframe_reviews.columns.size}")
# Вариант 4
print(f"\nВариант через 'info()' с использованием датафрейм:")
print(f"{dataframe_recipes.info()}\n")
print(dataframe_reviews.info())
# Вариант 5
print(f"\nВариант через 'dtype' с использованием датафрейм:")
print(f"{dataframe_recipes.dtypes}\n")
print(dataframe_reviews.dtypes)

# Задание 1.3
print(f"\nЗадание 1.3")
print(f"Исследуйте, в каких столбцах таблиц содержатся пропуски. Посчитайте долю строк, содержащих пропуски, в отношении к общему количеству строк.\n")
print(f"общее количество строк с хотя бы 1 пропуском в рецептах: {dataframe_recipes.isnull().any(axis=1).sum()}")
# общее количество строк с хотя бы 1 пропуском || isnull() = создание булевой маски || any(axis=1) = вернёт True c хотя бы 1 пропуском || sum() = их количество
print(f"общее количество строк с хотя бы 1 пропуском в обзорах: {dataframe_reviews.isnull().any(axis=1).sum()}")
print(f"Соотношение в рецептах: {dataframe_recipes.isnull().any(axis=1).sum()/dataframe_recipes.index.size}")
print(f"Соотношение в обзорах: {dataframe_reviews.isnull().any(axis=1).sum()/dataframe_reviews.index.size}")

# Задание 1.4
print(f"\nЗадание 1.4")
print(f"Рассчитайте среднее значение для каждого из числовых столбцов (где это имеет смысл).\n")
print(f"среднее значение в рецептах по столбцам: id - {dataframe_recipes['id'].mean()}, minutes - {dataframe_recipes['minutes'].mean()}, contributor_id - {dataframe_recipes['contributor_id'].mean()}, n_steps - {dataframe_recipes['n_steps'].mean()}, n_ingredients - {dataframe_recipes['n_ingredients'].mean()}")
print(f"среднее значение в обзорах по столбцам: безымянный столбец - {dataframe_reviews['Unnamed: 0'].mean()}, user_id - {dataframe_reviews['user_id'].mean()}, recipe_id - {dataframe_reviews['recipe_id'].mean()}, rating - {dataframe_reviews['recipe_id'].mean()}")

# Задание 1.5
print(f"\nЗадание 1.5")
print(f"10 уникальных рецептов\n")
random_recipes = dataframe_recipes.sample(n=10,random_state=80)
random_recipes_columns = random_recipes['name']
print(random_recipes_columns)

# Задание 1.6
print(f"\nЗадание 1.6")
print(f"Измените индекс в таблице reviews, пронумеровав строки, начиная с нуля. Заголовки с 0, значения в строчках с 1\n")
df_recipes_1 = pd.read_csv('reviews_sample.csv')
df_recipes_1.index = df_recipes_1.index + 1
print(df_recipes_1)

# Задание 1.7
print(f"\nЗадание 1.7")
print(f"Выведите информацию о рецептах, время выполнения которых не больше 20 минут и кол-во ингредиентов в которых не больше 5\n")
filter_dataframe_recipes = dataframe_recipes[(dataframe_recipes['minutes'] < 20) & (dataframe_recipes['n_ingredients'] < 5)]
print(f"Информацию о рецептах, время выполнения которых не больше 20 минут и кол-во ингредиентов в которых не больше 5: {filter_dataframe_recipes}")








# Задание 2
# Работа с датами в pandas
# Задание 2.1
print(f"\nЗадание 2.1")
print(f"1 Преобразуйте столбец submitted из таблицы recipes в формат времени. Модифицируйте решение задачи 1.1 так, чтобы считать столбец сразу в нужном формате.\n")
dataframe_recipes['submitted'] = pd.to_datetime(dataframe_recipes['submitted'], format = '%Y-%m-%d')
print(f"Форматирование типа \n{dataframe_recipes.dtypes}")

# Задание 2.2
print(f"\nЗадание 2.2")
print(f"Выведите информацию о рецептах, добавленных в датасет не позже 2010 года.\n")
dataframe_recipes['year'] = dataframe_recipes['submitted'].dt.year
filter_dataframe_recipes_2 = dataframe_recipes[dataframe_recipes['year']>2010]
print(f">2010\n{filter_dataframe_recipes_2}")







# Задание 3
# Работа со строковыми данными в pandas
# Задание 3.1
print(f"\nЗадание 3.1")
print(f"Добавьте в таблицу recipes столбец description_length, в котором хранится длина описания рецепта из столбца description.\n")
df_recipes['description_length'] = df_recipes['description'].str.len()
print(f"Вывод дополнительного столбца в recipes для \n{df_recipes}\n")

# Задание 3.2
print(f"\nЗадание 3.2")
print(f"Измените название каждого рецепта в таблице recipes таким образом, чтобы каждое слово в названии начиналось с прописной буквы.\n")
df_recipes['name'] = df_recipes['name'].str.title()
print(f"Вывод дополнительного столбца в recipes \n{df_recipes}\n")

# Задание 3.3
print(f"\nЗадание 3.3")
print(f"Добавьте в т. recipes столбец name_word_count, в ко-ом хранится кол-во слов из названии рецепта (слова в названии разделяются только пробелами). Обратите внимание, что между словами может располагаться несколько пробелов подряд.\n")
df_recipes['name_word_count'] = df_recipes['name'].str.split().str.len()
print(f"Вывод дополнительного столбца name_word_count в recipes \n{df_recipes}\n")
# df_recipes['name_word_count'] = df_recipes['name'].str.split('\s+').apply(len) # с учётом нескольких пробелов
# print(f"Вывод дополнительного столбца name_word_count в recipes \n{df_recipes}\n")







# Задание 4
# Группировки таблиц pd.DataFrame
# Задание 4.1
print(f"\nЗадание 4.1")
print(f"Посчитайте количество рецептов, представленных каждым из участников (contributor_id). Какой участник добавил максимальное кол-во рецептов?\n")
count_recipes = df_recipes.groupby('contributor_id').size()
max_contributor = count_recipes.max()
print(f"количество рецептов {count_recipes} и MAX {max_contributor}\n")

# Задание 4.2
print(f"\nЗадание 4.2")
print(f"Посчитайте средний рейтинг к каждому из рецептов. Для скольких рецептов отсутствуют отзывы? Обратите внимание, что отзыв с нулевым рейтингом или не заполненным текстовым описанием не считается отсутствующим.\n")
avg_rating = df_reviews.groupby('recipe_id')['rating'].mean() # ср. рейтинг для каждого рецепта
print(f"Ср. рейтинг {avg_rating}\n")
num_n_reviews = len(df_recipes[~df_recipes['id'].isin(df_reviews['recipe_id'])])
print(f"Рецепты без отзывов {num_n_reviews}\n")


# Задание 4.3
print(f"\nЗадание 4.3")
print(f"Количество рецептов с разбивкой по годам создания.\n")
df_recipes['year'] = pd.to_datetime(df_recipes['submitted']).dt.year
recipes_year = df_recipes.groupby('year').size()
print(recipes_year)






# Задание 5
# Объединение таблиц pd.DataFrame
# Задание 5.1
print(f"\nЗадание 5.1")
print(f"При помощи объединения таблиц, создайте DataFrame, состоящий из четырех столбцов: id, name, user_id, rating. Рецепты, на которые не оставлен ни один отзыв, должны отсутствовать в полученной таблице. Подтвердите правильность работы вашего кода, выбрав рецепт, не имеющий отзывов, и попытавшись найти строку, соответствующую этому рецепту, в полученном DataFrame\n")
merged = dataframe_recipes.merge(dataframe_reviews, left_on='id', right_on='recipe_id', how = 'inner')
merged_5_1 = merged[['id', 'name', 'user_id', 'rating']]
print(merged_5_1)

# Задание 5.2
print(f"\nЗадание 5.2")
print(f"При помощи объединения таблиц и группировок, создайте DataFrame, состоящий из трех столбцов: recipe_id, name, review_count, где столбец review_count содержит кол-во отзывов, оставленных на рецепт recipe_id. У рецептов, на которые не оставлен ни один отзыв, в столбце review_count должен быть указан 0. Подтвердите правильность работы вашего кода, выбрав рецепт, не имеющий отзывов, и найдя строку, соответствующую этому рецепту, в полученном DataFrame\n")
reviews_count = dataframe_reviews.groupby('recipe_id').size().reset_index(name='review_count')
merged_5_2 = dataframe_recipes.merge(reviews_count, left_on='id', right_on='recipe_id', how='left')
merged_5_2['review_count'] = merged_5_2['review_count'].fillna(0)
merged_5_2 = merged_5_2[['id', 'name', 'review_count']].rename(columns={'id': 'recipe_id'})
print(merged_5_2)

# Задание 5.3
print(f"\nЗадание 5.3")
print(f"Выясните, рецепты, добавленные в каком году, имеют наименьший средний рейтинг?\n")
merged['year'] = pd.to_datetime(merged['submitted']).dt.year
avg_rating_yearly = merged.groupby('year')['rating'].mean()
m = avg_rating_yearly.idxmin()
print(m)









# Задание 6
# Сохранение таблиц pd.DataFrame
# Задание 6.1
print(f"\nЗадание 6")
print(f"\nЗадание 6.1")
print("Отсортируйте таблицу в порядке убывания величины столбца name_word_count и сохраните результаты выполнения заданий 3.1-3.3 в csv файл\n")
sorted_recipes = df_recipes.sort_values('name_word_count', ascending=False) # asceding = порядок сортировки
sorted_recipes.to_csv('recipe_sample_new.csv', index = False)