import random


user = input("Masukkan angka!: ")
percobaan = 0
jawaban = random.randint(1, 10)
print(jawaban)

while jawaban != int(user):
    user = input("Masukkan angka!: ")


