# UYGULAMA 3: Kullanıcının ismini alıp selamlama

# Fonksiyon tanımlama
def merhaba_de(isim):
    print("Hoş geldin", isim)

# Kullanıcıdan isim alıyoruz
ad = input("Adınızı giriniz: ")

# Kullanıcıdan aldığımız ismi fonksiyona gönderiyoruz
merhaba_de(ad)