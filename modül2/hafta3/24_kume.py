# UYGULAMA 37: İki kursa da katılan öğrencileri bulma

# Python kursuna katılan öğrenciler
python_kursu = {"Ayşe", "Mehmet", "Ali", "Zeynep"}

# Yapay zeka kursuna katılan öğrenciler
yapay_zeka_kursu = {"Ayşe", "Ali", "Fatma", "Ahmet"}

# İki kursa da katılan öğrenciler
ortak = python_kursu.intersection(yapay_zeka_kursu)

# En az bir kursa katılan bütün öğrenciler
tum_ogrenciler = python_kursu.union(yapay_zeka_kursu)

# Sadece Python kursunda bulunan öğrenciler
sadece_python = python_kursu.difference(yapay_zeka_kursu)

print("Ortak öğrenciler:", ortak)
print("Tüm öğrenciler:", tum_ogrenciler)
print("Sadece Python kursundakiler:", sadece_python)