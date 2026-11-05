# Başarı metriklerini hesaplamak için gerekli fonksiyonları içe aktarıyoruz.
from sklearn.metrics import (
    accuracy_score,       # Genel doğruluk oranı
    precision_score,      # Kesinlik
    recall_score,         # Duyarlılık
    f1_score,             # F1 skoru
    confusion_matrix     # Karmaşıklık matrisi
)

# Gerçek sınıflar:
# İlk 50 e-posta spam, sonraki 50 e-posta normaldir.
y_gercek = ["spam"] * 50 + ["normal"] * 50

# Modelin tahmin ettiği sınıflar:
# İlk 50 gerçek spam e-postanın:
# 40 tanesi spam, 10 tanesi normal tahmin edilmiş.
#
# Sonraki 50 gerçek normal e-postanın:
# 5 tanesi spam, 45 tanesi normal tahmin edilmiş.

y_tahmin = (
    ["spam"] * 40 + ["normal"] * 10 +
    ["spam"] * 5 + ["normal"] * 45
)

# KARMAŞIKLIK MATRİSİ (CONFUSION MATRIX)
# Gerçek sınıflar ile modelin tahminlerini karşılaştırır.
# Satırlar gerçek sınıfları, sütunlar tahmin edilen sınıfları gösterir.
# Sıralama: spam, normal

print(confusion_matrix(
    y_gercek,
    y_tahmin,
    labels=["spam", "normal"]
))

# ACCURACY (DOĞRULUK)
# Modelin bütün tahminlerinin yüzde kaçının doğru olduğunu hesaplar.
print("Accuracy :", accuracy_score(y_gercek, y_tahmin))

# PRECISION (KESİNLİK)
# Modelin spam dediği e-postaların ne kadarının gerçekten spam olduğunu gösterir.
# pos_label="spam", pozitif sınıf olarak spam'i seçer.
print("Precision:", round(
    precision_score(y_gercek, y_tahmin, pos_label="spam"), 3
))

# RECALL (DUYARLILIK)
# Gerçek spam e-postaların ne kadarının doğru tespit edildiğini gösterir.
print("Recall   :", recall_score(
    y_gercek, y_tahmin, pos_label="spam"
))

# F1-SCORE
# Precision ve Recall değerlerinin harmonik ortalamasıdır.
# İki metriği birlikte değerlendirmemizi sağlar.
print("F1-score :", round(
    f1_score(y_gercek, y_tahmin, pos_label="spam"), 3
))