# UYGULAMA : Girilen sayıya göre haftanın gününü bulma

gun = int(input("1-7 arasında bir sayı giriniz: "))

# Girilen sayıyı kontrol edelim
match gun:

    case 1:
        print("Pazartesi")

    case 2:
        print("Salı")

    case 3:
        print("Çarşamba")

    case 4:
        print("Perşembe")

    case 5:
        print("Cuma")

    case 6:
        print("Cumartesi")

    case 7:
        print("Pazar")

    case _:
        print("Geçersiz gün numarası!")