# UYGULAMA: 1 ile 50 arasında hem 3'e hem 5'e bölünen sayıları bulma

adet = 0

for sayi in range(1, 51):
    if sayi % 3 == 0 and sayi % 5 == 0:
        print(sayi, end=" ")
        adet += 1

print()
print("Toplam", adet, "sayı bulundu.")