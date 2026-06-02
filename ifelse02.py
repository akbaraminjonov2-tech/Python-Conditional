a = float(input("1-son: "))
b = float(input("2-son: "))
amal = input("Amal: ")

if amal == "+":
    print(f"Natija: {a} + {b} = {a + b}")

if amal == "-":
    print(f"Natija: {a} - {b} = {a - b}")

if amal == "*":
    print(f"Natija: {a} * {b} = {a * b}")

if amal == "/":
    if b == 0:
        print("Nolga bo'lish mumkin emas!")
    else:
        print(f"Natija: {a} / {b} = {a / b}")

if amal != "+" and amal != "-" and amal != "*" and amal != "/":
    print("Noto'g'ri amal. Faqat +, -, *, / ishlatiladi.")
