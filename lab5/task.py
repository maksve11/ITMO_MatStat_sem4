import pandas as pd
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm

# Загрузка данных из файла
data = pd.read_csv('candy-data.csv', delimiter=',')

# Удаление конфет Chewey Lemonhead Fruit Mix и Kit Kat
data = data[(data['competitorname'] != 'Chewey Lemonhead Fruit Mix') & (data['competitorname'] != 'Kit Kat')]

# Определение предикторов и отклика
predictors = ['chocolate', 'fruity', 'caramel', 'peanutyalmondy', 'nougat', 'crispedricewafer', 'hard', 'bar', 'pluribus', 'sugarpercent', 'pricepercent']
response = 'winpercent'

# Разделение данных на предикторы и отклик
X = data[predictors]
y = data[response]

# Создание и обучение модели линейной многомерной регрессии
model = LinearRegression()
model.fit(X, y)

# Предсказание значения winpercent для конфеты Chewey Lemonhead Fruit Mix
chewey_lemonhead = [[0, 1, 0, 0, 0, 0, 0, 0, 1, 0.73199999, 0.51099998]]
predicted_winpercent = model.predict(chewey_lemonhead)

print("Предсказанное значение winpercent для конфеты Chewey Lemonhead Fruit Mix:", predicted_winpercent[0])

kit_kat = [[1, 0, 0, 0, 0, 1, 0, 1, 0, 0.31299999, 0.51099998]]
predicted_winpercent = model.predict(kit_kat)

print("Предсказанное значение winpercent для конфеты Kit Kat:", predicted_winpercent[0])

candy = [[0, 0, 0, 1, 0, 1, 0, 1, 1, 0.543, 0.402]]
predicted_winpercent = model.predict(candy)
print("Предсказанное значение winpercent для конфеты:", predicted_winpercent[0])

X = sm.add_constant(X)
model = sm.OLS(y, X)
results = model.fit()

print(results.summary())

# Проверка гипотез

# Гипотеза: Чем больше sugarpercent, тем больше winpercent
sugar_coef = results.params['sugarpercent']
sugar_p_value = results.pvalues['sugarpercent']
print("Значимость коэффициента sugarpercent: p =", sugar_p_value)
if sugar_p_value < 0.05:
    print("Гипотеза о влиянии sugarpercent на winpercent подтверждена.")
else:
    print("Нет достаточных доказательств в пользу гипотезы о влиянии sugarpercent на winpercent.")

# Гипотеза: Чем hard меньше, тем больше winpercent
hard_coef = results.params['hard']
hard_p_value = results.pvalues['hard']
print("Значимость коэффициента hard: p =", hard_p_value)
if hard_p_value < 0.05:
    print("Гипотеза о влиянии hard на winpercent подтверждена.")
else:
    print("Нет достаточных доказательств в пользу гипотезы о влиянии hard на winpercent.")

# Гипотеза: Зависимость winpercent от количества chocolate
chocolate_coef = results.params['chocolate']
chocolate_p_value = results.pvalues['chocolate']
print("Значимость коэффициента chocolate: p =", chocolate_p_value)
if chocolate_p_value < 0.05:
    print("Гипотеза о влиянии chocolate на winpercent подтверждена.")
else:
    print("Нет достаточных доказательств в пользу гипотезы о влиянии chocolate на winpercent.")

# Гипотеза: Одновременное влияние chocolate, caramel, nougat на winpercent

hypotheses = '(chocolate = 0), (caramel = 0), (nougat = 0)'
f_test = results.f_test(hypotheses)

print("Значимость теста F-статистики:", f_test.pvalue)
if f_test.pvalue < 0.05:
    print("Гипотеза о влиянии chocolate, caramel, nougat на winpercent подтверждена.")
else:
    print("Нет достаточных доказательств в пользу гипотезы о влиянии chocolate, caramel, nougat на winpercent.")