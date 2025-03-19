import pandas as pd

# Задание 1
print("Разминка")
print(f"\nЗадание 1 Вариант 1")
columns_1 = ['date', 'ticker', 'open', 'high', 'low', 'close', 'volume']
df = pd.read_csv('sp500hst.txt', delimiter=',', names=columns_1)
print(df)
dataframe = pd.DataFrame(df)
print(f"\nЗадание 1 Вариант 2")
print(dataframe)

# Задание 2
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
print(f"\nЗадание 3")
df_3 = pd.read_csv('sp500hst.txt', delimiter=',', names=columns_1)
df_3['date'] = pd.to_datetime(df['date'], format = '%Y%m%d') # преобразование столбца со датой в формат datetime
df_3['day'] = df_3['date'].dt.day # добавляет новый столбец 'day', извлекая день из даты
print(df_3)

# Задание 5
print(f"\nЗадание 5")
df_5 = pd.read_csv('sp500hst.txt', delimiter=',', names=columns_1, parse_dates=['date']) # Парсинг даты сразу  формате datetime
columns_ticker = ['ticker', 'name', 'pro']
df_ticker = pd.read_csv('sp_data2.csv', delimiter=';', names=columns_ticker)
#df_5['ticker'] = df_5['ticker'].str.upper() # к верхней регистре
#df_ticker['ticker'] = df_ticker['ticker'].str.upper()
#df_ticker = df_ticker.drop_duplicates(subset='ticker') # удаление дубликатов
result_df = df_5.merge(df_ticker[['ticker','name', 'pro']].drop_duplicates('ticker'), on='ticker',how='left') # объединение данных, выбор нужных колонок
result_df['name'] = result_df['name'].fillna('Увы...') # замена Nan значений в солбце на написанное
result_df['pro'] = result_df['pro'].fillna('Ля...')
print(result_df)

# Лабороторная работа по pandas
# Задание 1.1
print(f"\nЗадание 1.1")
df_recipes = pd.read_csv('recipes_sample.csv') # read_csv = по умолчанию игнорирует кавычки, как символы обрамления полей (игнорирование запятых внутри)
pd.set_option('display.max_columns', None)
print(f"\nRECIPES")
print(df_recipes.head()) # только первые строки
df_reviews = pd.read_csv('reviews_sample.csv', header=0)
print(f"\nREVIEWS")
print(df_reviews)

# Задание 1.2
print(f"\nЗадание 1.2")
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
print(f"общее количество строк с хотя бы 1 пропуском в рецептах: {dataframe_recipes.isnull().any(axis=1).sum()}")
# общее количество строк с хотя бы 1 пропуском || isnull() = создание булевой маски || any(axis=1) = вернёт True c хотя бы 1 пропуском || sum() = их количество
print(f"общее количество строк с хотя бы 1 пропуском в обзорах: {dataframe_reviews.isnull().any(axis=1).sum()}")
print(f"Соотношение в рецептах: {dataframe_recipes.isnull().any(axis=1).sum()/dataframe_recipes.index.size}")
print(f"Соотношение в обзорах: {dataframe_reviews.isnull().any(axis=1).sum()/dataframe_reviews.index.size}")

# Задание 1.4
print(f"\nЗадание 1.4")
print(f"среднее значение в рецептах по столбцам: id - {dataframe_recipes['id'].mean()}, minutes - {dataframe_recipes['minutes'].mean()}, contributor_id - {dataframe_recipes['contributor_id'].mean()}, n_steps - {dataframe_recipes['n_steps'].mean()}, n_ingredients - {dataframe_recipes['n_ingredients'].mean()}")
print(f"среднее значение в обзорах по столбцам: безымянный столбец - {dataframe_reviews['Unnamed: 0'].mean()}, user_id - {dataframe_reviews['user_id'].mean()}, recipe_id - {dataframe_reviews['recipe_id'].mean()}, rating - {dataframe_reviews['recipe_id'].mean()}")

# Задание 1.5
print(f"\nЗадание 1.5")
print('10 уникальных рецептов')
random_recipes = dataframe_recipes.sample(n=10,random_state=80)
random_recipes_columns = random_recipes['name']
print(random_recipes_columns)

# Задание 1.6
print(f"\nЗадание 1.6")
print("Заголовки с 0, значения в строчках с 1")
df_recipes_1 = pd.read_csv('reviews_sample.csv')
df_recipes_1.index = df_recipes_1.index + 1
print(df_recipes_1)

# Задание 1.7
print(f"\nЗадание 1.7")
filter_dataframe_recipes = dataframe_recipes[(dataframe_recipes['minutes'] < 20) & (dataframe_recipes['n_ingredients'] < 5)]
print(f"Информацию о рецептах, время выполнения которых не больше 20 минут и кол-во ингредиентов в которых не больше 5: {filter_dataframe_recipes}")