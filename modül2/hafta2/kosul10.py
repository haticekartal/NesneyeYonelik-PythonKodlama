# UYGULAMA 13: Şifrenin en az 8 karakter olup olmadığını kontrol etme

sifre = input("Bir şifre belirleyin: ")

if len(sifre) >= 8:
    print("Şifre uzunluğu uygun.")
else:
    print("Şifre en az 8 karakter olmalıdır.")