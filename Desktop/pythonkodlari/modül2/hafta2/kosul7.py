# UYGULAMA 7: Kullanıcının yaşına göre bilet türünü belirleme

yas = int(input("Yaşınızı girin: "))

if yas < 0:
    print("Geçersiz yaş.")
elif yas < 7:
    print("Bilet ücretsiz.")
elif yas < 18:
    print("İndirimli bilet.")
else:
    print("Tam bilet.")