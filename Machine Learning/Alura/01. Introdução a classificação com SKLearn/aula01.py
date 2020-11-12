# Features
# pelo longo?
# perna curta?
# faz auau?

porco1 = [0, 1, 0]
porco2 = [0, 1, 1]
porco3 = [1, 1, 0]

cachorro1 = [0, 1, 1]
cachorro2 = [1, 0, 1]
cachorro3 = [1, 1, 1]

# 1 => Porco, 0 => Cachorro
X_train = [porco1, porco2, porco3, cachorro1, cachorro2, cachorro3]
y_train = [1,1,1,0,0,0]

from sklearn.svm import LinearSVC

model = LinearSVC()
model.fit(X_train, y_train)

misterioso1 = [1,1,1]
misterioso2 = [1,1,0]
misterioso3 = [0,1,1]

X_test = [misterioso1, misterioso2, misterioso3]
y_test = [0,1,1]

previsoes = model.predict(X_test)

# Metricas para acurracia feito na mao
corretos = (previsoes == y_test).sum()
total = len(X_test)
taxa_de_acerto = (corretos/total) * 100
print('Taxa de acertos: %.2f%%' % (taxa_de_acerto))

# Metricas pelo Sklearn
from sklearn.metrics import accuracy_score

taxa_de_acerto = accuracy_score(y_test, previsoes)
print('Taxa de acertos: %.2f%%' % (taxa_de_acerto * 100))