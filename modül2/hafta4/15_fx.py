# UYGULAMA 10: Tek ve çift sayı kontrolü

# Sayıyı kontrol eden fonksiyon
def tek_cift(sayi):

    # Sayının 2'ye bölümünden kalan sıfırsa çifttir
    if sayi % 2 == 0:
        print("Bu sayı çifttir.")
    else:
        print("Bu sayı tektir.")

# Kullanıcıdan sayı alıyoruz
sayi = int(input("Bir sayı giriniz: "))

# Fonksiyonu çağırıyoruz
tek_cift(sayi)