import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Чтение данных из файла
df = pd.read_csv('D:\MatStat_lab1\sex_bmi_smokers.csv', sep=';', header=1)

# Сравнение количества курящих мужчин и некурящих женщин
smokers = df[df['smoker'] == 'yes']
male_smokers = smokers[smokers['sex'] == 'male']
female_non_smokers = df[(df['smoker'] == 'no') & (df['sex'] == 'female')]

print('Количество курящих мужчин:', len(male_smokers))
print('Количество некурящих женщин:', len(female_non_smokers))

# Расчет статистик для ИМТ
bmi_mean = df['bmi'].mean()
bmi_var = df['bmi'].var()
bmi_median = df['bmi'].median()
bmi_q35 = df['bmi'].quantile(0.6)

male_smokers_bmi = male_smokers['bmi']
male_non_smokers_bmi = df[(df['smoker'] == 'no') & (df['sex'] == 'male')]['bmi']
female_smokers_bmi = smokers[smokers['sex'] == 'female']['bmi']
female_non_smokers_bmi = female_non_smokers['bmi']

# Построение графиков
fig, axs = plt.subplots(2, 2, figsize=(10, 8))
plt.subplots_adjust(hspace=0.5)

# Эмпирическая функция распределения
axs[0, 0].hist(df['bmi'], cumulative=True, density=True, bins=30)
axs[0, 0].set_title('Эмпирическая функция распределения ИМТ')

# Гистограмма ИМТ
axs[0, 1].hist(df['bmi'], density=True, bins=30)
axs[0, 1].set_title('Гистограмма ИМТ')

# Box-plot ИМТ
axs[1, 0].boxplot([male_smokers_bmi, male_non_smokers_bmi, female_smokers_bmi, female_non_smokers_bmi])
axs[1, 0].set_xticklabels(['Курящие мужчины', 'Некурящие мужчины', 'Курящие женщины', 'Некурящие женщины'])
axs[1, 0].set_title('Box-plot ИМТ')

# Графики ИМТ для каждой комбинации пол-курение
axs[1, 1].hist([male_smokers_bmi, male_non_smokers_bmi, female_smokers_bmi, female_non_smokers_bmi], density=True, bins=30, label=['Курящие мужчины', 'Некурящие мужчины', 'Курящие женщины', 'Некурящие женщины'])
axs[1, 1].legend(loc='upper right')
axs[1, 1].set_title('Графики ИМТ для каждой комбинации пол-ку')

# Выборочное среднее, дисперсия, медиана и квантиль порядка 3/5
print("Выборочное среднее:", df["bmi"].mean())
print("Выборочная дисперсия:", df["bmi"].var())
print("Выборочная медиана:", df["bmi"].median())
print("Выборочная квантиль порядка 3/5:", df["bmi"].quantile(3/5))

# Выборочные характеристики по полу и курению
grouped = df.groupby(["sex", "smoker"])["bmi"]
for group, values in grouped:
    print(f"\nГруппа {group}")
    print("Выборочное среднее:", values.mean())
    print("Выборочная дисперсия:", values.var())
    print("Выборочная медиана:", values.median())
    print("Выборочная квантиль порядка 3/5:", values.quantile(3/5))

# График эмпирической функции распределения
plt.figure(figsize=(8, 6))
plt.step(sorted(df["bmi"]), np.arange(len(df))/len(df))
plt.xlabel("ИМТ")
plt.ylabel("Эмпирическая функция распределения")
plt.show()

# Гистограмма ИМТ для всех наблюдателей
plt.figure(figsize=(8, 6))
plt.hist(df["bmi"], bins=20)
plt.xlabel("ИМТ")
plt.ylabel("Частота")
plt.show()

# Box-plot ИМТ для всех наблюдателей
plt.figure(figsize=(8, 6))
plt.boxplot(df["bmi"])
plt.xlabel("Все наблюдатели")
plt.ylabel("ИМТ")
plt.show()