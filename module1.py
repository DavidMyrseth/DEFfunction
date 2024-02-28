# moodul.py

palgad = [1200, 2500, 750, 395, 1200]
inimesed = ["A", "B", "C", "D", "E"]

def lisa_uus(nimi, palk):
    inimesed.append(nimi)
    palgad.append(palk)

def eemalda_inimene(nimi):
    if nimi in inimesed:
        index = inimesed.index(nimi)
        inimesed.pop(index)
        palgad.pop(index)
    else:
        print("Sellist inimest ei leitud.")

def suurim_palk():
    max_palk = max(palgad)
    indeks = palgad.index(max_palk)
    return inimesed[indeks], max_palk

def vaikseim_palk():
    min_palk = min(palgad)
    indeks = palgad.index(min_palk)
    return inimesed[indeks], min_palk

def sorteeritud_palgad(kasvav=True):
    sorted_list = sorted(zip(palgad, inimesed))
    return sorted_list if kasvav else sorted_list[::-1]

def sama_palk(palk):
    sama_palkaga = [(inimesed[i], palgad[i]) for i in range(len(palgad)) if palgad[i] == palk]
    return len(sama_palkaga), sama_palkaga

def otsi_palk(nimi):
    return next((palk for i, palk in zip(inimesed, palgad) if i == nimi), "Sellist inimest ei leitud.")

def suuremad_kui(summa):
    return [(inimene, palk) for inimene, palk in zip(inimesed, palgad) if palk > summa]

def keskmise_palk():
    return sum(palgad) / len(palgad)

def top_palk():
    return sorted(zip(palgad, inimesed), reverse=True)[:5], sorted(zip(palgad, inimesed))[:5]

def keskmine_palk_jargmisel_aastal(aastad):
    return [round(palk * 1.05 ** aastad) for palk in palgad]

# main.py

from moodul import *

# Uue inimese lisamine
lisa_uus("F", 800)

# Inimese eemaldamine
eemalda_inimene("E")

# Suurima palga leidmine
print("Suurim palk:", suurim_palk())

# Väikseima palga leidmine
print("Väikseim palk:", vaikseim_palk())

# Sorteeritud palgad kasvavas järjekorras
print("Sorteeritud palgad kasvavas järjekorras:", sorteeritud_palgad())

# Sorteeritud palgad kahanevas järjekorras
print("Sorteeritud palgad kahanevas järjekorras:", sorteeritud_palgad(False))

# Inimeste arv, kes saavad teatud palga
print("Inimeste arv, kes saavad teatud palga:", sama_palk(1200))

# Inimese palga otsimine nime järgi
print("Inimese palk:", otsi_palk("D"))

# Inimeste arv, kes saavad rohkem kui teatud summa
print("Inimeste arv, kes saavad rohkem kui 1000:", suuremad_kui(1000))

# Keskmine palk
print("Keskmine palk:", keskmise_palk())

# Top 5 rikkamat ja vaesemat inimest
top_rich, top_poor = top_palk()
print("Top 5 rikkamat inimest:", top_rich)
print("Top 5 vaesemat inimest:", top_poor)

# Inimeste palgad 5 aasta pärast
print("Inimeste palgad 5 aasta pärast:", keskmine_palk_jargmisel_aastal(5))

