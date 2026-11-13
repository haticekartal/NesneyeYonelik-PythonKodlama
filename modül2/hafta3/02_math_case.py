# UYGULAMA : Match-case ile hesap makinesi

sayi1 = float(input("Birinci sayıyı giriniz: "))
sayi2 = float(input("İkinci sayıyı giriniz: "))

print("1 - Toplama")
print("2 - Çıkarma")
print("3 - Çarpma")
print("4 - Bölme")

secim = int(input("İşlem seçiniz: "))

match secim:

    case 1:
        print("Sonuç:", sayi1 + sayi2)

    case 2:
        print("Sonuç:", sayi1 - sayi2)

    case 3:
        print("Sonuç:", sayi1 * sayi2)

    case 4:
        # Sıfıra bölme kontrolü
        if sayi2 != 0:
            print("Sonuç:", sayi1 / sayi2)
        else:
            print("Bir sayı sıfıra bölünemez!")

    case _:
        print("Geçersiz işlem seçimi!")