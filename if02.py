parol = input("Parol: ")

harf = False
raqam = False

for belgi in parol:
    if belgi.isalpha():
        harf = True
    if belgi.isdigit():
        raqam = True

if len(parol) >= 8 and harf and raqam:
    print("Parol qabul qilindi.")
else:
    print("Parol noto'g'ri. Kamida 8 belgi, 1 harf va 1 raqam bo'lishi kerak.")
