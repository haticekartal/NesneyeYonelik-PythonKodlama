# UYGULAMA 1: Öğrenci not analiz sistemi

# Üç sınav notunun ortalamasını hesaplayan fonksiyon
def ortalama_hesapla(not1, not2, not3):

    ortalama = (not1 + not2 + not3) / 3

    return ortalama


# Ortalamaya göre harf notunu belirleyen fonksiyon
def harf_notu_bul(ortalama):

    if ortalama >= 90:
        return "AA"

    elif ortalama >= 80:
        return "BA"

    elif ortalama >= 70:
        return "BB"

    elif ortalama >= 60:
        return "CB"

    elif ortalama >= 50:
        return "CC"

    else:
        return "FF"


# Öğrencinin geçme durumunu belirleyen fonksiyon
def durum_kontrol(ortalama):

    if ortalama >= 50:
        return "Geçti"

    else:
        return "Kaldı"


# Öğrenci bilgilerini ekrana yazdıran fonksiyon
def sonuc_goster(ad, ortalama, harf, durum):

    print("\n--- ÖĞRENCİ SONUÇ RAPORU ---")

    print("Öğrenci:", ad)
    print("Ortalama:", round(ortalama, 2))
    print("Harf notu:", harf)
    print("Durum:", durum)


# Kullanıcıdan bilgileri alıyoruz
ad = input("Öğrenci adını giriniz: ")

not1 = float(input("1. sınav notu: "))
not2 = float(input("2. sınav notu: "))
not3 = float(input("3. sınav notu: "))

# Fonksiyonları sırayla çağırıyoruz
ortalama = ortalama_hesapla(not1, not2, not3)

harf = harf_notu_bul(ortalama)

durum = durum_kontrol(ortalama)

# Sonuçları ekrana yazdırıyoruz
sonuc_goster(ad, ortalama, harf, durum)