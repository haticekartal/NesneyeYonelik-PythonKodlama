# Gerekli kütüphaneler
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Iris veri setini yükle
iris = load_iris()

X = iris.data
y = iris.target

# Eğitim ve test verilerini ayır
X_egitim, X_test, y_egitim, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Karar ağacı modelini oluştur
model = DecisionTreeClassifier()

# Modeli eğit
model.fit(X_egitim, y_egitim)

# Modelin başarısını hesapla
tahmin = model.predict(X_test)
basari = accuracy_score(y_test, tahmin)

print("Model başarı oranı:", basari)

# Kullanıcıdan çiçek özelliklerini al
print("\nÇiçek özelliklerini giriniz:")

c1 = float(input("Çanak yaprağı uzunluğu (cm): "))
c2 = float(input("Çanak yaprağı genişliği (cm): "))
c3 = float(input("Taç yaprağı uzunluğu (cm): "))
c4 = float(input("Taç yaprağı genişliği (cm): "))

# Tahmin yap
yeni_cicek = [[c1, c2, c3, c4]]

sonuc = model.predict(yeni_cicek)

# Tahmin sonucunu yazdır
print("\nTahmin edilen çiçek türü:", iris.target_names[sonuc[0]])