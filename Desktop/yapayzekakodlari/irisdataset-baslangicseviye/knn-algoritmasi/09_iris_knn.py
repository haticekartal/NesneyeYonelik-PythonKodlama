# Gerekli kütüphaneler
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

# Iris veri setini yükle
iris = load_iris()

X = iris.data
y = iris.target

# Eğitim ve test verilerini ayır
X_egitim, X_test, y_egitim, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# K değerlerini ve başarı oranlarını tutacak listeler
k_degerleri = []
basari_oranlari = []

# K değerlerini 1'den 20'ye kadar dene
for k in range(1, 21):

    # KNN modelini oluştur
    model = KNeighborsClassifier(n_neighbors=k)

    # Modeli eğit
    model.fit(X_egitim, y_egitim)

    # Test verileriyle tahmin yap
    tahmin = model.predict(X_test)

    # Doğruluk oranını hesapla
    basari = accuracy_score(y_test, tahmin)

    # Sonuçları listelere ekle
    k_degerleri.append(k)
    basari_oranlari.append(basari)

    print("K değeri:", k, "Başarı:", round(basari, 2))

# Doğruluk grafiğini çiz
plt.plot(k_degerleri, basari_oranlari, marker="o")

# Grafik başlığı ve eksen isimleri
plt.title("KNN - K Değerine Göre Model Başarısı")
plt.xlabel("K Değeri")
plt.ylabel("Accuracy (Doğruluk)")

# Y eksenini 0 ile 1 arasında sınırla
plt.ylim(0, 1.05)

# Izgara çizgilerini göster
plt.grid()

# Grafiği göster
plt.show()