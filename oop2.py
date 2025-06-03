                            ##Banka Sistemi##

class Hesap:
    def __init__(self, ad, bakiye=0):
        self.ad = ad
        self.bakiye = bakiye

    def para_yatir(self, miktar):
        self.bakiye += miktar
        print(f"{self.ad} hesabına {miktar} TL yatırıldı. Yeni bakiye: {self.bakiye} TL")

    def para_cek(self, miktar):
        if miktar > self.bakiye:
            print("Yetersiz bakiye!")
        else:
            self.bakiye -= miktar
            print(f"{self.ad} hesabından {miktar} TL çekildi. Yeni bakiye: {self.bakiye} TL")

    def bakiye_goster(self):
        print(f"{self.ad} hesabının güncel bakiyesi: {self.bakiye} TL")

class VadeliHesap(Hesap):
    def __init__(self, ad, bakiye, faiz_orani):
        super().__init__(ad, bakiye)
        self.faiz_orani = faiz_orani

    def faiz_ekle(self):
        faiz = self.bakiye * self.faiz_orani / 100
        self.bakiye += faiz
        print(f"{self.ad} hesabına {faiz} TL faiz eklendi. Yeni bakiye: {self.bakiye} TL")

# Kullanım
h1 = Hesap("Ali", 500)
h1.bakiye_goster()
h1.para_yatir(200)
h1.para_cek(100)

print()

h2 = VadeliHesap("Ayşe", 1000, 10)
h2.faiz_ekle()
h2.bakiye_goster()
