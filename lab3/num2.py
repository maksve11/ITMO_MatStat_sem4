import numpy as np
from scipy.stats import norm

# выборки объема 100
np.random.seed(42)

n = 100
theta = 2

X = np.random.uniform(0, theta, n)
X_min = np.min(X)
X_max = np.max(X)
S = np.std(X, ddof=1)

z_quantile = norm.ppf(1 - 0.05 / 2)

CI_low = X_min - z_quantile * S / np.sqrt(n)
CI_high = X_max + z_quantile * S / np.sqrt(n)

print("95% confidence interval for theta:", CI_low, CI_high)


# 1000 выборок объема 100
np.random.seed(42)

n = 100
theta = 2

true_theta = theta
CI_count = 0

for i in range(1000):
    X = np.random.uniform(0, theta, n)
    X_min = np.min(X)
    X_max = np.max(X)
    S = np.std(X, ddof=1)

    z_quantile = norm.ppf(1 - 0.05 / 2)

    CI_low = X_min - z_quantile * S / np.sqrt(n)
    CI_high = X_max + z_quantile * S / np.sqrt(n)

    if CI_low <= true_theta <= CI_high:
        CI_count += 1

print("Coverage probability for n=100:", CI_count / 1000)