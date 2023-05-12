import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv('mushrooms.csv')

# for i in df.columns:
#     raspr = df.groupby('class')[i].value_counts().unstack() # вычисляем кол-во встретившихся значений
#     raspr.plot(kind = 'bar')# делаем стобцовую диаграмму
#     plt.show()
#    df[i] = LabelEncoder().fit_transform(df[i]) # Fit label encoder and return encoded labels.

frequency = df.groupby('cap-color')[['cap-shape', 'class']].value_counts().unstack()
frequency.plot(kind = 'bar')# делаем стобцовую диаграммy
plt.show()
