# UYGULAMA 17: Dikdörtgenin alanını ve çevresini hesaplama

# Alan ve çevre hesaplayan fonksiyon
def dikdortgen(kisa, uzun):

    alan = kisa * uzun
    cevre = 2 * (kisa + uzun)

    # İki sonucu birlikte döndürüyoruz
    return alan, cevre

# Fonksiyondan iki değeri alıyoruz
alan, cevre = dikdortgen(5, 10)

# Sonuçları yazdırıyoruz
print("Dikdörtgenin alanı:", alan)
print("Dikdörtgenin çevresi:", cevre)