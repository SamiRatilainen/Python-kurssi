import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/mpg.csv"
df = pd.read_csv(url)


df = df.dropna()

features = df.select_dtypes(include='number').drop(columns='cylinders').columns.tolist()


sns.pairplot(df, vars=features, hue='cylinders', diag_kind='hist')
plt.tight_layout()


plt.savefig("auto_mpg_pairplot.png")
plt.show()