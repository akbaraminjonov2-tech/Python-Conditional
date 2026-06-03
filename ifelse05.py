vazn = float(input("Vazn (kg): "))
boy = float(input("Bo'y (m): "))

bmi = vazn / (boy ** 2)

if bmi < 18.5:
    print("Kam vazn")

if bmi >= 18.5 and bmi < 25:
    print("Normal vazn")

if bmi >= 25 and bmi < 30:
    print("Ortiqcha vazn")

if bmi >= 30:
    print("Semizlik")
