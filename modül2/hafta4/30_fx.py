# UYGULAMA 9: Şifre kontrol sistemi

# Şifrenin uzunluğunu kontrol eden fonksiyon
def uzunluk_kontrol(sifre):

    return len(sifre) >= 8


# Şifrede rakam olup olmadığını kontrol ediyoruz
def rakam_kontrol(sifre):

    for karakter in sifre:

        if karakter.isdigit():
            return True

    return False


# Şifrede büyük harf olup olmadığını kontrol ediyoruz
def buyuk_harf_kontrol(sifre):

    for karakter in sifre:

        if karakter.isupper():
            return True

    return False


# Şifrenin güvenlik durumunu hesaplıyoruz
def sifre_kontrol(sifre):

    puan = 0

    if uzunluk_kontrol(sifre):
        puan += 1

    if rakam_kontrol(sifre):
        puan += 1

    if buyuk_harf_kontrol(sifre):
        puan += 1

    # Puan durumuna göre sonuç döndürüyoruz
    if puan == 3:
        return "Belirlenen kuralların tamamını sağlıyor."

    elif puan == 2:
        return "Belirlenen kurallardan ikisini sağlıyor."

    else:
        return "Belirlenen kuralların çoğunu sağlamıyor."


# Kullanıcıdan şifre alıyoruz
sifre = input("Şifre oluşturunuz: ")

# Şifreyi kontrol ediyoruz
sonuc = sifre_kontrol(sifre)

print("Şifre kontrol sonucu:", sonuc)