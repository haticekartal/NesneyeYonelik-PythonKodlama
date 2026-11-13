# UYGULAMA 3: Sınıf not analiz sistemi

# Notları kullanıcıdan alan fonksiyon
def notlari_al():

    notlar = []

    adet = int(input("Öğrenci sayısını giriniz: "))

    # Her öğrenciden not alıyoruz
    for i in range(adet):

        notu = float(input(str(i + 1) + ". öğrenci notu: "))

        # Girilen notu listeye ekliyoruz
        notlar.append(notu)

    # Oluşturulan listeyi döndürüyoruz
    return notlar


# Not ortalamasını hesaplayan fonksiyon
def ortalama_hesapla(notlar):

    toplam = sum(notlar)

    ortalama = toplam / len(notlar)

    return ortalama


# En yüksek ve en düşük notları bulan fonksiyon
def not_analizi(notlar):

    en_yuksek = max(notlar)

    en_dusuk = min(notlar)

    return en_yuksek, en_dusuk


# Geçen öğrenci sayısını bulan fonksiyon
def gecen_sayisi(notlar):

    adet = 0

    for notu in notlar:

        if notu >= 50:
            adet += 1

    return adet


# Ana program
notlar = notlari_al()

# Boş liste oluşmasını kontrol ediyoruz
if len(notlar) > 0:

    ortalama = ortalama_hesapla(notlar)

    en_yuksek, en_dusuk = not_analizi(notlar)

    gecen = gecen_sayisi(notlar)

    print("\n--- SINIF ANALİZİ ---")

    print("Notlar:", notlar)
    print("Sınıf ortalaması:", round(ortalama, 2))
    print("En yüksek not:", en_yuksek)
    print("En düşük not:", en_dusuk)
    print("Geçen öğrenci sayısı:", gecen)
    print("Kalan öğrenci sayısı:", len(notlar) - gecen)

else:
    print("Analiz için en az bir öğrenci gereklidir.")