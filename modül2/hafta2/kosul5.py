# UYGULAMA 5: Girilen iki sayıdan büyük olanı bulma

sayi1 = int(input("Birinci sayıyı girin: "))
sayi2 = int(input("İkinci sayıyı girin: "))

if sayi1 > sayi2:
    print("Birinci sayı daha büyüktür.")
elif sayi2 > sayi1:
    print("İkinci sayı daha büyüktür.")
else:
    print("İki sayı eşittir.")