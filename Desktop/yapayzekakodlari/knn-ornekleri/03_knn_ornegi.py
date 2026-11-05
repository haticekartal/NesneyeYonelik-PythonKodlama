# KNN ile Renk Sınıflandırma

from sklearn.neighbors import KNeighborsClassifier

# Eğitim verileri: Parlaklık, Doygunluk
X = [
    [40, 20],
    [50, 50],
    [60, 90],
    [10, 25],
    [70, 70],
    [60, 10],
    [25, 80]
]

# Renk sınıfları
y = [
    "Kırmızı",
    "Mavi",
    "Mavi",
    "Kırmızı",
    "Mavi",
    "Kırmızı",
    "Mavi"
]

# KNN modelini oluştur (K=5)
model = KNeighborsClassifier(n_neighbors=5)

# Modeli eğit
model.fit(X, y)

# Yeni rengin parlaklık ve doygunluk değerleri
yeni_renk = [[20, 35]]

# Tahmin yap
tahmin = model.predict(yeni_renk)

# Sonucu yazdır
print("Yeni rengin sınıfı:", tahmin[0])