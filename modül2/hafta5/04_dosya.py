# UYGULAMA 33: Python ile dosya silme

# os kütüphanesini ekliyoruz
import os

# Dosyanın varlığını kontrol ediyoruz
if os.path.exists("ogrenci.txt"):

    # Dosyayı siliyoruz
    os.remove("ogrenci.txt")

    print("Dosya silindi.")

else:
    print("Dosya bulunamadı.")