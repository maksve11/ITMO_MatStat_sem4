import pandas as pd
import scipy.stats as stats

# Загрузка данных
data = pd.read_csv("song_data.csv", delimiter=',')

# Задаем порог продолжительности для разбиения песен на две категории
duration_threshold = 180000 # 3 минуты в милисекундах

# Создаем две выборки: длинные и короткие песни
long_songs = data[data["song_duration_ms"] >= duration_threshold]["song_popularity"]
short_songs = data[data["song_duration_ms"] < duration_threshold]["song_popularity"]

# Проверка гипотезы с помощью t-критерия Стьюдента
t_stat, p_value = stats.ttest_ind(long_songs, short_songs, equal_var=False)
print("t-критерий Стьюдента:")
print("t-statistic =", t_stat)
print("p-value =", p_value)
if p_value < 0.05:
    print("Различие в распределении рейтинга для длинных и коротких песен статистически значимо.")
else:
    print("Различие в распределении рейтинга для длинных и коротких песен статистически незначимо.")

# Проверка гипотезы с помощью U-критерия Манна-Уитни
u_stat, p_value = stats.mannwhitneyu(long_songs, short_songs, alternative="two-sided")
print("\nU-критерий Манна-Уитни:")
print("U-statistic =", u_stat)
print("p-value =", p_value)
if p_value < 0.05:
    print("Различие в распределении рейтинга для длинных и коротких песен статистически значимо.")
else:
    print("Различие в распределении рейтинга для длинных и коротких песен статистически незначимо.")
