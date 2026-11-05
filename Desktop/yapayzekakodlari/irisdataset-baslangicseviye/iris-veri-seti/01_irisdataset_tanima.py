# Gerekli kütüphaneleri ekleyelim
from sklearn.datasets import load_iris

# Iris veri setini yükleyelim
iris = load_iris()

# Veri setindeki çiçek türlerini yazdıralım
print(iris.target_names)

# Veri setindeki özellikleri yazdıralım
print(iris.feature_names)

# İlk 5 çiçeğin ölçümlerini gösterelim
print(iris.data[:5])

# İlk 5 çiçeğin türlerini gösterelim
print(iris.target[:5])