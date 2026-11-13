# UYGULAMA 22: Global değişkene fonksiyon içinden erişme

# Fonksiyon dışında tanımlanan değişken
mesaj = "Python öğreniyorum"

# Fonksiyon tanımlıyoruz
def mesaj_yaz():

    # Global değişkeni okuyoruz
    print(mesaj)

# Fonksiyonu çağırıyoruz
mesaj_yaz()

# Global değişkene fonksiyon dışında da erişebiliyoruz
print(mesaj)




# UYGULAMA 23: Global ve yerel değişkenlerin karşılaştırılması

# Global değişken
sayi = 100

def goster():

    # Fonksiyon içinde aynı isimle yerel değişken tanımlıyoruz
    sayi = 20

    print("Fonksiyon içindeki sayı:", sayi)

# Fonksiyonu çağırıyoruz
goster()

# Global değişken değişmez
print("Fonksiyon dışındaki sayı:", sayi)