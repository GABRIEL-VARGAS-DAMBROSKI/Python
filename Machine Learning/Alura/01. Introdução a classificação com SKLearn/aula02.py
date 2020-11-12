import pandas as pd

df = pd.read_csv('acesso.csv', sep=',')

mapa = {
    'home' : 'principal',
    'how_it_works' : 'como_funciona',
    'contact' : 'contato',
    'bought' : 'comprou'
}

df = df.rename(columns = mapa)

X = df[['principal', 'como_funciona', 'contato']]
y = df['comprou']


# ---------------------------------------------- #
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

SEED = 20

# Separacao da base, para treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = SEED, test_size = 0.25, stratify = y)
'''
    LER SOBRE ESTES ARGUMENTOS DO train_test_split() => random_state, stratify
'''
# Treinando o modelo
model = LinearSVC()
model.fit(X_train, y_train)

previsoes = model.predict(X_test)
acuracia = accuracy_score(y_test, previsoes) * 100
print('A acuracia foi %.2f%%' % acuracia)


print('========')