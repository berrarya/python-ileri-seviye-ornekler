                ##Asal Sayı##

def asal_mi(sayi):
    if sayi < 2:
        return False
    for i in range(2, int(sayi ** 0.5) + 1):
        if sayi % i == 0:
            return False
    return True

def asal_listele(n):
    asal_sayilar = []
    for i in range(2, n + 1):
        if asal_mi(i):
            asal_sayilar.append(i)
    return asal_sayilar

def asal_toplam(n):
    return sum(asal_listele(n))

def calistir():
    n = int(input("Kaça kadar olan asal sayılar listelensin? "))
    liste = asal_listele(n)
    print("Asal Sayılar:", liste)
    print("Toplamları:", asal_toplam(n))

calistir()
