import pandas as pd
import matplotlib.pyplot as plt
df =  pd.read_csv('Iris.csv')

corr = df.corr(numeric_only = True)# выводим корреляцию для всей таблицы
grouped_corr = df.groupby('Species').corr() # корреляция по классам
print(corr)
print(grouped_corr)

#корелляция 2х категориальных признаков
sepal_corr = df['SepalLengthCm'].corr(df['SepalWidthCm'])
petal_corr = df['PetalLengthCm'].corr(df['PetalWidthCm'])
print(f'sepal_corr: {sepal_corr}')
print(f'petal_corr: {petal_corr}', '\n')

#между двумя признаками по классам
sepal_class_corr = df.groupby('Species')[['SepalLengthCm', 'SepalWidthCm']].corr().unstack().iloc[:, 1]
petal_class_corr = df.groupby('Species')[['PetalLengthCm', 'PetalWidthCm']].corr().unstack().iloc[:, 1]
print(sepal_class_corr,'\n')
print(petal_class_corr,'\n')

#добавляем столбец с кодами классов
df['Species_code'] = df.Species.astype('category').cat.codes
ax = df[['SepalLengthCm', 'SepalWidthCm','PetalLengthCm', 'PetalWidthCm']]
codes = df['Species_code'] # коды классов

#s - размер точек, с - цвета в которых закодированы классы, SepalLengthCm- ось х, SepalWidthCm - ось у
sp = plt.subplot(231) # 2 на 3 с индексом 1
plt.scatter(ax['SepalLengthCm'], ax['SepalWidthCm'], c = codes, s =3)

sp = plt.subplot (232)
plt.scatter(ax['SepalLengthCm'], ax['PetalLengthCm'], c = codes, s = 3)

sp = plt.subplot(233)
plt.scatter(ax['SepalLengthCm'], ax['PetalWidthCm'], c = codes, s = 3)

sp = plt.subplot (234)
plt.scatter(ax['SepalWidthCm'], ax['PetalLengthCm'], c = codes, s = 3)

sp = plt.subplot(235)
plt.scatter(ax['SepalWidthCm'], ax['PetalWidthCm'], c = codes, s= 3)

sp = plt.subplot (236)
plt.scatter(ax['PetalLengthCm'], ax['PetalWidthCm'], c = codes, s = 3)

plt.show()