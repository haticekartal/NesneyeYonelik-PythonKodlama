# UYGULAMA 28: TXT dosyasının içeriğini okuma

# Dosyayı okuma modunda açıyoruz
dosya = open("bilgiler.txt", "r", encoding="utf-8")

# Dosyanın tamamını okuyoruz
icerik = dosya.read()

# İçeriği yazdırıyoruz
print(icerik)

# Dosyayı kapatıyoruz
dosya.close()