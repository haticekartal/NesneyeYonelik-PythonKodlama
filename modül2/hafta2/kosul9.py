# UYGULAMA 9: Match-case ile basit hesap makinesi oluşturma

sayi1 = float(input("Birinci sayıyı girin: "))
islem = input("İşlem seçin (+, -, *, /): ")
sayi2 = float(input("İkinci sayıyı girin: "))

match islem:
    case "+":
        print("Sonuç:", sayi1 + sayi2)
    case "-":
        print("Sonuç:", sayi1 - sayi2)
    case "*":
        print("Sonuç:", sayi1 * sayi2)
    case "/":
        if sayi2 != 0:
            print("Sonuç:", sayi1 / sayi2)
        else:
            print("Bir sayı sıfıra bölünemez.")
    case _:
        print("Geçersiz işlem.")