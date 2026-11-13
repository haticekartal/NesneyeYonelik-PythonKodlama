# UYGULAMA 6: Dört işlem hesaplama

# Toplama fonksiyonu
def topla(a, b):
    print("Toplam:", a + b)

# Çıkarma fonksiyonu
def cikar(a, b):
    print("Fark:", a - b)

# Çarpma fonksiyonu
def carp(a, b):
    print("Çarpım:", a * b)

# Bölme fonksiyonu
def bol(a, b):
    if b != 0:
        print("Bölüm:", a / b)
    else:
        print("Sıfıra bölme yapılamaz.")

# Fonksiyonları çağırıyoruz
topla(20, 5)
cikar(20, 5)
carp(20, 5)
bol(20, 5)