                ##Kütüphane Sistemi##

class Kitap:
    def __init__(self, baslik, yazar, yil):
        self.baslik = baslik
        self.yazar = yazar
        self.yil = yil

    def bilgi(self):
        return f"{self.baslik} - {self.yazar} ({self.yil})"

class Kutuphane:
    def __init__(self):
        self.kitaplar = []

    def kitap_ekle(self, kitap):
        self.kitaplar.append(kitap)
        print(f"Kitap eklendi: {kitap.bilgi()}")

    def kitaplari_listele(self):
        if not self.kitaplar:
            print("Kütüphanede kitap yok.")
        else:
            for kitap in self.kitaplar:
                print(kitap.bilgi())

    def kitap_ara(self, kelime):
        print(f"'{kelime}' kelimesi ile arama sonuçları:")
        for kitap in self.kitaplar:
            if kelime.lower() in kitap.baslik.lower() or kelime.lower() in kitap.yazar.lower():
                print(kitap.bilgi())

# Kullanım
k = Kutuphane()
k.kitap_ekle(Kitap("Simyacı", "Paulo Coelho", 1988))
k.kitap_ekle(Kitap("1984", "George Orwell", 1949))
k.kitap_ekle(Kitap("Kürk Mantolu Madonna", "Sabahattin Ali", 1943))

k.kitaplari_listele()
print()
k.kitap_ara("orwell")
