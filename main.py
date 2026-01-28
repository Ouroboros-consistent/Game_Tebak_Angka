import random
user = 0
end_msg = "SIKIL ISU (CUPU)"
jawaban = random.randint(1, 10)
i = 0

print("""
      SELAMAT DATANG DI GAME TEBAK ANGKA!!
      HMM AK PILIH ANGKA DIANTARA 1 SAMPAI 10 
      
      Pilih mode:
      1.MUUDDAH (10 Kali Percobaan)
      2.BIASA AJ (5 Kali Percobaan)
      3.ARGHHHH (3 Kali Percobaan)
      """)


tingkatkatan = int(input("Pilih tingkat kesulitan (Ketik Nomor): "))
if tingkatkatan == 1:
    percobaan = 10
elif tingkatkatan == 2:
    percobaan = 5
else:
    percobaan = 3


while i < percobaan:
    i += 1
    user = int(input("Masukkan angka!: "))
    if user > jawaban:
        print("jawaban anda lebih besar dari pada jawaban")
    elif user < jawaban:
        print("jawaban anda lebih kecil dari pada jawaban")
    elif jawaban == user :
        end_msg = "KAMU MENANG!!"
        break


print(end_msg)
print(f"PERCOBAAN: {i}")
