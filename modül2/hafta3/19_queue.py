# UYGULAMA 28: Banka müşteri kuyruğu oluşturma

# Kuyruk veri yapısını içe aktaralım
from collections import deque

# Boş bir kuyruk oluşturalım
kuyruk = deque()

# Kuyruğa müşteri ekleyelim
kuyruk.append("Ayşe")
kuyruk.append("Mehmet")
kuyruk.append("Zeynep")

print("Bekleyen müşteriler:", kuyruk)

# İlk gelen müşteriyi çıkaralım
ilk_musteri = kuyruk.popleft()

print("İşlem yapılan müşteri:", ilk_musteri)

# Kalan müşterileri gösterelim
print("Kalan müşteriler:", kuyruk)