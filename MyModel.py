#(2)
from MyModel import Aritmetic, is_year_leap, square

a = int(input("Sisesta arv1: "))
b = int(input("Sisesta arv2: "))  # Ошибка второго ввода
c = int(input("Sisesta arv3: "))  # Ошибка третьего ввода
bombom = Aritmetic(a, b, c)
print(bombom)
while True:
    try:
        aasta = int(input("Sisesta aasta number: "))
        break
    except ValueError:  # Уточнение исключения
        print("Viga")
a = is_year_leap(aasta)
print(a)
while True:
    try:
        a = int(input("Sisesta külg: "))  # Перевод на эстонский
        break
    except ValueError:  # Уточнение исключения
        print("Viga")
S, P, d = square(a)
print(f"S={S}, P={P}, D={d}")  # Исправление переменных s и p на S и P

