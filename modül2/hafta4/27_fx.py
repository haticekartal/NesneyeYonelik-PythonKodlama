# UYGULAMA 5: Gelişmiş sayı tahmin oyunu

# Rastgele sayı üretmek için kütüphane ekliyoruz
import random


# Rastgele sayı oluşturan fonksiyon
def sayi_uret():

    return random.randint(1, 100)


# Tahminleri kontrol eden fonksiyon
def tahmin_kontrol(tahmin, gizli):

    if tahmin < gizli:
        return "Daha büyük sayı giriniz."

    elif tahmin > gizli:
        return "Daha küçük sayı giriniz."

    else:
        return "Doğru tahmin!"


# Puan hesaplayan fonksiyon
def puan_hesapla(deneme):

    puan = 100 - (deneme - 1) * 10

    # Puanın sıfırın altına düşmesini engelliyoruz
    if puan < 0:
        puan = 0

    return puan


# Oyunu başlatan fonksiyon
def oyun_baslat():

    # Gizli sayıyı oluşturuyoruz
    gizli = sayi_uret()

    deneme = 0

    print("\n1 ile 100 arasında bir sayı tuttum.")

    # Tahmin döngüsü
    while True:

        tahmin = int(input("Tahmininiz: "))

        deneme += 1

        # Tahminin sonucunu kontrol ediyoruz
        mesaj = tahmin_kontrol(tahmin, gizli)

        print(mesaj)

        # Doğru tahmin kontrolü
        if tahmin == gizli:

            puan = puan_hesapla(deneme)

            print("Deneme sayısı:", deneme)
            print("Puanınız:", puan)

            break


# Oyunun tekrar oynanabilmesi için döngü
while True:

    oyun_baslat()

    cevap = input("Tekrar oynamak ister misiniz? (e/h): ")

    if cevap.lower() != "e":
        print("Oyun sona erdi.")
        break