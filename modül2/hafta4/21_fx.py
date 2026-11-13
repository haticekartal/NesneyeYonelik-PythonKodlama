# UYGULAMA 20: Girilen sayının asal olup olmadığını bulma

# Asal sayı kontrol fonksiyonu
def asal_mi(sayi):

    # 2'den küçük sayılar asal değildir
    if sayi < 2:
        return False

    # Sayının bölenlerini kontrol ediyoruz
    for bolen in range(2, sayi):

        if sayi % bolen == 0:
            return False

    # Bölen bulunmazsa sayı asaldır
    return True

# Kullanıcıdan sayı alıyoruz
sayi = int(input("Bir sayı giriniz: "))

# Fonksiyonu kontrol ediyoruz
if asal_mi(sayi):
    print("Bu sayı asaldır.")
else:
    print("Bu sayı asal değildir.")