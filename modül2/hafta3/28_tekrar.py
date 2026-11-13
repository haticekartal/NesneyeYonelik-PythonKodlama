# UYGULAMA 43: Basit öğrenci kayıt sistemi

# Boş öğrenci listesi
ogrenciler = []

# Kaydedilecek öğrenci sayısını alalım
adet = int(input("Kaç öğrenci kaydedilecek? "))

# Girilen sayı kadar öğrenci kaydedelim
for i in range(adet):

    # Öğrencinin adını alalım
    ad = input("Öğrencinin adı: ")

    # İsmi listeye ekleyelim
    ogrenciler.append(ad)

# Kayıt tamamlandı
print("\nÖğrenci kayıtları tamamlandı!")

# Toplam öğrenci sayısını gösterelim
print("Toplam öğrenci:", len(ogrenciler))

# Öğrencileri numaralandırarak yazdıralım
for sira, ogrenci in enumerate(ogrenciler, start=1):

    print(sira, "-", ogrenci)