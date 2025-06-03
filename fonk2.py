                ##Not Sistemi##

ogrenciler = {}

def not_ekle(ad, notlar):
    ogrenciler[ad] = notlar

def ortalama_hesapla(ad):
    if ad in ogrenciler:
        return sum(ogrenciler[ad]) / len(ogrenciler[ad])
    else:
        return "Öğrenci bulunamadı."

def listele():
    for ad, notlar in ogrenciler.items():
        print(f"{ad} - Notlar: {notlar} - Ortalama: {ortalama_hesapla(ad):.2f}")

def baslat():
    not_ekle("Ali", [70, 85, 90])
    not_ekle("Ayşe", [88, 92, 80])
    not_ekle("Mehmet", [60, 75, 70])
    listele()

baslat()
