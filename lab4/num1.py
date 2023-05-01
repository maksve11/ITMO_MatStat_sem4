import pandas as pd
from scipy.stats import shapiro, kstest, norm
import matplotlib.pyplot as plt
import numpy as np
from statsmodels.graphics.gofplots import qqplot

# Загрузка данных из файла song_data.csv
data = pd.read_csv("song_data.csv", delimiter=",")

# Построение гистограммы распределения популярности песен
plt.hist(data['song_popularity'], bins=20)
plt.xlabel('Популярность')
plt.ylabel('Количество песен')
plt.title('Распределение популярности песен')
plt.show()

# Критерий Колмогорова-Смирнова
kstest_result = kstest(data['song_popularity'], 'norm')

print("Критерий Колмогорова-Смирнова: ")
if kstest_result.pvalue < 0.05:
    print("Распределение популярности песен отличается от нормального закона.")
else:
    print("Распределение популярности песен можно аппроксимировать нормальным законом.")

# Критерий Шапиро-Уилка
shapiro_result = shapiro(data['song_popularity'])

print("\nКритерий Шапиро-Уилка: ")
if shapiro_result.pvalue < 0.05:
    print("Распределение популярности песен отличается от нормального закона.")
else:
    print("Распределение популярности песен можно аппроксимировать нормальным законом.")

# Построение графика Q-Q plot для проверки нормальности распределения
qqplot(data['song_popularity'], line='s')
plt.title('QQ-график популярности песен')
plt.xlabel('Квантили теоретического распределения')
plt.ylabel('Квантили выборки')
plt.show()