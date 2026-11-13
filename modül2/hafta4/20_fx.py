# UYGULAMA 18: 1'den 5'e kadar sayıların karesini hesaplama

# Kare alma fonksiyonu
def kare_al(sayi):
    return sayi * sayi

# Döngü ile fonksiyonu tekrar tekrar çağırıyoruz
for sayi in range(1, 6):

    sonuc = kare_al(sayi)

    print(sayi, "sayısının karesi:", sonuc)




# UYGULAMA 19: Listedeki sayıların ortalamasını bulma

# Liste alan fonksiyon
def ortalama_hesapla(sayilar):

    toplam = sum(sayilar)

    adet = len(sayilar)

    ortalama = toplam / adet

    return ortalama

# Sayı listesi oluşturuyoruz
notlar = [70, 80, 90, 60, 100]

# Fonksiyonu çağırıyoruz
sonuc = ortalama_hesapla(notlar)

# Sonucu yazdırıyoruz
print("Sınıf ortalaması:", sonuc)