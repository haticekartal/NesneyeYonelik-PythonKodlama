# UYGULAMA : Doğru şifre girilene kadar tekrar isteme

# Doğru şifreyi belirleyelim
dogru_sifre = "1234"

while True:

    # Kullanıcıdan şifre alalım
    sifre = input("Şifrenizi giriniz: ")

    # Şifre doğruysa döngüyü bitirelim
    if sifre == dogru_sifre:
        print("Giriş başarılı!")
        break

    # Şifre yanlışsa tekrar isteyelim
    else:
        print("Hatalı şifre! Tekrar deneyiniz.")