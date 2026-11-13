# UYGULAMA : 1'den 10'a kadar sayıların toplamını bulma

# Başlangıçta toplam değerimiz sıfırdır
toplam = 0

# 1'den 10'a kadar sayıları dolaşalım
for sayi in range(1, 11):

    # Her sayıyı toplam değişkenine ekleyelim
    toplam = toplam + sayi

# Döngü bittikten sonra sonucu gösterelim
print("Sayıların toplamı:", toplam)





# UYGULAMA : Beş öğrencinin not ortalamasını hesaplama
toplam = 0
# Beş öğrenciden not alalım
for i in range(5):

    # Kullanıcıdan not alınır
    notu = float(input("Öğrenci notunu giriniz: "))

    # Girilen not toplama eklenir
    toplam = toplam + notu

# Toplam notu öğrenci sayısına bölelim
ortalama = toplam / 5

print("Sınıfın not ortalaması:", ortalama)