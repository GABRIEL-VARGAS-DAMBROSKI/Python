# coding: utf-8
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ### A primeira coluna e a segunda são redundantes, logo, vamos utilizar somente a segunda. Pois a coluna numérica é a qualificada para o modelo

df = pd.read_csv('Position_Salaries.csv', sep=',')
X = df.iloc[:, 1:-1].values  #Level
y = df.iloc[:, -1].values #Salary

# Regressão Linear
from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(X, y)

# Fazer a parte polinomial da regressão. Elevando a potência as features
# 1. Elevar essa as features à potencia escolhida (parâmetro)
# 2. Fazer uma regressao das features já pre processadas na potencia

from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree = 4)
X_poly = poly_reg.fit_transform(X)
regressao = LinearRegression()
regressao.fit(X_poly, y)

# Plotando o resultado com a Regressão Linear
plt.scatter(X,y,color='red')
plt.plot(X, lin_reg.predict(X), color='blue')
plt.title('Linear Regression')
plt.xlabel('Level')
plt.ylabel('Salário')
plt.show()

# Plotando agora a regressão Polinomial
plt.scatter(X,y,color='red')
plt.plot(X, regressao.predict(X_poly), color='blue')
plt.title('Polynomial Regression')
plt.xlabel('Level')
plt.ylabel('Salário')
plt.show()