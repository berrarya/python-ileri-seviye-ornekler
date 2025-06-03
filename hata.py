def bolme_islemi():
    try:
        sayi1 = int(input("Birinci sayıyı girin: "))
        sayi2 = int(input("İkinci sayıyı girin: "))
        
        sonuc = sayi1 / sayi2
        print(f"{sayi1} / {sayi2} = {sonuc}")

    except ValueError:
        print("HATA: Lütfen yalnızca sayı girin!")
    
    except ZeroDivisionError:
        print("HATA: Bir sayıyı sıfıra bölemezsiniz!")

    except Exception as e:
        print(f"Beklenmeyen bir hata oluştu: {e}")

    finally:
        print("İşlem tamamlandı. Teşekkürler!")

bolme_islemi()
