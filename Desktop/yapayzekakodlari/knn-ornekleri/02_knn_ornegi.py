# KNN ile Meyve Sınıflandırma

from sklearn.neighbors import KNeighborsClassifier

# Eğitim verileri: Ağırlık (gram), Çap (cm)
X = [
    [150, 7],
    [160, 8],
    [140, 7],
    [200, 9],
    [210, 10],
    [190, 9]
]

# Meyve sınıfları
y = [
    "Elma",
    "Elma",
    "Elma",
    "Portakal",
    "Portakal",
    "Portakal"
]

# KNN modelini oluştur (En yakın 3 komşu)
model = KNeighborsClassifier(n_neighbors=3)

# Modeli eğit
model.fit(X, y)

# Yeni meyvenin özellikleri
yeni_meyve = [[170, 8]]

# Tahmin yap
tahmin = model.predict(yeni_meyve)

# Sonucu ekrana yazdır
print("Tahmin edilen meyve:", tahmin[0])