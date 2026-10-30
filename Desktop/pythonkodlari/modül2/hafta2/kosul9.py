sayi1 = float(input("Birinci sayıyı giriniz: "))
sayi2 = float(input("İkinci sayıyı giriniz: "))

islem = input("İşlem seçiniz (+, -, *, /): ")

if islem == "+":
    print("Sonuç:", sayi1 + sayi2)

elif islem == "-":
    print("Sonuç:", sayi1 - sayi2)

elif islem == "*":
    print("Sonuç:", sayi1 * sayi2)

elif islem == "/":
    if sayi2 != 0:
        print("Sonuç:", sayi1 / sayi2)
    else:
        print("Bir sayı sıfıra bölünemez.")

else:
    print("Geçersiz işlem.")





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