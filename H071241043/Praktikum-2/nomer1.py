#Menganalisis jenis segitiga

a = int(input("Masukkan panjang sisi a : "))
b = int(input("Masukkan panjang sisi b : "))
c = int(input("Masukkan panjang sisi c : "))

if a + b > c and a + c > b and b + c > a:
     if a == b == c:
        print("Segitiga sama sisi")

     elif a == b != c:
        print("Segitiga sama kaki")

     elif b == c != a:
        print("Segitiga sama kaki")

     elif c == a != b:
        print("Segitiga sama kaki")

     elif a != b != c:
        print("Segitiga sembarang")

else:
    print("Tidak dapat membentuk segitiga yang valid")