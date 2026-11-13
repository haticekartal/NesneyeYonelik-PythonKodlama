# UYGULAMA: 2 ile 30 arasındaki asal sayıları bulma

print("2 ile 30 arasındaki asal sayılar:")

adet = 0

for sayi in range(2, 31):
    for bolen in range(2, sayi):
        if sayi % bolen == 0:
            break
    else:
        print(sayi, end=" ")
        adet += 1

print()
print("Toplam", adet, "asal sayı bulundu.")