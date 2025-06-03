                        ##ONLINE SİPARİŞ SİSTEMİ##

class Urun:
    def __init__(self, ad, fiyat):
        self.ad = ad
        self.fiyat = fiyat

    def bilgi(self):
        return f"{self.ad}: {self.fiyat} TL"

class Sepet:
    def __init__(self):
        self.urunler = []

    def urun_ekle(self, urun, adet=1):
        self.urunler.append((urun, adet))
        print(f"{adet} adet '{urun.ad}' sepete eklendi.")

    def toplam_tutar(self):
        toplam = sum(u.fiyat * a for u, a in self.urunler)
        return toplam

    def sepeti_goster(self):
        print("Sepetiniz:")
        for urun, adet in self.urunler:
            print(f"- {urun.ad} x{adet} = {urun.fiyat * adet} TL")
        print(f"Toplam: {self.toplam_tutar()} TL")

# Kullanım
u1 = Urun("Laptop", 15000)
u2 = Urun("Mouse", 500)
u3 = Urun("Klavye", 1000)

sepet = Sepet()
sepet.urun_ekle(u1, 1)
sepet.urun_ekle(u2, 2)
sepet.urun_ekle(u3, 1)
sepet.sepeti_goster()
