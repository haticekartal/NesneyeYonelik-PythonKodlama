# UYGULAMA: Sayı tahmin oyunu

gizli = 37

deneme = 0

while True:
    tahmin = int(input("Tahmininiz (1-100): "))

    deneme += 1

    if tahmin < gizli:
        print("Daha büyük bir sayı deneyin.")

    elif tahmin > gizli:
        print("Daha küçük bir sayı deneyin.")

    else:
        print("Tebrikler!", deneme, "denemede buldunuz.")
        break