# UYGULAMA 17: Bakiyeye ve çekilmek istenen tutara göre para çekme

bakiye = 2500
tutar = float(input("Çekmek istediğiniz tutarı girin: "))

if tutar <= 0:
    print("Geçersiz tutar.")
elif tutar > bakiye:
    print("Yetersiz bakiye.")
else:
    bakiye = bakiye - tutar
    print("Para çekme işlemi başarılı.")
    print(f"Kalan bakiye: {bakiye:.2f} TL")