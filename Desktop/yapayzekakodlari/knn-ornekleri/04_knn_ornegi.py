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

# KNN modelini oluştur
model = KNeighborsClassifier(n_neighbors=5)

# Modeli eğit
model.fit(X, y)

# Kullanıcıdan değerleri al
parlaklik = int(input("Parlaklık değerini girin: "))
doygunluk = int(input("Doygunluk değerini girin: "))

# Tahmin yapılacak veri
yeni_renk = [[parlaklik, doygunluk]]

# Tahmin yap
tahmin = model.predict(yeni_renk)

# Sonucu yazdır
print("Tahmin edilen renk:", tahmin[0])