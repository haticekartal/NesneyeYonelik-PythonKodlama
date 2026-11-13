# UYGULAMA 26: Kitap yığını oluşturma

# Boş bir yığın oluşturalım
yigin = []

# Yığına kitapları ekleyelim
yigin.append("Python Kitabı")
yigin.append("Matematik Kitabı")
yigin.append("Yapay Zeka Kitabı")

# Yığının son halini gösterelim
print("Kitap yığını:", yigin)

# Son eklenen kitabı çıkaralım
cikan_kitap = yigin.pop()

print("Çıkarılan kitap:", cikan_kitap)

# Kalan kitapları gösterelim
print("Kalan kitaplar:", yigin)