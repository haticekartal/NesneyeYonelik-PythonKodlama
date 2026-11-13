# UYGULAMA 6: Global değişkenlerle banka hesabı

# Global bakiye değişkeni
bakiye = 2000


# Para yatırma fonksiyonu
def para_yatir(miktar):

    global bakiye

    if miktar > 0:

        bakiye += miktar

        print("Para yatırma başarılı.")

    else:
        print("Geçersiz miktar.")


# Para çekme fonksiyonu
def para_cek(miktar):

    global bakiye

    if miktar <= 0:
        print("Geçersiz miktar.")

    elif miktar > bakiye:
        print("Yetersiz bakiye.")

    else:

        bakiye -= miktar

        print("Para çekme başarılı.")


# Bakiye gösterme fonksiyonu
def bakiye_goster():

    print("Güncel bakiyeniz:", bakiye, "TL")


# Menüyü gösteren fonksiyon
def menu():

    print("\n--- BANKA İŞLEMLERİ ---")
    print("1 - Para yatır")
    print("2 - Para çek")
    print("3 - Bakiye sorgula")
    print("4 - Çıkış")


# Ana program
while True:

    menu()

    secim = input("Seçiminiz: ")

    if secim == "1":

        miktar = float(input("Yatırılacak miktar: "))

        para_yatir(miktar)

    elif secim == "2":

        miktar = float(input("Çekilecek miktar: "))

        para_cek(miktar)

    elif secim == "3":

        bakiye_goster()

    elif secim == "4":

        print("İyi günler.")
        break

    else:
        print("Geçersiz seçim.")