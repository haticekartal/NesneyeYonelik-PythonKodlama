# UYGULAMA 7: Sayının karesini hesaplama

# Sayının karesini hesaplayan fonksiyon
def kare_al(sayi):
    sonuc = sayi * sayi
    print("Sayının karesi:", sonuc)

# Kullanıcıdan sayı alıyoruz
sayi = int(input("Bir sayı giriniz: "))

# Fonksiyonu çağırıyoruz
kare_al(sayi)