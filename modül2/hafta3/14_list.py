# UYGULAMA 22: Listeye eleman ekleme ve çıkarma

# Meyve listesi oluşturalım
meyveler = ["Elma", "Armut", "Muz"]

print("İlk liste:", meyveler)

# Listenin sonuna Çilek ekleyelim
meyveler.append("Çilek")

print("Eleman eklendi:", meyveler)

# Listenin ilk sırasına Kivi ekleyelim
meyveler.insert(0, "Kivi")

print("İlk sıraya eklendi:", meyveler)

# Armut elemanını silelim
meyveler.remove("Armut")

print("Eleman silindi:", meyveler)

# Son elemanı listeden çıkaralım
meyveler.pop()

print("Son eleman çıkarıldı:", meyveler)