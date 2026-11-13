# UYGULAMA 6: Kullanıcı adı ve şifreyi kontrol etme

kullanici_adi = input("Kullanıcı adınızı girin: ")
sifre = input("Şifrenizi girin: ")

if kullanici_adi == "admin" and sifre == "1234":
    print("Giriş başarılı.")
else:
    print("Kullanıcı adı veya şifre hatalı.")