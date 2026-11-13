# UYGULAMA 3: Sınav notuna göre geçme veya kalma durumunu belirleme

notu = float(input("Sınav notunuzu girin: "))

if notu >= 50:
    print("Dersi geçtiniz.")
else:
    print("Dersten kaldınız.")