# Gerekli kütüphaneleri içe aktaralım
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt

# Iris veri setini yükleyelim
iris = load_iris()

X = iris.data
y = iris.target

# Eğitim ve test verilerini ayıralım
X_egitim, X_test, y_egitim, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# KNN modelini oluşturalım ve eğitelim
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_egitim, y_egitim)

# Karar ağacı modelini oluşturalım ve eğitelim
agac = DecisionTreeClassifier(max_depth=2, random_state=42)
agac.fit(X_egitim, y_egitim)

# Tahminleri yapalım
knn_tahmin = knn.predict(X_test)
agac_tahmin = agac.predict(X_test)

# Doğru ve yanlış tahmin sayılarını hesaplayalım
knn_dogru = sum(knn_tahmin == y_test)
knn_yanlis = sum(knn_tahmin != y_test)

agac_dogru = sum(agac_tahmin == y_test)
agac_yanlis = sum(agac_tahmin != y_test)

# Sonuçları ekrana yazdıralım
print("KNN doğru tahmin:", knn_dogru)
print("KNN yanlış tahmin:", knn_yanlis)

print("Karar Ağacı doğru tahmin:", agac_dogru)
print("Karar Ağacı yanlış tahmin:", agac_yanlis)

# Pasta grafiklerini oluşturalım
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.pie(
    [knn_dogru, knn_yanlis],
    labels=["Doğru", "Yanlış"],
    autopct="%1.1f%%"
)
plt.title("KNN Tahmin Sonuçları")

plt.subplot(1, 2, 2)
plt.pie(
    [agac_dogru, agac_yanlis],
    labels=["Doğru", "Yanlış"],
    autopct="%1.1f%%"
)
plt.title("Karar Ağacı Tahmin Sonuçları")

plt.show()