import random

level = 1
ulang = "y"

while ulang == "y":
    print("Game Tebak Angka")
    print("Level :", level)

    if level == 1:
        batas = 10
        kesempatan = 3
    elif level == 2:
        batas = 20
        kesempatan = 42
    else:
        batas = 50
        kesempatan = 5

    angka = random.randint(1, batas)

    print("Tebak angka dari 1 sampai", batas)
    print("Kesempatan menebak:", kesempatan)

    for i in range(kesempatan):
        tebakan = int(input("Masukkan tebakan: "))

        if tebakan == angka:
            print("Tebakan benar")
            level = level + 1
            break
        elif tebakan < angka:
            print("Tebakan terlalu kecil")
        else:
            print("Tebakan terlalu besar")

    if tebakan != angka:
        print("Anda kalah")
        print("Angka yang benar adalah", angka)

    ulang = input("Main lagi? (y/t): ")

print("Program selesai")