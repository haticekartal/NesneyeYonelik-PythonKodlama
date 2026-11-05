"""
Iris veri setini scikit-learn ve pandas ile yükleme ve inceleme

Ders dokümanı: "Yapay Zekâya Giriş – Sınıflandırma ve Iris Veri Seti", Bölüm 5.
Python ile Iris Veri Setini Yükleme ve İnceleme

Çalıştırma: python 03_iris_yukleme_ve_inceleme.py

Gerekli kütüphaneler:
pip install scikit-learn pandas matplotlib seaborn

Not: "# %%" satırları hücre ayıracıdır. VS Code, Spyder ve PyCharm'da
her bölüm ayrı ayrı çalıştırılabilir.
"""

# %% 5.1 scikit-learn kütüphanesi – Kurulum kontrolü

# Gerekli kütüphaneleri programa dahil ediyoruz.
import sklearn
import pandas
import matplotlib
import seaborn

# Kütüphanelerin bilgisayarımızda yüklü olup olmadığını
# ve hangi sürümlerinin kullanıldığını kontrol ediyoruz.
print("scikit-learn:", sklearn.__version__)
print("pandas      :", pandas.__version__)
print("matplotlib  :", matplotlib.__version__)
print("seaborn     :", seaborn.__version__)


# %% 5.2 Iris veri setini yükleme: load_iris()

# scikit-learn içerisinden Iris veri setini yüklememizi
# sağlayan load_iris fonksiyonunu içe aktarıyoruz.
from sklearn.datasets import load_iris

# Iris veri setini yüklüyoruz ve iris değişkenine atıyoruz.
iris = load_iris()

# Veri setinin bütün içeriğini ekrana yazdırıyoruz.
# Ölçümler, sınıf bilgileri ve diğer açıklamalar görüntülenir.
print(iris)


# %% Bunch nesnesinin anahtarları

from sklearn.datasets import load_iris

# Iris veri setini tekrar yüklüyoruz.
iris = load_iris()

# Veri setinin hangi Python nesne türünde olduğunu öğreniyoruz.
print(type(iris))

# Veri setinin içerisinde bulunan anahtarları listeliyoruz.
# Bu anahtarlar sayesinde veri setinin farklı bölümlerine ulaşabiliriz.
print(list(iris.keys()))


# %% 5.3 data, target, feature_names ve target_names

# Çiçeklere ait ölçüm bilgilerini görüntülüyoruz.
# Her satır bir çiçeği, her sütun bir ölçüm özelliğini temsil eder.
print(iris.data)

# Çiçeklerin hangi sınıfa ait olduğunu gösteren sayısal etiketleri görüntülüyoruz.
# 0: Setosa, 1: Versicolor, 2: Virginica
print(iris.target)

# Ölçüm sütunlarının isimlerini görüntülüyoruz.
print(iris.feature_names)

# Sınıf numaralarının karşılık geldiği çiçek türlerinin isimlerini görüntülüyoruz.
print(iris.target_names)


# %% Boyutlar ve tek bir çiçeğe erişim

# Veri setindeki çiçek sayısını ve özellik sayısını gösteriyoruz.
# 150 satır ve 4 sütun bulunur.
print(iris.data.shape)

# Sınıf etiketlerinin boyutunu gösteriyoruz.
# Toplam 150 çiçeğin sınıf bilgisi vardır.
print(iris.target.shape)

# Veri setindeki ilk çiçeğin dört ölçüm değerini görüntülüyoruz.
print(iris.data[0])

# İlk, 51. ve 101. çiçeklerin sınıf numaralarını görüntülüyoruz.
# Her türün veri setinde hangi sırayla bulunduğunu görebiliriz.
print(iris.target[0], iris.target[50], iris.target[100])


# %% Kodları tür adlarına çevirmek

# enumerate() fonksiyonu ile sınıf numaralarını ve tür isimlerini eşleştiriyoruz.
# Böylece 0, 1 ve 2 numaralarının hangi çiçek türünü temsil ettiğini görüyoruz.
for kod, ad in enumerate(iris.target_names):
    print(kod, "->", ad)

# İncelemek istediğimiz çiçeklerin indeks numaralarını belirliyoruz.
ornekler = [0, 56, 147]

# Seçtiğimiz çiçeklerin sınıf numaralarını görüntülüyoruz.
print(iris.target[ornekler])

# Sınıf numaralarını gerçek çiçek isimlerine dönüştürüyoruz.
print(iris.target_names[iris.target[ornekler]])


# %% 5.4 pandas ile veri setini inceleme

# Pandas kütüphanesini pd kısaltmasıyla içe aktarıyoruz.
import pandas as pd

from sklearn.datasets import load_iris

# Iris veri setini yüklüyoruz.
iris = load_iris()

# Iris veri setindeki ölçüm bilgilerini DataFrame yapısına dönüştürüyoruz.
# Sütun isimlerini iris.feature_names içerisinden alıyoruz.
df = pd.DataFrame(
    iris.data,
    columns=iris.feature_names
)

# Çiçeklerin sınıf numaralarını species isimli yeni bir sütuna ekliyoruz.
df["species"] = iris.target

# Oluşturduğumuz tablonun ilk 5 satırını görüntülüyoruz.
print(df.head())


# %% df.info()

# Veri setinin genel yapısı hakkında bilgi veriyoruz.
# Sütun isimleri, dolu değer sayıları ve veri türleri görüntülenir.
print(df.info())


# %% df.describe()

# Sayısal sütunların istatistiksel özetini görüntülüyoruz.
# Ortalama, standart sapma, minimum, maksimum ve çeyrek değerleri hesaplanır.
print(df.describe())


# %% df.shape

# Veri setinin kaç satır ve kaç sütundan oluştuğunu gösteriyoruz.
print(df.shape)


# %% df.isnull().sum()

# Veri setindeki eksik değerleri kontrol ediyoruz.
# isnull() eksik değerleri tespit eder.
# sum() her sütundaki eksik değerleri sayar.
print(df.isnull().sum())


# %% df['species'].value_counts()

# Her çiçek türünden veri setinde kaç tane bulunduğunu sayıyoruz.
# 0: Setosa, 1: Versicolor, 2: Virginica
print(df["species"].value_counts())


# %% Türlere göre ortalama ölçüler

# Çiçekleri species sütunundaki sınıf numaralarına göre gruplandırıyoruz.
# mean() her çiçek türünün ölçüm ortalamalarını hesaplar.
# round(2) sonuçları virgülden sonra iki basamakla gösterir.
print(df.groupby("species").mean().round(2))