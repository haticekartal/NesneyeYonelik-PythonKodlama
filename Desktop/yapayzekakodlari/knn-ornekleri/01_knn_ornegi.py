import math

# Meyve eğitim verileri
veriler = [
    [150, 7, "Elma"],
    [160, 8, "Elma"],
    [140, 7, "Elma"],
    [200, 9, "Portakal"],
    [210, 10, "Portakal"],
    [190, 9, "Portakal"]
]

# Yeni meyvenin özellikleri
yeni_meyve = [170, 8]

uzakliklar = []

# Her meyve ile yeni meyve arasındaki uzaklığı hesapla
for veri in veriler:

    uzaklik = math.sqrt(
        (yeni_meyve[0] - veri[0])**2 +
        (yeni_meyve[1] - veri[1])**2
    )

    uzakliklar.append([uzaklik, veri[2]])

# Uzaklıkları sırala
uzakliklar.sort()

# En yakın 3 komşuyu seç
k = 3
komsular = uzakliklar[:k]

# Sınıfları say
elma = 0
portakal = 0

for komsu in komsular:

    if komsu[1] == "Elma":
        elma += 1
    else:
        portakal += 1

# Sonucu yazdır
if elma > portakal:
    print("Tahmin: Elma")
else:
    print("Tahmin: Portakal")