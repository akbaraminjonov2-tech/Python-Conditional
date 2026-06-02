narx = 100
yosh = int(input("Yosh: "))

if yosh < 7:
    narx = 50
    print("Yakuniy narx: 50 so'm (50% chegirma qo'llanildi)")

if yosh >= 7 and yosh <= 17:
    narx = 80
    print("Yakuniy narx: 80 so'm (20% chegirma qo'llanildi)")

if yosh > 60:
    narx = 70
    print("Yakuniy narx: 70 so'm (30% chegirma qo'llanildi)")

if yosh >= 18 and yosh <= 60:
    print("Yakuniy narx: 100 so'm")