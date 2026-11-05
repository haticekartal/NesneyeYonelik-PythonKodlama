# Gerekli kütüphaneler
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Veri setini yükle
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

# Tahmin yap
tahmin = model.predict(X_test)

# Başarı oranını hesapla
basari = accuracy_score(y_test, tahmin)

print("Model başarı oranı:", basari)

# Yeni bir çiçeğin özelliklerini gir
yeni_cicek = [[5.1, 3.5, 1.4, 0.2]]

# Çiçeğin türünü tahmin et
sonuc = model.predict(yeni_cicek)

print("Tahmin edilen çiçek:", iris.target_names[sonuc[0]])