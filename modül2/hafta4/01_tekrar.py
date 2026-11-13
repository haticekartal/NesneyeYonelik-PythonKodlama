# UYGULAMA: 1'den n'e kadar olan sayıların toplamını hesaplama

n = int(input("n değerini girin: "))

toplam = 0

for sayi in range(1, n + 1):
    toplam += sayi

print("1'den", n, "'e kadar sayıların toplamı:", toplam)