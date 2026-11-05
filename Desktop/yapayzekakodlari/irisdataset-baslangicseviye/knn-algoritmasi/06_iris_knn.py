import pandas as pd
import numpy as np

# Iris veri setini yükleyelim
from sklearn.datasets import load_iris

iris = load_iris()

# Özellikleri ve hedef değişkeni alalım
X = iris.data
y = iris.target

# Eğitim ve test verilerini ayıralım
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# İki veri arasındaki Öklid uzaklığını hesaplayan fonksiyon
def uzaklik_hesapla(veri1, veri2):
    toplam = 0

    for i in range(len(veri1)):
        toplam += (veri1[i] - veri2[i]) ** 2

    return np.sqrt(toplam)


# KNN algoritması
def knn_tahmin(X_train, y_train, yeni_veri, k):

    uzakliklar = []

    # Eğitim verilerinin tamamına uzaklığı hesapla
    for i in range(len(X_train)):

        uzaklik = uzaklik_hesapla(X_train[i], yeni_veri)

        uzakliklar.append((uzaklik, y_train[i]))

    # Uzaklıkları küçükten büyüğe sırala
    uzakliklar.sort(key=lambda x: x[0])

    # En yakın K komşuyu seç
    en_yakinlar = uzakliklar[:k]

    # Komşuların sınıflarını say
    siniflar = []

    for komsu in en_yakinlar:
        siniflar.append(komsu[1])

    # En çok tekrar eden sınıfı bul
    tahmin = max(set(siniflar), key=siniflar.count)

    return tahmin


# Bir test verisi üzerinde tahmin yapalım
yeni_veri = X_test[0]

tahmin = knn_tahmin(
    X_train,
    y_train,
    yeni_veri,
    k=5
)

print("Gerçek tür:", iris.target_names[y_test[0]])
print("Tahmin edilen tür:", iris.target_names[tahmin])