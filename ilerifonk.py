from functools import reduce
import time

#Decorator: Fonksiyon çalışma süresini ölçer
def zaman_olcucu(func):
    def wrapper(*args, **kwargs):
        basla = time.time()
        sonuc = func(*args, **kwargs)
        bitir = time.time()
        print(f"'{func.__name__}' çalışması {bitir - basla:.4f} saniye sürdü.")
        return sonuc
    return wrapper

#Generator: Notları tek tek döndürür 
def not_generator(ogrenci_listesi):
    for ogrenci in ogrenci_listesi:
        yield ogrenci["not"]


ogrenciler = [
    {"isim": "Ali", "not": 75},
    {"isim": "Ayşe", "not": 90},
    {"isim": "Mehmet", "not": 60},
    {"isim": "Zeynep", "not": 95},
    {"isim": "Ahmet", "not": 50},
]

#Map: Öğrenci ismi ve notunu biçimlendir
@zaman_olcucu
def not_listesi(ogr_list):
    return list(map(lambda o: f"{o['isim']} - {o['not']}", ogr_list))

#Filter: 70 üzeri olanlar
@zaman_olcucu
def basarili_ogrenciler(ogr_list):
    return list(filter(lambda o: o["not"] >= 70, ogr_list))

#Reduce: Ortalama hesaplama
@zaman_olcucu
def ortalama_hesapla(ogr_list):
    notlar = list(map(lambda o: o["not"], ogr_list))
    return reduce(lambda x, y: x + y, notlar) / len(notlar)


print("Öğrenci Listesi:")
print(*not_listesi(ogrenciler), sep="\n")

print("\nBaşarılı Öğrenciler (>= 70):")
for ogr in basarili_ogrenciler(ogrenciler):
    print(f"{ogr['isim']} - {ogr['not']}")

print("\nSınıf Ortalaması:")
print(f"Ortalama Not: {ortalama_hesapla(ogrenciler):.2f}")

print("\nGenerator ile notlar:")
for n in not_generator(ogrenciler):
    print(f"Not: {n}")
