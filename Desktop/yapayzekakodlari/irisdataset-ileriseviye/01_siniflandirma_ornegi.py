# Gerekli kütüphaneyi içe aktarıyoruz.
# DecisionTreeClassifier, Karar Ağacı sınıflandırma algoritmasıdır.
from sklearn.tree import DecisionTreeClassifier

# Eğitim verileri:
# Her satır bir e-postayı temsil eder.
# İlk değer: E-postadaki bağlantı sayısı
# İkinci değer: "Bedava/kazandınız" kelime sayısı

X_egitim = [
    [0, 0],
    [1, 0],
    [2, 1],
    [8, 3],
    [6, 4],
    [9, 2]
]

# E-postaların gerçek sınıfları:
# İlk üç e-posta normal, son üç e-posta spam olarak etiketlenmiştir.
# Bu etiketler, modelin eğitim sırasında öğrenmesini sağlar.

y_egitim = [
    "normal",
    "normal",
    "normal",
    "spam",
    "spam",
    "spam"
]

# Karar ağacı modelini oluşturuyoruz.
# random_state=0, sonuçların tekrar çalıştırıldığında
# aynı şekilde elde edilmesine yardımcı olur.

model = DecisionTreeClassifier(random_state=0)

# EĞİTİM AŞAMASI
# Model, X_egitim içerisindeki özellikleri ve
# y_egitim içerisindeki sınıfları inceleyerek öğrenir.

model.fit(X_egitim, y_egitim)

# Yeni e-postalar oluşturuyoruz.
# Henüz bu e-postaların normal mi spam mı olduğunu bilmiyoruz.

yeni_epostalar = [
    [1, 1],  # 1 bağlantı, 1 şüpheli kelime
    [7, 5]   # 7 bağlantı, 5 şüpheli kelime
]

# TAHMİN AŞAMASI
# Eğitilmiş model, yeni e-postaların sınıflarını tahmin eder.

tahminler = model.predict(yeni_epostalar)

# Tahmin sonuçlarını ekrana yazdırıyoruz.
print(tahminler)