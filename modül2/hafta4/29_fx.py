# UYGULAMA 7: Öğrenci kayıt sistemi

# Öğrenci ekleme fonksiyonu
def ogrenci_ekle(ogrenciler):

    ad = input("Öğrenci adı: ")
    notu = float(input("Öğrenci notu: "))

    # Öğrenci bilgilerini sözlük olarak oluşturuyoruz
    ogrenci = {
        "ad": ad,
        "not": notu
    }

    # Öğrenciyi listeye ekliyoruz
    ogrenciler.append(ogrenci)

    print("Öğrenci başarıyla eklendi.")


# Öğrencileri listeleme fonksiyonu
def ogrencileri_listele(ogrenciler):

    if len(ogrenciler) == 0:
        print("Kayıtlı öğrenci bulunmuyor.")
        return

    print("\n--- ÖĞRENCİLER ---")

    for ogrenci in ogrenciler:

        print(ogrenci["ad"], "-", ogrenci["not"])


# Öğrenci arama fonksiyonu
def ogrenci_ara(ogrenciler, aranan_ad):

    for ogrenci in ogrenciler:

        # Büyük/küçük harf farkını kaldırıyoruz
        if ogrenci["ad"].lower() == aranan_ad.lower():

            return ogrenci

    # Öğrenci bulunamadığında
    return None


# Öğrenci silme fonksiyonu
def ogrenci_sil(ogrenciler, aranan_ad):

    # Önce öğrenciyi arıyoruz
    ogrenci = ogrenci_ara(ogrenciler, aranan_ad)

    if ogrenci is not None:

        # Öğrenciyi listeden siliyoruz
        ogrenciler.remove(ogrenci)

        print("Öğrenci silindi.")

    else:
        print("Öğrenci bulunamadı.")


# Boş öğrenci listesi
ogrenciler = []


# Ana program
while True:

    print("\n--- ÖĞRENCİ KAYIT SİSTEMİ ---")
    print("1 - Öğrenci ekle")
    print("2 - Öğrencileri listele")
    print("3 - Öğrenci ara")
    print("4 - Öğrenci sil")
    print("5 - Çıkış")

    secim = input("Seçiminiz: ")

    if secim == "1":

        ogrenci_ekle(ogrenciler)

    elif secim == "2":

        ogrencileri_listele(ogrenciler)

    elif secim == "3":

        ad = input("Aranacak öğrenci adı: ")

        sonuc = ogrenci_ara(ogrenciler, ad)

        if sonuc is not None:
            print("Öğrenci bulundu:", sonuc)

        else:
            print("Öğrenci bulunamadı.")

    elif secim == "4":

        ad = input("Silinecek öğrenci adı: ")

        ogrenci_sil(ogrenciler, ad)

    elif secim == "5":

        print("Program kapatıldı.")
        break

    else:
        print("Geçersiz seçim.")