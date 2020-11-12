import pandas as pd

df = pd.read_csv('projetos.csv', sep=',')

df_renomear = {
    'unfinished' : 'nao_finalizado',
    'expected_hours' : 'horas_esperadas',
    'price' : 'preco'
}

df = df.rename(columns = df_renomear)

troca = {
    1 : 0,
    0 : 1
}

df['finalizado'] = df.nao_finalizado.map(troca)

import seaborn as sns

sns.scatterplot(x='horas_esperadas', y='preco', data=df)
sns.scatterplot(x='horas_esperadas', y='preco', hue='finalizado', data=df)

from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

SEED = 20

X = df[['horas_esperadas', 'preco']]
y = df['finalizado']

X_train, X_test, y_train, y_test = train_test_split( X, y, 
                                                     random_state = SEED,
                                                     test_size = 0.25,
                                                     stratify = y)


model = LinearSVC()
model.fit(X_train, y_train)

previsoes = model.predict(X_test)
acuracia = accuracy_score(y_test, previsoes) * 100

print('Acertou: %.2f%%' % acuracia) 





















print('===============')