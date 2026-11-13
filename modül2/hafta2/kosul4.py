# UYGULAMA 4: Sınav notuna göre başarı derecesini belirleme

notu = float(input("Sınav notunuzu girin: "))

if notu < 0 or notu > 100:
    print("Geçersiz not girdiniz.")
elif notu >= 85:
    print("Pekiyi")
elif notu >= 70:
    print("İyi")
elif notu >= 50:
    print("Geçti")
else:
    print("Kaldı")