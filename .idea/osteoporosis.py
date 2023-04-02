# импортируем библиотеку Pandas
import pandas as pd

# вставляем путь к файлу в переменную path
path = r"E:\Data science\Pet_project\Sveta_data\Kniga1.xlsx"

# загрузим файлы excel из таблиц
data_osteoporosis = pd.read_excel(path, sheet_name='Остеопороз лаб')
data_related = pd.read_excel(path, sheet_name='Остео сопут')
data_complaints = pd.read_excel(path, sheet_name='Остео жалобы')
data_fracture = pd.read_excel(path, sheet_name='Остео_перелом')
data_other = pd.read_excel(path, sheet_name='СД_прочие')
data_complaints_2 = pd.read_excel(path, sheet_name='СД_остео_жалобы')

# посмотрим первые пять строк фрейма данных data_osteoporosis
data_osteoporosis.head()

# посмотрим последние пять строк фрейма данных data_osteoporosis
data_osteoporosis.tail()

print(data_osteoporosis.head())

print(data_osteoporosis.tail())


# надо поработать над фичами