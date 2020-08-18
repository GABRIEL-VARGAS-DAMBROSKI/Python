# coding: utf-8

import pandas as pd

df = pd.read_csv('diabetes.csv', sep=',')
df.head()

df.info()

mapa = {
    'Pregnancies' : 'Gravidez',
    'Glucose' : 'Glicose',
    'BloodPressure' : 'PressaoSanguinea',
    'SkinThickness' : 'EspessuraDaPele', 
    'Insulin' : 'Insulina',
    'BMI' : 'IMC',
    'DiabetesPedigreeFunction' : 'FuncaoDePedigreeDoDiabetes',
    'Age' : 'Idade',
    'Outcome' : 'Resultado'
}

df = df.rename(columns = mapa)
df.head()

X = df.iloc[:,:-1]
y = df.iloc[:, -1]
X.head()

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

SEED = 20

model = LinearRegression()
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = SEED, test_size = 0.25, stratify = y)

model.fit(X_train, y_train)

resultado = model.predict(X_test)

from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

acuracia = accuracy_score(y_test, resultado.round())*100
print('Acuracia >> ', acuracia)

VN, FP, FN, VP = confusion_matrix(y_test, resultado.round()).ravel()
print('\nVerdadeiro Positivo >>', VP)
print('Falso Positivo >>', FP)
print('Verdadeiro Negativo >>', VN)
print('Falso Negativo >>', FN)

print(classification_report(y_test, resultado.round()))

# Adicionar o plot "The Lifecycle of a Plot". mostrando a comparação de acuracia entre os tipos diferentes de modelo
# https://matplotlib.org/3.3.0/tutorials/introductory/lifecycle.html#sphx-glr-tutorials-introductory-lifecycle-py