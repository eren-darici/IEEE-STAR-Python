sayi = int(input("Bir sayı giriniz:"))

if (sayi % 2 == 0) and (sayi > 0):
    print("Bu sayı çifttir.")
elif (sayi % 2 != 0) and (sayi > 0):
    print("Bu sayı tektir.")
else:
    print("{}, sıfır veya negatiftir.".format(sayi))
