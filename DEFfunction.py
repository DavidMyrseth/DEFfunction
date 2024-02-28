def aritmetic(arv1:int,arv2:int,sümbol:str)->int:
    if sümbol=="+":
        s=arv1+arv2
    elif sümbol=="-":
        s=arv1-arv2
    elif sümbol=="*":
        s=arv1*arv2
    elif sümbol=="/":
        s=arv1/arv2
    else:
        s="Неизвестная операция"
    return s

def is_year_leap(aasta: int)->bool:
    """Functioon otsustab  kas aasta on liigaasta või ei ole.
    Tagastad True kui aasta on liigaasta ja False kui on tavaline aasta.
    Tagastad True kui aasta on liipaasta ja False kui aasta on tavaline aasta.

    parem int aasta: Aasta sisestab kasutaja
    rtype: bool
    """
    if aasta==0 and aasta%4==0 and aasta%100!=0:
        return
    else:
        return False

#3
from math import *
def square(külg:float)->any:
    """
    """
    S=külg**2
    P=4*külg
    d=külg*sqrt(2)
    return S,P,d

#4
def aastaaeg(kuu: int) -> str:
    while True:
        if 1 <= kuu <= 12:
            break
        else:
            try:
                kuu = int(input("Sisestage kuu number 1-12: "))
            except ValueError:
                print("Vale sisend, proovige uuesti.")
    if 3 <= kuu <= 5:
        aeg = "kevad"
    elif 6 <= kuu <= 8:
        aeg = "suvi"
    elif 9 <= kuu <= 11:
        aeg = "sügis"
    else:
        aeg = "talv"
    return aeg
kuu = int(input("Sisestage kuu number: "))
print("Aasta aeg on:", aastaaeg(kuu))

#5
def bank(a, years):
    total = a   # начальная сумма вклада
    for i in range(years):
        total += total * 0.1   # добавляем 10% к текущей сумме
    return total
initial_deposit = float(input("Введите сумму вклада: "))
deposit_years = int(input("Введите срок вклада в годах: "))
result = bank(initial_deposit, deposit_years)
print("Сумма на счету пользователя через", deposit_years, "лет будет:", result, "евро")

#6
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True
number = int(input("Введите число от 0 до 1000: "))
if is_prime(number):
    print(number, "является простым числом")
else:
    print(number, "не является простым числом")

#7
def is_valid_date(day, month, year):
    if year < 1 or month < 1 or month > 12:  # Проверяем условия корректности даты
        return False
    if month in [1, 3, 5, 7, 8, 10, 12]:  # Проверка на количество дней в месяце
        return 1 <= day <= 31
    elif month in [4, 6, 9, 11]:
        return 1 <= day <= 30
    elif month == 2:
        # Проверка на високосный год
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            return 1 <= day <= 29
        else:
            return 1 <= day <= 28
    else:
        return False
day = int(input("Введите день: "))
month = int(input("Введите месяц: "))
year = int(input("Введите год: "))
if is_valid_date(day, month, year):
    print("Да, такая дата существует.")
else:
    print("Нет, такой даты не существует.")

#8
def XOR_cipher(text, key):
    return ''.join(chr(ord(char) ^ key) for char in text)
def XOR_uncipher(encrypted_text, key):
    return ''.join(chr(ord(char) ^ key) for char in encrypted_text)
text = input("Введите строку для шифрования: ")
key = int(input("Введите ключ шифрования (целое число): "))
encrypted_text = XOR_cipher(text, key)
print("Зашифрованная строка:", encrypted_text)
decrypted_text = XOR_uncipher(encrypted_text, key)
print("Расшифрованная строка:", decrypted_text)

