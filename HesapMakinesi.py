sayi1 = float(input("İLK SAYIYI GİRİNİZ: "))
sayi2 = float(input("İKİNCİ SAYIYI GİRİNİZ: "))
islem = input("""Yapmak istediğiniz işlemi yazınız
+ : Toplama
- : Çıkarma
* : çarpma
/ : bölme
""")

if islem == "+" :
    print("Sonuç: ", str(sayi1 + sayi2))
    
elif islem == "-" :
    print("Sonuç: ", str(sayi1 - sayi2))
    
elif islem == "*" :
    print("Sonuç: ", str(sayi1 * sayi2))
    
elif islem == "/" :
    print("Sonuç: ", str(sayi1 / sayi2))
else:
    print("Yanlış işlem seçtiniz, program sonlandırıldı.")