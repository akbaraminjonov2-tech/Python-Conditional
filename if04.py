balans = 5000
summa = int(input("Summa: "))

if summa < 0:
    print("Manfiy summa kiritib bo'lmaydi.")

elif summa <= balans:
    print(f"Pul yechildi. Qolgan balans: {balans - summa} so'm")

else:
    print("Mablag' yetarli emas. Sizning balansingiz: 5000 so'm")
