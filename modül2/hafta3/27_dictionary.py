# UYGULAMA : Öğrencilerin sınav notlarını saklama

# Öğrenci adlarını ve notlarını tanımlayalım
notlar = {
    "Ayşe": 85,
    "Mehmet": 65,
    "Zeynep": 95,
    "Ahmet": 45
}

# Her öğrencinin notunu kontrol edelim
for ad, notu in notlar.items():

    # Öğrencinin notunu yazdıralım
    print("Öğrenci:", ad)
    print("Not:", notu)

    # Geçme durumunu kontrol edelim
    if notu >= 50:
        print("Durum: Geçti")
    else:
        print("Durum: Kaldı")

    print("------------------")