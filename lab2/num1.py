import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
n = 1000
theta = 10
X = np.random.uniform(low=-theta, high=theta, size=n)
theta_hat = np.sqrt(3 * np.mean(X**2))
bias = -theta / np.sqrt(n)
variance = (2 / n) * theta**2
mse = (3 / n) * theta**2

print("Оценка методом моментов:", theta_hat)
print("Смещение оценки:", bias)
print("Дисперсия оценки:", variance)
print("Среднеквадратическая ошибка:", mse)


def generate_samples(n, theta):
    np.random.seed(42)
    samples = np.random.uniform(low=-theta, high=theta, size=(500, n))
    estimates = np.sqrt(3 * np.mean(samples**2, axis=1))
    deviations = np.abs(estimates - theta)
    return np.sum(deviations > 0.01)


theta = 10
sample_sizes = [50, 100, 500, 1000, 2500]

deviations = []
for n in sample_sizes:
    deviation = generate_samples(n, theta)
    deviations.append(deviation)
    print(f"Объем выборки: {n}, Смещение: {deviation}")

plt.plot(sample_sizes, deviations, 'bo-')
plt.xlabel('Объем выборки')
plt.ylabel('номер смещения > 0.01')
plt.show()