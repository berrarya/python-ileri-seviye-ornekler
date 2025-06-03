                    ###Hesap Makinesi###

def toplama(a, b):
    return a + b

def cikarma(a, b):
    return a - b

def carpma(a, b):
    return a * b

def bolme(a, b):
    if b == 0:
        return "Bir sayıyı sıfıra bölemezsiniz!"
    return a / b

def menu():
    print("1. Toplama")
    print("2. Çıkarma")
    print("3. Çarpma")
    print("4. Bölme")

def calistir():
    menu()
    secim = input("Seçiminizi yapınız (1-4): ")
    a = float(input("Birinci sayıyı girin: "))
    b = float(input("İkinci sayıyı girin: "))

    if secim == "1":
        print("Sonuç:", toplama(a, b))
    elif secim == "2":
        print("Sonuç:", cikarma(a, b))
    elif secim == "3":
        print("Sonuç:", carpma(a, b))
    elif secim == "4":
        print("Sonuç:", bolme(a, b))
    else:
        print("Geçersiz seçim!")

calistir()
