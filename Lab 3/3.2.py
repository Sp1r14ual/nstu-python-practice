import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder

# df = pd.read_csv(r"C:\Users\Sp1r14ual\Desktop\nstu-python-practice\Lab 3\mushrooms.csv")
df1 = pd.read_csv(
    r"C:\Users\Sp1r14ual\Desktop\nstu-python-practice\Lab 3\primary_data.csv", sep=';')
df2 = pd.read_csv(
    r"C:\Users\Sp1r14ual\Desktop\nstu-python-practice\Lab 3\secondary_data.csv", sep=';')

frequency = df2.groupby(
    'cap-color')[['class']].value_counts().unstack()  # cap-shape
frequency.plot(kind='bar')  # делаем стобцовую диаграммy
plt.show()
