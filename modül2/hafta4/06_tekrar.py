# UYGULAMA: Kelimeyi ters çevirme ve palindrom kontrolü

kelime = input("Bir kelime giriniz: ")

ters = ""

for harf in kelime:
    ters = harf + ters

print("Kelimenin tersi:", ters)

if kelime == ters:
    print("Bu kelime palindromdur.")
else:
    print("Bu kelime palindrom değildir.")