from DEFfolder import *

palgad=[1200,2500,750,395,1200]
inimesed=["A","B","C","D","E"]

while True:
    print("Vali mida teha\n 0-print järjend\n 1-andmete lisamine\n 2-kustutada kedagi\n 3-kellel on suurim palk \n 4-kellel on väiksem palk \n 5-sorteeri palgat \n")
    valik=int(input())
    if valik==1:
        inimesed,palgad=inimeste_ja_palkage_lisamine(inimesed,palgad,int(input("Mitu inimest lisamine?")))
    elif valik==0:
        andmet_veerudes(inimesed,palgad)
    elif valik==2:
        andmete_eemaldamine_nimi_jargi(inimesed,palgad)
    elif valik==3:
        kellel_on_suurim_palk(inimesed,palgad)
    elif valik==4:
        kellel_on_väiksem_palk(inimesed,palgad)
    elif valik==5:
        sorteerimine(inimesed,palgad)