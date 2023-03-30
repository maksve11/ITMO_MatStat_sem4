import numpy as np
from scipy.stats import t

# две выборки объема 25
np.random.seed(42)

n = m = 25
mu1, mu2 = 2, 1
sigma1 = sigma2 = 1

X = np.random.normal(mu1, sigma1, n)
Y = np.random.normal(mu2, sigma2, m)

t_stat = (np.mean(X) - np.mean(Y)) / np.sqrt((np.var(X, ddof=1) / n) + (np.var(Y, ddof=1) / m))
t_quantile = t.ppf(1 - 0.05 / 2, m + n - 2)

CI_low = np.mean(X) - np.mean(Y) - t_quantile * np.sqrt((np.var(X, ddof=1) / n) + (np.var(Y, ddof=1) / m))
CI_high = np.mean(X) - np.mean(Y) + t_quantile * np.sqrt((np.var(X, ddof=1) / n) + (np.var(Y, ddof=1) / m))

print("95% confidence interval for tau:", CI_low, CI_high)


# 1000 выборок объема 25
np.random.seed(42)

n = m = 25
mu1, mu2 = 2, 1
sigma1 = sigma2 = 1

true_tau = mu1 - mu2
CI_count = 0

for i in range(1000):
    X = np.random.normal(mu1, sigma1, n)
    Y = np.random.normal(mu2, sigma2, m)

    t_stat = (np.mean(X) - np.mean(Y)) / np.sqrt((np.var(X, ddof=1) / n) + (np.var(Y, ddof=1) / m))
    t_quantile = t.ppf(1 - 0.05 / 2, m + n - 2)

    CI_low = np.mean(X) - np.mean(Y) - t_quantile * np.sqrt((np.var(X, ddof=1) / n) + (np.var(Y, ddof=1) / m))
    CI_high = np.mean(X) - np.mean(Y) + t_quantile * np.sqrt((np.var(X, ddof=1) / n) + (np.var(Y, ddof=1) / m))

    if CI_low <= true_tau <= CI_high:
        CI_count += 1

print("Coverage probability for n=25:", CI_count / 1000)


# эксперимент для выборок объема 10000
np.random.seed(42)

n = m = 10000
mu1, mu2 = 2, 1
sigma1 = sigma2 = 1

true_tau = mu1 - mu2
CI_count = 0

for i in range(1000):
    X = np.random.normal(mu1, sigma1, n)
    Y = np.random.normal(mu2, sigma2, m)

    t_stat = (np.mean(X) - np.mean(Y)) / np.sqrt((np.var(X, ddof=1) / n) + (np.var(Y, ddof=1) / m))
    t_quantile = t.ppf(1 - 0.05 / 2, m + n - 2)

    CI_low = np.mean(X) - np.mean(Y) - t_quantile * np.sqrt((np.var(X, ddof=1) / n) + (np.var(Y, ddof=1) / m))
    CI_high = np.mean(X) - np.mean(Y) + t_quantile * np.sqrt((np.var(X, ddof=1) / n) + (np.var(Y, ddof=1) / m))

    if CI_low <= true_tau <= CI_high:
        CI_count += 1

print("Coverage probability for n=10000:", CI_count / 1000)
