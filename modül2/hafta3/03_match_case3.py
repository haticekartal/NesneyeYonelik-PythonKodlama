# UYGULAMA : Restoranda seçilen ürünün fiyatını bulma

print("----- YEMEK MENÜSÜ -----")
print("1 - Hamburger: 150 TL")
print("2 - Pizza: 200 TL")
print("3 - Makarna: 120 TL")
print("4 - Salata: 90 TL")

secim = int(input("Sipariş numarasını giriniz: "))

match secim:

    case 1:
        print("Hamburger seçildi.")
        print("Ödenecek tutar: 150 TL")

    case 2:
        print("Pizza seçildi.")
        print("Ödenecek tutar: 200 TL")

    case 3:
        print("Makarna seçildi.")
        print("Ödenecek tutar: 120 TL")

    case 4:
        print("Salata seçildi.")
        print("Ödenecek tutar: 90 TL")

    case _:
        print("Menüde böyle bir ürün bulunmuyor.")