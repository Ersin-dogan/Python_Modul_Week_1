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












