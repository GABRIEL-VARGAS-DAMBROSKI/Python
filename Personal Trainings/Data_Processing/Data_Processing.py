# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 09:29:57 2020

@author: Gabriel Vargas Dambroski
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

''' IMPORTING THE DATASET '''
dataset = pd.read_csv('Data.csv')
#iloc => [linha, coluna] -Pegando todas as linhas.
X = dataset.iloc[:, :-1].values     # Colocando todas as linhas e colunas em um Array(.values) X com exceção da útlima coluna
Y = dataset.iloc[:, -1:].values     # Colocando todas as linhas da última coluna em um Array(.values) Y

''' TAKING CARE OF THE MISSING DATA '''
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0)
imputer = imputer.fit(X[:, 1:3])              # fit será a substituição dos campos com 'NaN' para a média da sua coluna
X[:, 1:3] = imputer.transform(X[:, 1:3])      # Adicionando as modificações nas colunas corretas

''' ENCODING THE CATEGORICAL DATA '''
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
# Fazer a codificação da primeira coluna, que já está contida na variável X
labelencoder_X = LabelEncoder()                  # Tornando o objeto do tipo LabelEncoder(EU ACHO)
X[:, 0] = labelencoder_X.fit_transform(X[:, 0])  # Substituíndo a coluna original por códigos
onehotencoder = OneHotEncoder(categorical_features = [0])  # Codificando a coluna sem nível de importância, porque neste caso não precisa
X = onehotencoder.fit_transform(X).toarray()               # jogando os dados de volta na variável, agora todos dados da coluna 0 codificados corretamente

# Fazer a codificação da última coluna, que está contida na variável Y
labelencoder_Y = LabelEncoder()
Y = labelencoder_Y.fit_transform(Y)

''' SPLITTING THE DATASET INTO THE TRAIN SET AND TEST SET '''
