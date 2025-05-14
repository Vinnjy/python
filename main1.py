import numpy as np
import pandas as pd
import xml.etree.ElementTree as ET

# задача 6
print(f"Задание 6\n")
# Определим границы прямоугольника
x_min, x_max = 0, 5
y_min, y_max = 0, 5
# Создадим сетку точек
n_points = 1000  # Количество точек по каждой оси (для точности)
x = np.linspace(x_min, x_max, n_points)
y = np.linspace(y_min, y_max, n_points)
X, Y = np.meshgrid(x, y)
# Вычислим значение функции в каждой точке
Z = X * Y * np.sin(X) * np.cos(Y)
# Найдем точки, где значение функции больше 0.25
mask = Z > 0.25
# Вычислим долю площади, где функция > 0.25
area_ratio = np.mean(mask)
# Вычислим площадь всего прямоугольника
total_area = (x_max - x_min) * (y_max - y_min)
# Вычислим площадь, где функция > 0.25
target_area = area_ratio * total_area
print(f"Доля площади, где z(x,y) > 0.25: {area_ratio:.4f} или {area_ratio*100:.2f}%")
print(f"Площадь, где z(x,y) > 0.25: {target_area:.4f} из {total_area}")

# Задание 8
print(f"\nЗадание 8\n")
# Загрузка данных из файла
data = pd.read_csv('sp500hst.txt', header=None, names=['Date', 'Ticker', 'Open', 'High', 'Low', 'Close', 'Volume'])
# Фильтрация данных для NVDA и AAPL
nvda_data = data[data['Ticker'] == 'NVDA'].copy()
aapl_data = data[data['Ticker'] == 'AAPL'].copy()
# Преобразование столбца Date в datetime для корректного объединения
nvda_data['Date'] = pd.to_datetime(nvda_data['Date'], format='%Y%m%d')
aapl_data['Date'] = pd.to_datetime(aapl_data['Date'], format='%Y%m%d')
# Объединение данных по дате
merged_data = pd.merge(nvda_data, aapl_data, on='Date', suffixes=('_NVDA', '_AAPL'))
# Расчет разницы в объемах торгов
merged_data['Volume_Difference'] = merged_data['Volume_NVDA'] - merged_data['Volume_AAPL']
# Создание DataFrame с требуемыми столбцами
result_df = merged_data[['Date', 'Volume_NVDA', 'Volume_AAPL', 'Volume_Difference']].copy()
# Фильтрация дней, когда обе акции дорожали (цена закрытия > цены открытия)
filtered_df = merged_data[
    (merged_data['Close_NVDA'] > merged_data['Open_NVDA']) &
    (merged_data['Close_AAPL'] > merged_data['Open_AAPL'])
][['Date', 'Volume_NVDA', 'Volume_AAPL', 'Volume_Difference']].copy()
# Вывод результатов
print("Исходный DataFrame с разницей объемов:")
print(result_df.head())
print("\nОтфильтрованный DataFrame (дни роста обеих акций):")
print(filtered_df.head())

# Задание 10
print(f"\nЗадание 10\n")
columns_1 = ['date', 'ticker', 'open', 'high', 'low', 'close', 'volume']
df_5 = pd.read_csv('sp500hst.txt', delimiter=',', names=columns_1, parse_dates=['date']) # Парсинг даты сразу  формате datetime
columns_ticker = ['ticker', 'name', 'pro']
df_ticker = pd.read_csv('sp_data2.csv', delimiter=';', names=columns_ticker)
result = df_5.merge(df_ticker[['ticker','name', 'pro']].drop_duplicates('ticker'), on='ticker',how='left') # объединение данных, выбор нужных колонок
result.to_csv('sp500hst_names_with_decoded.txt', index=False)

# Задание 1
print(f"\nЗадание 1\n")
# Парсинг XML-файла
tree = ET.parse('addres-book-q.xml')
root = tree.getroot()
# Создание списка для хранения данных
data = []
# Обход структуры XML
for country in root.findall('country'):
    country_name = country.get('name')
    for address in country.findall('address'):
        address_id = address.get('id')
        gender = address.find('gender').text
        name = address.find('name').text
        email = address.find('email').text
        position = address.find('position').text
        company = address.find('company').text

        # Обработка телефонов (может быть несколько)
        phones = address.find('phones')
        work_phone = None
        personal_phone = None
        for phone in phones.findall('phone'):
            if phone.get('type') == 'work':
                work_phone = phone.text
            elif phone.get('type') == 'personal':
                personal_phone = phone.text

        # Добавление записи в список
        data.append({
            'Country': country_name,
            'Address ID': address_id,
            'Gender': gender,
            'Name': name,
            'Email': email,
            'Position': position,
            'Company': company,
            'Work Phone': work_phone,
            'Personal Phone': personal_phone
        })
# Создание DataFrame
df = pd.DataFrame(data)
# Сохранение в CSV (если нужно)
df.to_csv('address_book_processed.csv', index=False)
# Вывод первых строк для проверки
print(df.head())