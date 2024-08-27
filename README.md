# Basit Hesap Makinesi

Bu depo, kullanıcıdan iki sayı ve bir işlem alarak toplama, çıkarma, çarpma veya bölme işlemlerini gerçekleştiren basit bir Python hesap makinesi içerir. Program, kullanıcının seçimine göre işlemi yapar ve sonucu ekrana yazdırır.

## Nasıl Çalışır?

Program aşağıdaki adımlarla çalışır:

1. **Sayıları Al**: Kullanıcıdan iki sayı girmesi istenir.
2. **İşlem Seç**: Kullanıcıya hangi işlemi yapmak istediği sorulur: toplama (+), çıkarma (-), çarpma (*) veya bölme (/).
3. **İşlemi Gerçekleştir**: Kullanıcının seçtiği işleme göre hesaplama yapılır.
4. **Sonucu Yazdır**: İşlemin sonucu ekrana yazdırılır.
5. **Geçersiz İşlem**: Eğer geçersiz bir işlem seçilirse, kullanıcıya hata mesajı verilir ve program sonlandırılır.

## Kod

```python
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
```