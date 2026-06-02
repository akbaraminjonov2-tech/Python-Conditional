import os

fayl_nomi = input("Fayl: ")

if os.path.exists(fayl_nomi):
    print(f"Fayl '{fayl_nomi}' mavjud.")
else:
    print(f"Fayl '{fayl_nomi}' topilmadi.")
