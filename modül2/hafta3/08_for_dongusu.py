# UYGULAMA 13: 1'den 10'a kadar sayıları yazdırma
# Ancak 5 sayısını atlama

for sayi in range(1, 11):

    # Sayı 5 olduğunda bu turu atla
    if sayi == 5:
        continue

    # Diğer sayıları yazdır
    print(sayi)