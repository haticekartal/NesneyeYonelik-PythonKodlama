# Gerekli kütüphaneleri içe aktaralım
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt

# Iris veri setini yükleyelim
iris = load_iris()

# Çiçeklerin özelliklerini X değişkenine aktaralım
X = iris.data

# Çiçeklerin türlerini y değişkenine aktaralım
y = iris.target

# Karar ağacı modelini oluşturalım
# max_depth=3: Ağacın maksimum derinliğini 3 olarak belirler
model = DecisionTreeClassifier(max_depth=3)

# Modeli eğitim verileriyle eğitelim
model.fit(X, y)

# Grafiğin boyutunu belirleyelim
plt.figure(figsize=(12, 7))

# Karar ağacını görselleştirelim
plot_tree(
    model,
    feature_names=iris.feature_names,  # Özelliklerin isimlerini göster
    class_names=iris.target_names,    # Çiçek türlerinin isimlerini göster
    filled=True                        # Karar ağacındaki kutuları renklendir
)

# Grafiği ekranda gösterelim
plt.show()