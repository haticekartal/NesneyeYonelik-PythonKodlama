# UYGULAMA 25: Banka hesabına para yatırma

# Global bakiye değişkeni
bakiye = 1000

# Para yatırma fonksiyonu
def para_yatir(miktar):

    global bakiye

    # Bakiyeyi artırıyoruz
    bakiye += miktar

    print("Güncel bakiye:", bakiye)

# Kullanıcıdan para miktarını alıyoruz
miktar = float(input("Yatırılacak tutarı giriniz: "))

# Fonksiyonu çağırıyoruz
para_yatir(miktar)