import numpy as np
import pandas as pd

# implement your solution here
def get_grouped_mean():
  data = pd.DataFrame(pd.read_csv(url, names=names))
  data = data.drop(columns=["sepallength","petallength","petalwidth"])
  setosa = data.loc[data['species'].isin(['Iris-setosa'])]
  versicolor = data.loc[data['species'].isin(['Iris-versicolor'])]
  virginica = data.loc[data['species'].isin(['Iris-virginica'])]
  return [["Iris-setosa",setosa.mean(numeric_only=True).item()],["Iris-versicolor",versicolor.mean(numeric_only=True).item()],["Iris-virginica",virginica.mean(numeric_only=True).item()]]

names = ('sepallength', 'sepalwidth', 'petallength', 'petalwidth', 'species')
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'


# calculate grouped mean and print
grouped_mean = get_grouped_mean()
for i in grouped_mean:
  print(i)
get_grouped_mean()