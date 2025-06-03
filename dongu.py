
                           #Sayı tahmin etme oyunu#
import random

sayi=random.randint(0,10)
hak=5

while hak>0:
    tahmin=int(input("0-10 arası bir sayı tahmin et: "))

    if tahmin==sayi:
        print("Doğru tahmin, tebrikler!")
        break 
    elif tahmin > sayi:
        print("Daha küçük bir sayı gir dostum.")
    else:
        print("Daha büyük bir sayı gir dostum.")
    hak-=1
if tahmin != sayi:
    print(f"Doğru sayı: {sayi} idi dostum") 

    