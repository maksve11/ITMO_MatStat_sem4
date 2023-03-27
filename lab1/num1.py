import numpy as np
from scipy.stats import norm, geom

# Задаем параметры распределения Geom(p)
p = 4/5

# Рассчитываем объем выборки
epsilon = 0.01
delta = 0.05
n = np.ceil((norm.ppf(1 - delta/2)**2 * p * (1-p)) / epsilon**2).astype(int)

# Генерируем 500 выборок и вычисляем выборочное среднее
samples = geom.rvs(p, size=(500, n))
sample_means = np.mean(samples, axis=1)

# Вычисляем математическое ожидание
mu = geom.mean(p)

# Определяем, сколько раз выборочное среднее отличается от математического ожидания на более чем epsilon
count = np.sum(np.abs(sample_means - mu) > epsilon)

# Выводим результат
print("Количество раз, когда выборочное среднее отличается от математического ожидания на более чем", epsilon, ":", count)
