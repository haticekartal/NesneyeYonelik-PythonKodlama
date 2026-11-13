# UYGULAMA : Kullanıcı 0 girene kadar sayı isteme

while True:

    # Kullanıcıdan sayı alınır
    sayi = int(input("Bir sayı giriniz: "))

    # Girilen sayı ekrana yazılır
    print("Girdiğiniz sayı:", sayi)

    # Kullanıcı 0 girerse döngü biter
    if sayi == 0:
        print("Program sona erdi.")
        break