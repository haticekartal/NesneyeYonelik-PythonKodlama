# UYGULAMA 13: Ürünün KDV dahil fiyatını hesaplama

# KDV hesaplama fonksiyonu
def kdv_hesapla(fiyat):
    kdv = fiyat * 0.20
    toplam = fiyat + kdv
    return toplam

# Ürün fiyatını alıyoruz
fiyat = float(input("Ürün fiyatını giriniz: "))

# KDV dahil fiyatı hesaplıyoruz
sonuc = kdv_hesapla(fiyat)

# Sonucu yazdırıyoruz
print("KDV dahil fiyat:", sonuc, "TL")