#(2)
from MyModel import * #Summa as s 

a=int(input("Sisesta arv1: "))
b=int(input("Sisesta arv1: "))
c=int(input("Sisesta arv1: "))
bombom=Aritmetic(a,b,c)
print(bombom)
while True:
    try:
        aasta=int(input("Sisesta aasta number: "))
        break
    except:
        print("viga")
a=is_year_leap(aasta)
print(a)


While True:
    try:
        a=int(input("Sisesta"))
        break
    except:
        print("viga")
S,P,d=square(a)
print(f"S={s},P={p}, D={d}")

