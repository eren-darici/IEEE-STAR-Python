x = float(input("Birinci sayı:"))
y = float(input("İkinci sayı:"))

islem = int(input("İşlem seçin: "))

print("1. Toplama")
print("2. Çıkartma")
print("Çıkmak için herhangi bir tuşa basınız.")

if islem == 1:
    print(x + y)
elif islem == 2:
    print(x - y)
else:
    print("çıkış")