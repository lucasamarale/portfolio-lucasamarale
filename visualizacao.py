import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report

# Carregar o conjunto de dados Iris
iris = load_iris()
data = pd.DataFrame(data=iris.data, columns=iris.feature_names)
data['species'] = iris.target

# Visualizar a distribuição dos dados
plt.figure(figsize=(8,6))
sns.pairplot(data, hue='species')
plt.title('Distribuição de Dados Iris')
plt.show()

# Dividir o conjunto de dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.3, random_state=42)

# Treinar o modelo KNN
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)

# Fazer previsões
y_pred = knn.predict(X_test)

# Mostrar as métricas de avaliação
print(classification_report(y_test, y_pred))


