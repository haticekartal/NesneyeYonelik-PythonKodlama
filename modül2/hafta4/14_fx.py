# UYGULAMA 9: Sayının küpünü hesaplama

# Küp hesaplayan fonksiyon
def kup_al(sayi):
    return sayi ** 3

# Kullanıcıdan sayı alıyoruz
sayi = int(input("Bir sayı giriniz: "))

# Fonksiyonun sonucunu alıyoruz
sonuc = kup_al(sayi)

# Sonucu yazdırıyoruz
print("Sayının küpü:", sonuc)