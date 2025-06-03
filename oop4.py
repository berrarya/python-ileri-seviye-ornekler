                    ##Araç Takip Sistemi##

class Arac:
    def __init__(self, marka, model, hiz=0):
        self.marka = marka
        self.model = model
        self.hiz = hiz

    def hizlan(self, miktar):
        self.hiz += miktar
        print(f"{self.marka} {self.model} {miktar} km/h hızlandı. Yeni hız: {self.hiz} km/h")

    def yavasla(self, miktar):
        self.hiz = max(0, self.hiz - miktar)
        print(f"{self.marka} {self.model} {miktar} km/h yavaşladı. Yeni hız: {self.hiz} km/h")

    def bilgi(self):
        return f"{self.marka} {self.model} - {self.hiz} km/h"

class Otomobil(Arac):
    def korna_cal(self):
        print(f"{self.marka} {self.model}: Bip bip!")

class Kamyon(Arac):
    def korna_cal(self):
        print(f"{self.marka} {self.model}: HONK HONK!")

# Kullanım
a1 = Otomobil("Toyota", "Corolla")
a2 = Kamyon("Mercedes", "Actros")

a1.hizlan(50)
a2.hizlan(40)
a1.korna_cal()
a2.korna_cal()
print(a1.bilgi())
print(a2.bilgi())
