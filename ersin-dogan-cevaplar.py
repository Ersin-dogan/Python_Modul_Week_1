######### ilk sorunun cevabı
for sayi in range(1,11):
    print(sayi)


#########// soru-2 cevabı
#for döngüsü
for sayi in range(0, 10 + 1, 2):
    print(sayi)

# while döngüsü
sayial = int(input("Bir sayı giriver : "))
basla = 2
while basla <= sayial:
    print(basla)
    basla += 2 


#########// soru-3 cevabı
ilksayi = input("Lütfen ilk sayıyı giriniz !")
ikincisayi = input("Lütfen ikinci sayıyı giriniz !")

for sayi in range(int(ilksayi), int(ikincisayi)+1):
    print(sayi)



#########// soru-4 cevabı
sayial = input("Lütfen bir sayı giriver: ")
if sayial % 2 == 0:
    print(f"{sayial} Girdiğin sayı çift sayıdır.")
else:
    print(f"{sayial} Girdiğin sayı tek sayıdır.")


#########// soru-5 cevabı
sayi = int(input("Lütfen pozitif bir tam sayı girin: "))
basla = 1 
if sayi < 0:
    print("Lütfen pozitif bir tam sayı girin.")
else:
    for i in range(1, sayi + 1):
        basla *= i
    print(f" {sayi} Faktöriyel: {basla}")


#########// soru-6 cevabı
sayial = int(input("Bir sayı giriniz: "))

if sayial <= 1:
    print(f"{sayial} bir asal sayı değildir.")
elif sayial == 2:
    print(f"{sayial} bir asal sayıdır.")
else:
    if sayial % 2 == 0:
        print(f"{sayial} bir asal sayı değildir.")
    else:
        asalmi = True
        for i in range(3, int(sayial ** 0.5) + 1, 2):
            if sayial % i == 0:
                asalmi = False
                break
        if asalmi:
            print(f"{sayial} bir asal sayıdır.")
        else:
            print(f"{sayial} bir asal sayı değildir.")


#########// soru-7 cevabı
limit = int(input("Bir limit giriniz: "))
fib_liste = [0, 1]
# Limit durumlarına göre liste atamaları
if limit == 0:
    fib_liste = [0]
elif limit == 1:
    fib_liste = [0, 1]
else:
    # Dizideki üçüncü elemandan başlayarak limit sayısına kadar Fibonacci hesaplaması
    for i in range(2, limit):
        next_fib = fib_liste[i - 1] + fib_liste[i - 2]
        fib_liste.append(next_fib)
# Hesaplanan Fibonacci buraya yazdır
print(fib_liste)


#########// soru-8 cevabı
metinal = input("Lütfen bir metin giriniz")
terscevir = metinal[::-1]
print(f"{terscevir}")



#########// soru-9 cevabı
kelimeal = input("Bir kelime giriniz: ").lower()
length = len(word)
is_palindrome = True
for i in range(length // 2):
    if word[i] != word[length - i - 1]:
        is_palindrome = False
        break
if is_palindrome:
    print(f"'{word}' bir palindromdur.")
else:
    print(f"'{word}' bir palindrom değildir.")


#########// soru-10 cevabı
agirlik = float(input("Kilonuzu girin (kg): "))
boy = float(input("Boyunuzu girin (metre cinsinden, örn: 1.75): "))
vki = agirlik / (boy ** 2)
if vki < 18.5:
    print(f"Vücut kitle indeksiniz: {vki:.2f}. Sonuç: Zayıf.")    
elif 18.5<= vki < 24.9:
    print(f"Vücut kitle indeksiniz: {vki:.2f}. Sonuç: Normal kilolu.")
elif 24.9<= vki < 29.9:
    print(f"Vücut kitle indeksiniz: {vki:.2f}. Sonuç: Fazla kilolu.")
elif 30 <= vki < 34.9:
    print(f"Vücut kitle indeksiniz: {vki:.2f}. Sonuç: 1.Derece Obezsiniz.")
elif 35 <= vki < 39.9:
    print(f"Vücut kitle indeksiniz: {vki:.2f}. Sonuç: 2.Derece Obezsiniz.")   
elif vki < 40:
    print(f"Vücut kitle indeksiniz: {vki:.2f}. Sonuç: 2.Derece Obezsiniz.")   


#########// soru-11 cevabı
sayi1 = int(input("Birinci sayıyı girin: "))
sayi2 = int(input("İkinci sayıyı girin: "))
sayi3 = int(input("Üçüncü sayıyı girin: "))
if sayi1 >= sayi2 and sayi1 >= sayi3:
    enbuyuk = sayi1
elif sayi2 >= sayi1 and sayi2 >= sayi3:
    enbuyuk = sayi2
else:
    enbuyuk = sayi3
print(f"En büyük sayı: {enbuyuk}")


#########// soru-12 cevabı
for i in range(1, 5):
    dersadi = input(f"{i}. dersin adını girin: ")
    arasinav = float(input(f"{dersadi} dersinin ara sınav notunu girin: "))
    finalsinav = float(input(f"{dersadi} dersinin final notunu girin: "))
    sonuc = (0.4 * arasinav) + (0.6 * finalsinav)
    if sonuc < 50:
        print(f"{dersadi} dersi: KALDI")
    else:
        print(f"{dersadi} dersi: GEÇTİ")


