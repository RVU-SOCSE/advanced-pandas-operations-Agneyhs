import pandas as pd

import matplotlib.pyplot as plt

import seaborn as sns

df2 = pd.read_csv(r"C:\Users\RVUW243\Desktop\14prog_5ds_salaries.csv")

sns.heatmap(df2.corr(numeric_only=True),annot=True)
plt.show()
