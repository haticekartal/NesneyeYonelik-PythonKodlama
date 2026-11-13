# UYGULAMA 26: Yeni bir metin dosyası oluşturma

# x modu dosya yoksa yeni dosya oluşturur
dosya = open("bilgiler.txt", "x", encoding="utf-8")

# Dosyayı kapatıyoruz
dosya.close()

print("Dosya oluşturuldu.")

# UYGULAMA 27: TXT dosyasına bilgi yazma

# Dosyayı yazma modunda açıyoruz
dosya = open("bilgiler.txt", "w", encoding="utf-8")

# Dosyaya metin yazıyoruz
dosya.write("Python programlama dersine hoş geldiniz.\n")

dosya.write("Bugün dosya işlemlerini öğreniyoruz.")

# Dosyayı kapatıyoruz
dosya.close()

print("Bilgiler dosyaya kaydedildi.")
