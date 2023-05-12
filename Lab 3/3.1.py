import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('./Iris/iris.csv')

# выводим корреляцию для всей таблицы
corr = df.corr(numeric_only=True)
# корреляция по классам
grouped_corr = df.groupby('variety').corr()
print(corr)
print(grouped_corr)

# корелляция 2х категориальных признаков
sepal_corr = df['sepal.length'].corr(df['sepal.width'])
petal_corr = df['petal.length'].corr(df['petal.width'])
print(f'sepal_corr: {sepal_corr}')
print(f'petal_corr: {petal_corr}', '\n')

# между двумя признаками по классам
sepal_class_corr = df.groupby(
    'variety')[['sepal.length', 'sepal.width']].corr().unstack().iloc[:, 1]
petal_class_corr = df.groupby(
    'variety')[['petal.length', 'petal.width']].corr().unstack().iloc[:, 1]
print(sepal_class_corr, '\n')
print(petal_class_corr, '\n')

# добавляем столбец с кодами классов
df['Species_code'] = df.variety.astype('category').cat.codes
ax = df[['sepal.length', 'sepal.width', 'petal.length', 'petal.width']]
codes = df['Species_code']  # коды классов

# s - размер точек, с - цвета в которых закодированы классы, sepal.length- ось х, sepal.width - ось у
sp = plt.subplot(231)  # 2 на 3 с индексом 1
plt.scatter(ax['sepal.length'], ax['sepal.width'], c=codes, s=3)

sp = plt.subplot(232)
plt.scatter(ax['sepal.length'], ax['petal.length'], c=codes, s=3)

sp = plt.subplot(233)
plt.scatter(ax['sepal.length'], ax['petal.width'], c=codes, s=3)

sp = plt.subplot(234)
plt.scatter(ax['sepal.width'], ax['petal.length'], c=codes, s=3)

sp = plt.subplot(235)
plt.scatter(ax['sepal.width'], ax['petal.width'], c=codes, s=3)

sp = plt.subplot(236)
plt.scatter(ax['petal.length'], ax['petal.width'], c=codes, s=3)

plt.show()
