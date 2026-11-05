"""
Iris ile ilk sınıflandırma modeli (karar ağacı)

Ders dokümanı: "Yapay Zekâya Giriş – Sınıflandırma ve Iris Veri Seti", Bölüm 7.
Iris ile İlk Sınıflandırma Modeli

Çalıştırma: python 05_siniflandirma_modeli.py

Gerekli kütüphaneler:
pip install scikit-learn pandas matplotlib seaborn

Not: "# %%" satırları hücre ayıracıdır; VS Code, Spyder ve PyCharm'da
her bölüm ayrı ayrı çalıştırılabilir.
"""

# %% 7.1 Modelin eğitilmesi ve test edilmesi – Karar ağacı ile Iris sınıflandırması

# Iris veri setini yüklemek için gerekli fonksiyonu içe aktarıyoruz.
from sklearn.datasets import load_iris

# Veri setini eğitim ve test olarak ayırmak için kullanıyoruz.
from sklearn.model_selection import train_test_split

# Karar ağacı sınıflandırma algoritmasını içe aktarıyoruz.
from sklearn.tree import DecisionTreeClassifier

# Modelin başarısını ölçmek için gerekli metrikleri içe aktarıyoruz.
from sklearn.metrics import accuracy_score, classification_report

# Iris veri setini yüklüyoruz.
iris = load_iris()

# X değişkenine çiçeklerin ölçüm bilgilerini,
# y değişkenine ise çiçeklerin sınıf numaralarını atıyoruz.
# X: Özellikler (uzunluk ve genişlik ölçümleri)
# y: Hedef değişken (0, 1 veya 2)
X, y = iris.data, iris.target

# Veri setini eğitim ve test olarak ikiye ayırıyoruz.
X_train, X_test, y_train, y_test = train_test_split(
    X,                  # Çiçeklerin ölçüm bilgileri
    y,                  # Çiçeklerin sınıf numaraları
    test_size=0.2,      # Verilerin %20'si test, %80'i eğitim için ayrılır.
    random_state=42,    # Aynı veri bölünmesinin tekrar elde edilmesini sağlar.
    stratify=y          # Her çiçek türünün oranını korur.
)

# Karar ağacı modelini oluşturuyoruz.
model = DecisionTreeClassifier(random_state=42)

# EĞİTİM AŞAMASI
# Model, eğitim verilerindeki ölçümler ile çiçek türleri arasındaki
# ilişkileri öğrenir.
model.fit(X_train, y_train)

# TEST AŞAMASI
# Eğitilmiş modelin daha önce görmediği test verileri için
# çiçek türü tahminleri yapmasını sağlıyoruz.
y_pred = model.predict(X_test)

# Eğitim verileri üzerindeki başarı oranını hesaplıyoruz.
# Modelin öğrendiği verileri ne kadar doğru sınıflandırdığını gösterir.
egitim_basari = accuracy_score(y_train, model.predict(X_train))
print("Eğitim doğruluğu:", egitim_basari)

# Test verileri üzerindeki başarı oranını hesaplıyoruz.
# Modelin daha önce görmediği verilerde ne kadar başarılı olduğunu gösterir.
print("Test doğruluğu  :", round(accuracy_score(y_test, y_pred), 3))

# Precision, Recall, F1-score ve desteklenen örnek sayısı gibi
# sınıflandırma başarı metriklerini ayrıntılı olarak görüntülüyoruz.
# target_names parametresi sayısal sınıf numaralarını çiçek isimleriyle eşleştirir.
print(classification_report(
    y_test,
    y_pred,
    target_names=iris.target_names
))


# %% 7.2 Çok sınıflı karışıklık matrisi – Karışıklık matrisini çizmek

# Grafik oluşturmak için Matplotlib kütüphanesini içe aktarıyoruz.
import matplotlib.pyplot as plt

# Karışıklık matrisini grafik olarak göstermek için
# ConfusionMatrixDisplay sınıfını içe aktarıyoruz.
from sklearn.metrics import ConfusionMatrixDisplay

# Gerçek sınıflar ile modelin tahmin ettiği sınıfları karşılaştıran
# karışıklık matrisini oluşturuyoruz.
ConfusionMatrixDisplay.from_predictions(
    y_test,                         # Gerçek sınıf değerleri
    y_pred,                         # Modelin tahmin ettiği sınıf değerleri
    display_labels=iris.target_names,  # Sınıf numaralarının isimleri
    cmap="Blues"                    # Grafikte kullanılacak renk teması
)

# Grafiğin başlığını belirliyoruz.
plt.title("Karar ağacı – karışıklık matrisi (test verisi)")

# Oluşturulan karışıklık matrisini ekranda gösteriyoruz.
plt.show()


# %% 7.3 Yeni bir çiçeğin türünü tahmin etmek – Yeni bir çiçek için tahmin

# Yeni bir çiçeğe ait dört ölçüm değerini modele veriyoruz.
# Sırasıyla:
# 1. Sepal length (Çanak yaprak uzunluğu): 6.4 cm
# 2. Sepal width (Çanak yaprak genişliği): 3.1 cm
# 3. Petal length (Taç yaprak uzunluğu): 5.5 cm
# 4. Petal width (Taç yaprak genişliği): 1.8 cm

# Çift köşeli parantez kullanılmasının nedeni,
# modelin tek bir örneği bile iki boyutlu veri yapısında beklemesidir.
yeni_cicek = [[6.4, 3.1, 5.5, 1.8]]

# Eğitilmiş karar ağacı modelini kullanarak yeni çiçeğin türünü tahmin ediyoruz.
tahmin = model.predict(yeni_cicek)

# Modelin tahmin ettiği sayısal sınıf kodunu görüntülüyoruz.
print("Tahmin edilen kod:", tahmin)

# Sayısal sınıf kodunu gerçek çiçek türünün ismine dönüştürüyoruz.
# [0] kullanarak tahmin dizisinin ilk elemanını alıyoruz.
print("Tahmin edilen tür:", iris.target_names[tahmin][0])