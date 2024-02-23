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

from math import *
def square(külg:float)->any:
    """
    """
    S=külg**2
    P=4*külg
    d=külg*sqrt(2)
    return S,P,d

from math import *
def season(a:int)->str:
    """
    """
    while True:
        if a>0 and a<13:
            break
        else:
            try:
                a=int(input("Ainult 1-12, Sisesta veel kord number: "))
            except:
                print("Vigaadnmedmetüübiga")
    if a>2 and a<6:
        s="kevad"
    elif a>5 and a<9:
        s="suvi"
    elif a>8 and a<12:
        s="kevad"
    else:
        s="talv"
return(s)