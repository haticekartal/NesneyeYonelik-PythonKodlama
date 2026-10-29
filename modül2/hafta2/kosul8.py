# UYGULAMA 8: Alışveriş tutarına göre indirim hesaplama

tutar = float(input("Alışveriş tutarını girin (TL): "))

if tutar >= 1000:
    indirim = tutar * 0.20
elif tutar >= 500:
    indirim = tutar * 0.10
else:
    indirim = 0

odenecek = tutar - indirim

print(f"İndirim tutarı: {indirim:.2f} TL")
print(f"Ödenecek tutar: {odenecek:.2f} TL")