soat = int(input("Kun davomidagi vaqt: "))

if soat < 0 or soat > 23:
    print("Soat 0-23 oralig'ida bo'lishi kerak!")

if soat >= 5 and soat <= 11:
    print("Ertalab")

if soat >= 12 and soat <= 17:
    print("Kunduzi")

if soat >= 18 and soat <= 21:
    print("Kechqurun")

if (soat >= 22 and soat <= 23) or (soat >= 0 and soat <= 4):
    print("Tun")
