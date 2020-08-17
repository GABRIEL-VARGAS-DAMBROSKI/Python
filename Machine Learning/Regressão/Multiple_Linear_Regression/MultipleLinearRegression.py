# coding: utf-8

# Importando as bibliotecas
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Importando o Dataset

df = pd.read_csv('50_Startups.csv', sep=',')
X = df.iloc[:, :-1].values
y = df.iloc[:, -1].values
df.head()

# Enconding dados categoricos

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [3])],remainder='passthrough')
X = np.array(ct.fit_transform(X))

# Separando o DataSet em TrainSet e TestSet

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=0)

# Treinando o modelo de Regressão Linear Multipla

from sklearn.linear_model import LinearRegression
regressao = LinearRegression()
regressao.fit(X_train, y_train)

# Predição do Modelo

predicao = regressao.predict(X_test)
predicao


# Imprimir a predicao de forma que possamos visualizar melhor em comparação com as Labels de teste

np.set_printoptions(precision=2)
print(np.concatenate((predicao.reshape(len(predicao),1), y_test.reshape(len(y_test),1)),1))