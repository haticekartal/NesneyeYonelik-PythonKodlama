# UYGULAMA 14: Alışveriş indirimini hesaplama

# İndirim hesaplayan fonksiyon
def indirim_hesapla(tutar):

    if tutar >= 1000:
        indirim = tutar * 0.20

    elif tutar >= 500:
        indirim = tutar * 0.10

    else:
        indirim = 0

    # Ödenecek tutarı hesaplıyoruz
    odenecek = tutar - indirim

    return odenecek

# Alışveriş tutarını alıyoruz
tutar = float(input("Alışveriş tutarını giriniz: "))

# Fonksiyonu çağırıyoruz
sonuc = indirim_hesapla(tutar)

# Sonucu yazdırıyoruz
print("Ödenecek tutar:", sonuc, "TL")