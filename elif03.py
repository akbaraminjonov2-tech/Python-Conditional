template = "{} soni {} ga bo'linadi"

n = int(input("Son: "))
 
if n % 2 == 0:
    print(template.format(n, 2))

if n % 3 == 0:
    print(template.format(n, 3))

if n % 5 == 0:
    print(template.format(n, 5))    
