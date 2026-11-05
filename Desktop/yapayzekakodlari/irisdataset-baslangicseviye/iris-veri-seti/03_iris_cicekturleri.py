import pandas as pd
from sklearn.datasets import load_iris

# Veri setini yükleyelim
iris = load_iris()

# Verileri tabloya dönüştürelim
tablo = pd.DataFrame(iris.data, columns=iris.feature_names)

# Çiçek türlerini tabloya ekleyelim
tablo["Tur"] = iris.target

# İlk 5 satırı gösterelim
print(tablo.head())

# Tablo hakkında bilgi alalım
print(tablo.info())

# Sayısal verilerin ortalamasını bulalım
print(tablo.mean(numeric_only=True))

# Eksik veri var mı kontrol edelim
print(tablo.isnull().sum())