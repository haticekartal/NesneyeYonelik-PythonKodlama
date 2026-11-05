# Gerekli kütüphaneleri içe aktaralım
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

# Iris veri setini yükleyelim
iris = load_iris()

# Verileri X ve y değişkenlerine aktaralım
X = iris.data
y = iris.target

# Verileri eğitim ve test olarak ayıralım
X_egitim, X_test, y_egitim, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# -------------------------------
# KNN ALGORİTMASI
# -------------------------------

# KNN modelini oluşturalım
knn_model = KNeighborsClassifier(n_neighbors=3)

# Modeli eğitelim
knn_model.fit(X_egitim, y_egitim)

# Tahmin yapalım
knn_tahmin = knn_model.predict(X_test)

# Başarı oranını hesaplayalım
knn_basari = accuracy_score(y_test, knn_tahmin)


# -------------------------------
# KARAR AĞACI ALGORİTMASI
# -------------------------------

# Karar ağacı modelini oluşturalım
karar_agaci = DecisionTreeClassifier(max_depth=2, random_state=42)

# Modeli eğitelim
karar_agaci.fit(X_egitim, y_egitim)

# Tahmin yapalım
agac_tahmin = karar_agaci.predict(X_test)

# Başarı oranını hesaplayalım
agac_basari = accuracy_score(y_test, agac_tahmin)


# -------------------------------
# SONUÇLARI EKRANA YAZDIRALIM
# -------------------------------

print("KNN Başarı Oranı:", round(knn_basari * 100, 2), "%")
print("Karar Ağacı Başarı Oranı:", round(agac_basari * 100, 2), "%")


# -------------------------------
# GRAFİK OLUŞTURALIM
# -------------------------------

algoritmalar = ["KNN", "Karar Ağacı"]
basari_oranlari = [knn_basari * 100, agac_basari * 100]

plt.bar(algoritmalar, basari_oranlari)

plt.title("KNN ve Karar Ağacı Başarı Karşılaştırması")
plt.xlabel("Algoritmalar")
plt.ylabel("Başarı Oranı (%)")

plt.ylim(0, 100)
plt.grid(axis="y")

plt.show()