def inimeste_ja_palkage_lisamine (i:list,p:list,n=1)->any:
    """
    Funktsioon tagastab uuendatud loendi, kuslisatud inimesi ja palka
    :parem list i: Inimeste jarjend
    :param list p: palgate jarjend
    :param int n: inimese arv
    :rtype:list,list
    """
    if n>0:
        for j in range(n):
            nimi=input("Nimi: ").capitalize()
            palk=int(input("Palk "))
            i.append(nimi)
            p.append(palk)
    return i,p
    print()

def andmet_veerudes(i:list,p:list):
    """
    Funktsioon kuvab ekraanile kahe järjendite andmed veerudes
    :parem list i: Inimeste jarjend
    :param list p: palgate jarjend
    """
    for j in range(len(i)):
        print(i[j],"-",p[j])
    print()

def andmete_eemaldamine_nimi_jargi(i:list,p:list)->any:
    """
    Funktsioon kustutab andmeid ja tagastab listid.
    :parem list i: Inimeste jarjend
    :param list p: palgate jarjend
    :rtype:list,list
    """
    nimi=input("Keda kustutada ära(nimi)")
    for j in range(0,len(i)-1):
        if nimi in i:
            index=i.index(nimi)
            i.pop(index)
    return i,p
    print()

def kellel_on_suurim_palk(i:list,p:list)->any:
    """

    """
    nimed=[]
    nimi=1
    max_palk=max(p)
    ind=1
    for palk in p:
        if palk==max_palk:
            nimed=i[p.index(palk,ind)]
            nimed.append(nimi)
    return nimed

def kellel_on_väiksem_palk(i:list,p:list)->list:
    """
    Функция возвращает список имен сотрудников, у которых зарплата меньше порога.
    :param i: Список имен сотрудников
    :param p: Список зарплат сотрудников
    :param порог: Порог зарплаты
    :return: Список имен сотрудников с зарплатой меньше порога
    """
    palgad = []
    for nimi, зарплата in zip(i, p):
        if зарплата < palgalävi:
            palgad.append(nimi)
    return palgad
nimed = ["Алексей", "Мария", "Иван", "Екатерина"]
palgad = [1200,2500,750,395,1200]
palgalävi = 3000
väiksem_palk = kellel_on_väiksem_palk(nimed, palgad, palgalävi)
print("Сотрудники с зарплатой меньше", palgalävi, ":", väiksem_palk)
def sorteerimine(i:list,p:list)->any:
    """

    """
    for n in range(0,len(i)):
        for m in range(n,len(i)):
            if p[n]>p[m]:
                p[m],p[n]=p[n],p[m]
                i[m],i[n]=i[n],i[m]
    return i,p

def vordsed_palgad(i:list,p:list)->list:
    """
    """
    nimed=[]
    for id_, palgad in enumerate(p):
        print(id_,palgad)
    for palk in p:
        n=p.count(palk)
        ind=p.index(palk)
        if n>1:
            subnimed=[]
            for j in range(n):
                nimi=i[p.index(palk,ind)]
                subnimed.append(nimi)
                p.pop(ind)
                i.pop(ind)
                ind=+1
                nimed.append(subnimed)
    print(nimed)
