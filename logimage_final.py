from random import randint

taille_max = 20

def creation_tableau(var1 = randint(5,taille_max) ,var2 = randint(5,taille_max)):
    tableau = [['O' for i in range(var1)]for i in range(var2)]
    for i in range(var2):
        for j in range(var1):
            r = randint(1,2)
            if r == 1:
                tableau[i][j] = 'X'
    return tableau

def compte_ligne(tab):
    rep = []
    n = 0
    for i in range(len(tab)):
        rep_inter = []
        for j in range(len(tab[0])):
            if tab[i][j] == 'X':
                n += 1
            elif tab[i][j] =='O'and n > 0:
                rep_inter.append(n)
                n = 0
        if n > 0:
            rep_inter.append(n)
            n = 0
        elif len(rep_inter) == 0:
            rep_inter.append(0)
        rep.append(rep_inter)
    return rep

def inver_col_lig(tab):
    tab_f = []
    for i in range(len(tab[0])):
        tab_inter = []
        for j in range(len(tab)):
            tab_inter.append(tab[j][i])
        tab_f.append(tab_inter)
    return tab_f