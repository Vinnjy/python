import pandas as pd

#############
# ЗАДАНИЕ №7
#############
#
# Для тикера NVDA подсчитать, сколько дней прошло между максимальным и минимальным значением цены акции на открытии рынка и
# суммарный объем торгов за этот период (включая дни максимума и минимума).
# Решить задачу средствами numpy и/или pandas. Не использовать циклы и конструкции стандартного Python там, где можно использовать возможности данных библиотек.
#
# 7
#
print(f"\nЗадание 7\n")
df7 = pd.read_csv('sp500hst.txt', header=None, names=['date', 'ticker', 'open', 'high', 'low', 'close', 'volume'])

nvda = df7[df7['ticker'] == 'NVDA'].copy()
nvda['date'] = pd.to_datetime(nvda['date'], format='%Y%m%d')

idxMax = nvda['open'].idxmax()
idxMin = nvda['open'].idxmin()

dateMax = nvda.loc[idxMax, 'date']
dateMin = nvda.loc[idxMin, 'date']

dateStart = min(dateMax, dateMin)
dateEnd = max(dateMax, dateMin)

daysBetween = (dateEnd - dateStart).days

period = nvda[(nvda['date'] >= dateStart) & (nvda['date'] <= dateEnd)]

totalVlm = period['volume'].sum()
print("################ ЗАДАНИЕ 7 (1 УР) ################\n")
print(f"Между максимумом ({dateMax.date()}) и минимумом ({dateMin.date()}) прошло {daysBetween} дней (включительно: {daysBetween+1} дней).")
print(f"Суммарный объем торгов за этот период: {totalVlm}")
print("\n\n")

#############
# ЗАДАНИЕ №8
#############
#
# Создать DataFrame в котором присутствует столбец, отражающий разницу в объемах торгов по NVDA и AAPL в одинаковые дни и
# содержит исходные данные об объеме торгов этими акциями и модификацию этого DataFrame в котором сохранены только строки для дней,
# когда и акции NVDA, и акции AAPL дорожали (цена закрытия была выше цены открытия).
# Решить задачу средствами numpy и/или pandas. Не использовать циклы и конструкции стандартного Python там, где можно использовать возможности данных библиотек.
#
# 8
#
print(f"\nЗадание 8\n")
data = pd.read_csv('sp500hst.txt', header=None, names=['date', 'symbol', 'open', 'high', 'low', 'close', 'volume'])
nvdaData = data[data['symbol'] == 'NVDA'][['date', 'volume', 'close', 'open']]
aaplData = data[data['symbol'] == 'AAPL'][['date', 'volume', 'close', 'open']]
# объединяем по дате
mergedData = pd.merge(nvdaData, aaplData, on='date', suffixes=('_nvda', '_aapl'))
mergedData['volumeDifference'] = mergedData['volume_nvda'] - mergedData['volume_aapl']
# модифицируем (оставляем только там, где дорожает)
filteredData = mergedData[(mergedData['close_nvda'] > mergedData['open_nvda']) & (mergedData['close_aapl'] > mergedData['open_aapl'])]
print("################ ЗАДАНИЕ 8 (1 УР) ################\n")
print(filteredData)
print("\n\n")

#############
# ЗАДАНИЕ №9
#############
#
# 9.
# Датасет: titanic.csv
# Заменить все пропущенные числовые значения возраста на значения,
# равные среднему значению для представителей этого класса пассажиров данного пола
# (не выполнять операцию, если неизвестен и возраст, и класс билета пассажира или его пол).
# Решить задачу средствами numpy и/или pandas. Не использовать циклы и конструкции стандартного Python там, где можно использовать возможности данных библиотек
#
# 9
#
print(f"\nЗадание 9\n")
dff = pd.read_csv('Titanic.csv')

# Сохраним маску пропусков возраста
ageNA = dff['Age'].isna()

# Сохраним маску, где известны и Pclass, и Sex (для остальных не заполняем)
hasClassAndSex = dff['Pclass'].notna() & dff['Sex'].notna()

# Группируем по Pclass и Sex и считаем средний возраст по этим группам (игнорируя NaN)
groupMeans = dff.groupby(['Pclass', 'Sex'])['Age'].transform('mean')

# Заполняем только там, где Age пропущен, но Pclass и Sex известны
dff['Age'] = dff['Age'].mask(ageNA & hasClassAndSex, groupMeans)
print("################ ЗАДАНИЕ 9 (1 УР) ################\n")
print(dff.loc[ageNA, ['PassengerId', 'Pclass', 'Sex', 'Age']].head(20)) # тут я вывожу именно те строки, где возраста у пассажиров нет
print("\n\n")
#
#10.
# Датасет: sp_data2.csv, sp500hst.txt
# Сохранить в sp500hst_names.txt CSV с добавленным столбцом с расшифровкой названия тикера.
# Использовать для этого данные из файла sp_data2.csv.
# В случае нехватки данных об именах тикеров корректно обработать такую ситуацию
# (в новом столбце для этих случаев должно быть пустое значение).
# Решить задачу средствами numpy и/или pandas. Не использовать циклы и конструкции стандартного Python там, где можно использовать возможности данных библиотек.
#
#10
#
print(f"\nЗадание 10\n")
names = pd.read_csv('sp_data2.csv',sep=';',header=None)
names=names.drop(2,axis=1)
names.columns=['ticker','name']
# names
df = pd.read_csv('sp500hst.txt', header=None)
df.columns=['date','ticker','open','high','low','close','value']
# df
df_named = df.merge(names, on='ticker',how='left')
#df_named
print(df_named)
df_named.to_csv('sp500hst_names.txt', sep=',',index=False)
#
# 11.
# Датасет: sp500hst.txt
# Рассчитать среднее значение за 2010 год для показателей каждого из столбцов 3-6 для одинаковых значений тикеров из столбца 2 и
# сохранить рассчитанную таблицу со столбцами Тикер, open , high, low, closing
# (где OHLC содержат среднее значение для данного тикера за 2010 год) в новом CSV файле.
# Решить задачу средствами numpy и/или pandas. Не использовать циклы и конструкции стандартного Python там, где можно использовать возможности данных библиотек.
#
# 11
#
print(f"\nЗадание 11\n")
df['year'] = df.date.astype(str).str[:4]
df_mean = df[df['year'] == '2010'].groupby(['ticker']).agg({'open':'mean', 'high':'mean', 'low':'mean','close':'mean'})
# df_mean
print(df_mean)
#
# 12.
# Датасет: sp500hst.txt
# Создать таблицу, в которой индексом являются даты торгов, столбцами - наименования тикеров, а в ячейках хранятся объемы торгов.
# Заполнить эту таблицу данными из sp500hst.txt (в случае отсутствия информации для определенных сочетаний тикер-дата,
# сохранить в ячейке пустое значение). Сохранить результат в новый CSV файл.
# Решить задачу средствами numpy и/или pandas. Не использовать циклы и конструкции стандартного Python там, где можно использовать возможности данных библиотек.
#
# 12
#
print(f"\nЗадание 12\n")
print(df.pivot(columns='ticker',values='value',index='date'))
#
# 13.
# Датасет Titanic.csv
# Загрузить набор данных из датасета с информацией о пассажирах Титаника и посмотреть на первые несколько строк данных,
# чтобы убедиться, что данные загружены корректно.
# Выполнить первичный анализ данных: определить форму датасета с помощью и получить общую информации о колонках.
# Найти все строки, где есть пропущенные значения и удалить их.
# Сгруппировать данные по классу пассажиров на Титанике и рассчитать среднюю сумма билета.
# Выбрать всех пассажиров, которые выжили и были моложе 18 лет, рассчитывать общее количество таких пассажиров.
#
# 13
#
print(f"\nЗадание 13\n")
titanic = pd.read_csv('Titanic.csv')
titanic = titanic.dropna()
print(titanic.shape)
print(titanic.info())
titanic.groupby(['Pclass']).agg({'Fare':'mean'})
print(titanic[(titanic.Survived == 1) & (titanic.Age < 18)].size)
#
# 14.
# Датасет Titanic.csv
# Загрузить набор данных из датасета с информацией о пассажирах Титаника и посмотреть на первые несколько строк данных,
# чтобы убедиться, что данные загружены корректно.
# Выполнить первичный анализ данных: определить форму датасета с помощью и получить общую информации о колонках.
# Найти все строки, где есть пропущенные значения и и заполнить пропуски средним значением для количественных колонок.
# Сгруппировать данные по портам отправления пассажиров и рассчитать средний возраст.
# Выбрать всех пассажиров, которые погибли и были старше 30 лет, рассчитывать общее количество таких пассажиров.
#
# 14
#
print(f"\nЗадание 14\n")
titanic14=titanic.copy()
titanic14.Age = titanic.Age.fillna((titanic['Age'].mean()))
print(titanic14.info())
print(titanic14.groupby(['Embarked']).agg({'Age':'mean'}))
print(titanic14[(titanic14.Survived == 0) & (titanic14.Age > 30)].size)