# UYGULAMA : 1'den 10'a kadar sayıları yazdırma
# Döngü 1'den başlar, 11'e ulaşmadan durur
for sayi in range(1, 11):

    # Sayının değerini ekrana yazdırır
    print(sayi)


# UYGULAMA : 1 ile 20 arasındaki çift sayıları yazdırma
# 2'den başla, ikişer ikişer artır
for sayi in range(2, 21, 2):

    print(sayi)


# UYGULAMA : 10'dan 1'e kadar geri sayma
# 10'dan başla, her seferinde 1 azalt
for sayi in range(10, 0, -1):

    print(sayi)

# Döngü tamamlandıktan sonra çalışır
print("Geri sayım tamamlandı!")