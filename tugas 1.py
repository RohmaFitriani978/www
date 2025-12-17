tinggi = int(input("masukkan tinggi segitiga: "))
character = input("masukkan karakter: ")

for i in range(1, tinggi + 1):
    print(" " * (tinggi - i) + character * (2*1 - i))