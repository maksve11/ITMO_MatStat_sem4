import numpy as np
from matplotlib import pyplot as plt

# Задаем параметры распределения
n = 4
theta = 1/5

# Генерируем выборку размера 50
sample = np.random.binomial(n, theta, size=50)

# Находим оценку параметра методом максимального правдоподобия
theta_hat = np.mean(sample)/n

# Находим смещение, дисперсию и среднеквадратическую ошибку
bias = theta_hat - theta
variance = (theta * (1-theta))/n
mse = variance + bias**2

print("Оценка методом максимального правдоподобия:", theta_hat)
print("Смещение:", bias)
print("Дисперсия:", variance)
print("Среднеквадратическая ошибка:", mse)

delta = 0.01
sample_sizes = [50, 100, 500, 1000, 2500]

# Определяем число экспериментов
n_experiments = 500

# Создаем массивы для хранения результатов
proportions = np.zeros(len(sample_sizes))

for i, sample_size in enumerate(sample_sizes):
    # Создаем массив для хранения отклонений
    deviations = np.zeros(n_experiments)

    for j in range(n_experiments):
        # Генерируем выборку
        sample = np.random.binomial(n, theta, size=sample_size)

        # Находим оценку параметра методом максимального правдоподобия
        theta_hat = np.mean(sample) / n

        # Считаем отклонение от истинного значения параметра
        deviation = abs(theta_hat - theta)

        # Добавляем отклонение в массив
        deviations[j] = deviation

    # Считаем количество выборок с отклонением более, чем на delta
    proportion = (deviations > delta).sum() / n_experiments

    # Записываем результат
    proportions[i] = proportion

# Выводим результаты
for i, sample_size in enumerate(sample_sizes):
    print(f"Доля выборок объема {sample_size}, отклонившихся более чем на {delta}: {proportions[i] * 100:.2f}%")
