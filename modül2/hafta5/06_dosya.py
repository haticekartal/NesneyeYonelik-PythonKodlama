# UYGULAMA 10: JSON dosyasıyla öğrenci kayıt sistemi

# Gerekli kütüphaneleri ekliyoruz
import json
import os


# JSON dosyasından öğrenci listesini okuyan fonksiyon
def ogrencileri_oku():

    # Dosya henüz oluşturulmamışsa boş liste döndürüyoruz
    if not os.path.exists("ogrenciler.json"):
        return []

    # Dosyayı okuma modunda açıyoruz
    with open("ogrenciler.json", "r", encoding="utf-8") as dosya:

        # JSON verilerini Python listesine dönüştürüyoruz
        ogrenciler = json.load(dosya)

    return ogrenciler


# Öğrenci listesini JSON dosyasına kaydeden fonksiyon
def ogrencileri_kaydet(ogrenciler):

    # Dosyayı yazma modunda açıyoruz
    with open("ogrenciler.json", "w", encoding="utf-8") as dosya:

        # Listeyi JSON biçiminde kaydediyoruz
        json.dump(ogrenciler, dosya, ensure_ascii=False, indent=4)


# Yeni öğrenci ekleyen fonksiyon
def ogrenci_ekle():

    # Önce mevcut öğrencileri okuyoruz
    ogrenciler = ogrencileri_oku()

    # Kullanıcıdan bilgi alıyoruz
    ad = input("Öğrenci adı: ")
    notu = float(input("Öğrenci notu: "))

    # Yeni öğrenci sözlüğünü oluşturuyoruz
    yeni_ogrenci = {
        "ad": ad,
        "not": notu
    }

    # Öğrenciyi listeye ekliyoruz
    ogrenciler.append(yeni_ogrenci)

    # Güncellenmiş listeyi dosyaya kaydediyoruz
    ogrencileri_kaydet(ogrenciler)

    print("Öğrenci başarıyla kaydedildi.")


# Öğrencileri listeleyen fonksiyon
def ogrencileri_listele():

    # JSON dosyasından verileri okuyoruz
    ogrenciler = ogrencileri_oku()

    if len(ogrenciler) == 0:
        print("Kayıtlı öğrenci bulunmuyor.")
        return

    # Öğrencileri yazdırıyoruz
    for ogrenci in ogrenciler:

        print(ogrenci["ad"], "-", ogrenci["not"])


# Sınıf ortalamasını hesaplayan fonksiyon
def sinif_ortalamasi():

    # Öğrencileri dosyadan okuyoruz
    ogrenciler = ogrencileri_oku()

    if len(ogrenciler) == 0:
        print("Henüz öğrenci kaydı yok.")
        return

    toplam = 0

    # Bütün öğrenci notlarını topluyoruz
    for ogrenci in ogrenciler:

        toplam += ogrenci["not"]

    # Ortalamayı hesaplıyoruz
    ortalama = toplam / len(ogrenciler)

    print("Sınıf ortalaması:", round(ortalama, 2))


# Ana program
while True:

    print("\n--- ÖĞRENCİ KAYIT SİSTEMİ ---")
    print("1 - Öğrenci ekle")
    print("2 - Öğrencileri listele")
    print("3 - Sınıf ortalaması")
    print("4 - Çıkış")

    secim = input("Seçiminiz: ")

    if secim == "1":
        ogrenci_ekle()

    elif secim == "2":
        ogrencileri_listele()

    elif secim == "3":
        sinif_ortalamasi()

    elif secim == "4":
        print("Program sonlandırıldı.")
        break

    else:
        print("Geçersiz seçim.")