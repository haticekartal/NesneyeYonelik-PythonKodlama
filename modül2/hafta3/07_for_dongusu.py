# UYGULAMA : Üç haklı sayı tahmin oyunu

# Tahmin edilecek sayı
gizli_sayi = 7

# Kullanıcının üç tahmin hakkı var
for hak in range(1, 4):

    tahmin = int(input("1-10 arasında tahmin yapınız: "))

    # Tahmin doğruysa
    if tahmin == gizli_sayi:
        print("Tebrikler! Doğru bildiniz.")

        # Döngüyü sonlandır
        break

    else:
        print("Yanlış tahmin!")