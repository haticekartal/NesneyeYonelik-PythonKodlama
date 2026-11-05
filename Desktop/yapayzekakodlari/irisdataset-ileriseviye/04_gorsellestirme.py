"""
Iris veri setinin görselleştirilmesi (matplotlib ve seaborn)

Ders dokümanı: "Yapay Zekâya Giriş – Sınıflandırma ve Iris Veri Seti", Bölüm 6.
Iris Veri Setinin Görselleştirilmesi

Çalıştırma: python 04_gorsellestirme.py

Gerekli kütüphaneler:
pip install scikit-learn pandas matplotlib seaborn

Not: "# %%" satırları hücre ayıracıdır; VS Code, Spyder ve PyCharm'da
her bölüm ayrı ayrı çalıştırılabilir.
"""

# %% 6.1 Hazırlık kodu – Grafikler için ortak hazırlık

# Veri analizi ve tablo işlemleri için Pandas kütüphanesini içe aktarıyoruz.
import pandas as pd

# Grafik oluşturmak ve düzenlemek için Matplotlib kütüphanesini içe aktarıyoruz.
import matplotlib.pyplot as plt

# Daha gelişmiş ve görsel açıdan düzenli grafikler oluşturmak için
# Seaborn kütüphanesini içe aktarıyoruz.
import seaborn as sns

# scikit-learn içerisinden Iris veri setini yüklemek için
# load_iris fonksiyonunu içe aktarıyoruz.
from sklearn.datasets import load_iris

# Iris veri setini yüklüyoruz.
iris = load_iris()

# Çiçeklerin ölçüm bilgilerini Pandas DataFrame yapısına dönüştürüyoruz.
# Sütun isimlerini Iris veri setindeki özellik isimlerinden alıyoruz.
df = pd.DataFrame(iris.data, columns=iris.feature_names)

# Çiçeklerin sınıf numaralarını species isimli yeni bir sütuna ekliyoruz.
df["species"] = iris.target

# Sayısal sınıf numaralarını çiçek türlerinin isimlerine dönüştürüyoruz.
# 0: Setosa, 1: Versicolor, 2: Virginica
df["tur"] = df["species"].map({
    0: "setosa",
    1: "versicolor",
    2: "virginica"
})

# Her çiçek türü için kullanacağımız renkleri belirliyoruz.
renkler = {
    "setosa": "#2a78d6",
    "versicolor": "#eb6834",
    "virginica": "#1baf7a"
}

# Seaborn grafiklerinin genel görünümünü beyaz arka plan ve ızgaralı
# bir tema olarak ayarlıyoruz.
sns.set_theme(style="whitegrid")

# species ve tur sütunlarındaki farklı eşleşmeleri görüntülüyoruz.
# drop_duplicates() tekrar eden satırları kaldırır.
print(df[["species", "tur"]].drop_duplicates())


# %% 6.2 Sütun grafiği (bar chart) – Sütun grafikleri

# Her çiçek türünden kaç tane bulunduğunu sayıyoruz.
# sort_index() sonuçları sınıf indeksine göre sıralar.
sayilar = df["tur"].value_counts().sort_index()

# Her çiçek türünün dört ölçüm özelliği için ortalama değerlerini hesaplıyoruz.
ortalamalar = df.groupby("tur")[iris.feature_names].mean()

# Yan yana iki grafik oluşturuyoruz.
# figsize grafiğin genişliğini ve yüksekliğini belirler.
fig, axes = plt.subplots(1, 2, figsize=(12, 4.5))

# Birinci grafik: Her çiçek türünden kaç tane bulunduğunu gösteren sütun grafiği.
# bar() sütun grafiği oluşturur.
axes[0].bar(
    sayilar.index,
    sayilar.values,
    color=[renkler[t] for t in sayilar.index]
)

# Sütunların üzerine sayısal değerleri yazdırıyoruz.
axes[0].bar_label(axes[0].containers[0])

# Grafiğin başlığını ve dikey eksen açıklamasını belirliyoruz.
axes[0].set_title("Türlere göre çiçek sayısı")
axes[0].set_ylabel("Gözlem sayısı")

# İkinci grafik: Çiçek türlerine göre ortalama ölçümleri gösteriyoruz.
# T, satır ve sütunların yerini değiştirir.
# plot(kind="bar") sütun grafiği oluşturur.
ortalamalar.T.plot(
    kind="bar",
    ax=axes[1],
    color=[renkler[t] for t in ortalamalar.index]
)

# İkinci grafiğin başlığını ve eksen açıklamalarını belirliyoruz.
axes[1].set_title("Türlere göre ortalama ölçüler")
axes[1].set_ylabel("Ortalama (cm)")

# Yatay eksendeki yazıların eğimini 15 derece yapıyoruz.
axes[1].tick_params(axis="x", rotation=15)

# Grafikteki renklerin hangi çiçek türünü temsil ettiğini gösteriyoruz.
axes[1].legend(title="Tür")

# Grafiklerin birbirine ve kenarlara göre düzenli yerleşmesini sağlıyoruz.
plt.tight_layout()

# Oluşturduğumuz grafikleri ekranda gösteriyoruz.
plt.show()


# %% 6.3 Histogram – Histogramlar

# 2 satır ve 2 sütundan oluşan toplam 4 grafik alanı oluşturuyoruz.
# Her grafik bir çiçek ölçüm özelliğini temsil edecek.
fig, axes = plt.subplots(2, 2, figsize=(11, 7))

# axes.flat ile grafik alanlarını tek boyutlu olarak dolaşıyoruz.
# zip() ile grafik alanlarını ve özellik isimlerini eşleştiriyoruz.
for ax, ozellik in zip(axes.flat, iris.feature_names):

    # Her grafik içerisinde üç farklı çiçek türünü ayrı ayrı gösteriyoruz.
    for tur, renk in renkler.items():

        # İlgili çiçek türüne ait ölçüm değerlerini seçiyoruz.
        degerler = df.loc[df["tur"] == tur, ozellik]

        # Seçilen ölçüm değerlerinin histogramını oluşturuyoruz.
        ax.hist(
            degerler,
            bins=12,             # Verileri 12 aralığa bölüyoruz.
            alpha=0.6,           # Sütunların saydamlık oranını ayarlıyoruz.
            color=renk,          # Çiçek türüne ait rengi kullanıyoruz.
            label=tur,           # Grafik açıklamasına tür ismini ekliyoruz.
            edgecolor="white"    # Sütunların kenar rengini beyaz yapıyoruz.
        )

    # Her grafiğin başlığını ve dikey eksen açıklamasını belirliyoruz.
    ax.set_title(ozellik)
    ax.set_ylabel("Frekans")

# İlk histogramın üzerine renklerin hangi türleri gösterdiğini belirten açıklama ekliyoruz.
axes[0, 0].legend(title="Tür")

# Grafiklerin düzenli yerleşmesini sağlıyoruz.
plt.tight_layout()

# Histogramları ekranda gösteriyoruz.
plt.show()


# %% 6.4 Saçılım grafiği (scatter plot) – Saçılım grafikleri

# Her çiçek türünü farklı bir işaret şekliyle göstermek için sözlük oluşturuyoruz.
# o: Daire, s: Kare, ^: Üçgen
isaretler = {
    "setosa": "o",
    "versicolor": "s",
    "virginica": "^"
}

# Birbirleriyle karşılaştıracağımız özellik çiftlerini belirliyoruz.
# İlk grafik: Çanak yaprak uzunluğu ve genişliği.
# İkinci grafik: Taç yaprak uzunluğu ve genişliği.
ciftler = [
    ("sepal length (cm)", "sepal width (cm)"),
    ("petal length (cm)", "petal width (cm)")
]

# Yan yana iki saçılım grafiği oluşturuyoruz.
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Her grafik için karşılaştırılacak özellik çiftlerini dolaşıyoruz.
for ax, (x_ozellik, y_ozellik) in zip(axes, ciftler):

    # Her çiçek türünü ayrı ayrı grafiğe ekliyoruz.
    for tur, renk in renkler.items():

        # Sadece ilgili çiçek türüne ait satırları seçiyoruz.
        secim = df[df["tur"] == tur]

        # Seçilen çiçeklerin iki özelliğini karşılaştırarak grafiğe işliyoruz.
        ax.scatter(
            secim[x_ozellik],     # Yatay eksende gösterilecek özellik
            secim[y_ozellik],     # Dikey eksende gösterilecek özellik
            color=renk,           # Çiçek türüne ait renk
            marker=isaretler[tur],# Çiçek türüne ait işaret şekli
            s=45,                 # Noktaların büyüklüğü
            edgecolor="white",    # Noktaların kenar rengi
            label=tur             # Çiçek türünün adı
        )

    # Yatay ve dikey eksenlerin isimlerini belirliyoruz.
    ax.set_xlabel(x_ozellik)
    ax.set_ylabel(y_ozellik)

# Birinci ve ikinci grafiklerin başlıklarını belirliyoruz.
axes[0].set_title("Sepal ölçüleri")
axes[1].set_title("Petal ölçüleri")

# İkinci grafiğe çiçek türlerini açıklayan gösterge ekliyoruz.
axes[1].legend(title="Tür")

# Grafiklerin düzenli yerleşmesini sağlıyoruz.
plt.tight_layout()

# Saçılım grafiklerini ekranda gösteriyoruz.
plt.show()


# %% 6.5 Çiftli grafik (pairplot) – Pairplot

# Pairplot, veri setindeki sayısal özelliklerin ikili ilişkilerini
# tek bir grafik düzeni içerisinde gösterir.
#
# species sütununu kaldırıyoruz çünkü tur sütununu renk ayrımı için kullanacağız.
# hue="tur" her çiçek türünü farklı renkte gösterir.
# hue_order türlerin gösterim sırasını belirler.
# palette renkleri belirler.
# markers her tür için farklı işaret şekli kullanır.
# height her küçük grafiğin yüksekliğini belirler.

g = sns.pairplot(
    df.drop(columns="species"),
    hue="tur",
    hue_order=list(renkler),
    palette=renkler,
    markers=["o", "s", "^"],
    height=2.3
)

# Tüm grafik düzeninin üst kısmına genel bir başlık ekliyoruz.
g.figure.suptitle(
    "Iris veri seti – tüm özellik çiftleri",
    y=1.02
)

# Pairplot grafiğini ekranda gösteriyoruz.
plt.show()


# %% 6.6 Korelasyon ısı haritası (correlation heatmap) – Korelasyon ısı haritası

# Iris veri setindeki dört ölçüm özelliği arasındaki korelasyonu hesaplıyoruz.
# corr() sayısal sütunlar arasındaki ilişkinin yönünü ve gücünü gösterir.
korelasyon = df[iris.feature_names].corr()

# Isı haritası için grafik alanı oluşturuyoruz.
plt.figure(figsize=(7.5, 6))

# Korelasyon değerlerini renklerle gösteren ısı haritasını oluşturuyoruz.
sns.heatmap(
    korelasyon,
    annot=True,          # Hücrelerin içine korelasyon değerlerini yazdırır.
    fmt=".2f",           # Sayıları virgülden sonra iki basamakla gösterir.
    cmap="coolwarm",     # Pozitif ve negatif değerler için renk geçişi kullanır.
    vmin=-1,             # Korelasyonun alabileceği en düşük değer.
    vmax=1,              # Korelasyonun alabileceği en yüksek değer.
    square=True,         # Hücrelerin kare şeklinde olmasını sağlar.
    linewidths=2         # Hücreler arasındaki çizgi kalınlığını belirler.
)

# Grafiğin başlığını belirliyoruz.
plt.title("Özellikler arası korelasyon")

# Grafik düzenini ayarlıyoruz.
plt.tight_layout()

# Korelasyon ısı haritasını ekranda gösteriyoruz.
plt.show()