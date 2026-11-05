from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier

iris = load_iris()

X = iris.data
y = iris.target

model = DecisionTreeClassifier()
model.fit(X, y)

# Özellik önemlerini yazdır
for i in range(4):
    print(iris.feature_names[i])
    print(model.feature_importances_[i])