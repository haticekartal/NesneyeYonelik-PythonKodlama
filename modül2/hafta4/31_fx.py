# UYGULAMA 12: Müşteri memnuniyet anketi

# Kullanıcılardan puan alan fonksiyon
def puanlari_topla(kisi_sayisi):

    puanlar = []

    for i in range(kisi_sayisi):

        while True:

            puan = int(input(str(i + 1) + ". kişinin puanı (1-5): "))

            # Geçerli puan kontrolü
            if 1 <= puan <= 5:

                puanlar.append(puan)
                break

            else:
                print("Puan 1 ile 5 arasında olmalıdır.")

    return puanlar


# Ortalama memnuniyet puanını hesaplayan fonksiyon
def ortalama_hesapla(puanlar):

    toplam = sum(puanlar)

    return toplam / len(puanlar)


# Her puanın kaç defa verildiğini bulan fonksiyon
def puan_dagilimi(puanlar):

    dagilim = {}

    for puan in range(1, 6):

        # Listedeki ilgili puanın sayısını buluyoruz
        dagilim[puan] = puanlar.count(puan)

    return dagilim


# Memnuniyet durumunu yorumlayan fonksiyon
def memnuniyet_yorumla(ortalama):

    if ortalama >= 4:
        return "Yüksek memnuniyet"

    elif ortalama >= 3:
        return "Orta memnuniyet"

    else:
        return "Düşük memnuniyet"


# Kullanıcıdan kişi sayısını alıyoruz
kisi_sayisi = int(input("Ankete kaç kişi katılacak? "))

if kisi_sayisi > 0:

    # Puanları topluyoruz
    puanlar = puanlari_topla(kisi_sayisi)

    # Analiz fonksiyonlarını çalıştırıyoruz
    ortalama = ortalama_hesapla(puanlar)

    dagilim = puan_dagilimi(puanlar)

    yorum = memnuniyet_yorumla(ortalama)

    # Sonuçları yazdırıyoruz
    print("\n--- ANKET RAPORU ---")
    print("Katılımcı sayısı:", kisi_sayisi)
    print("Ortalama puan:", round(ortalama, 2))
    print("Puan dağılımı:", dagilim)
    print("Memnuniyet durumu:", yorum)

else:
    print("Katılımcı sayısı pozitif olmalıdır.")