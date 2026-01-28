import random


user = int(input("Masukkan angka!: "))
percobaan = 0
jawaban = random.randint(1, 10)
print(jawaban)

while jawaban != user:
    if user > jawaban:
        print("jawaban anda lebih besar dari pada jawaban")
    if user < jawaban:
        print("jawaban anda lebih kecil dari pada jawaban")
    user = int(input("Masukkan angka!: "))

print("kamu menang!!!")

