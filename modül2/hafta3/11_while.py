# UYGULAMA 16: Menü ile çalışan basit program

while True:

    print("\n----- ANA MENÜ -----")
    print("1 - Merhaba yazdır")
    print("2 - İki sayı topla")
    print("3 - Çıkış")

    secim = input("Seçiminizi yapınız: ")

    if secim == "1":
        print("Merhaba Python!")

    elif secim == "2":

        sayi1 = int(input("Birinci sayı: "))
        sayi2 = int(input("İkinci sayı: "))

        print("Toplam:", sayi1 + sayi2)

    elif secim == "3":
        print("Program kapatılıyor...")
        break

    else:
        print("Geçersiz seçim!")