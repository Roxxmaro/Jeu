from random import randint

taille_max = 5

def creation_tableau(var1 = randint(5,taille_max) ,var2 = randint(5,taille_max)):
#########################################
### fonction creation_tableau
# Cette fonction permet de préparer un tableau de jeu aléatoire.
# Chaque cellule est rempli au hasard, avec une chance sur 2 d'etre une croix.
# les dimensions sont définies par 2 variables : var1 et var2 (entre 5 et taille_max)
######
# sortie : la grille de jeu.
###
#########################################
    tableau = [['O' for i in range(var1)]for i in range(var2)]
    for i in range(var2):
        for j in range(var1):
            r = randint(1,2)
            if r == 1:
                tableau[i][j] = 'X'
    return tableau

def compte_ligne(tab):
#########################################
### fonction compte_ligne
# Cette fonction permet de compter les blocs de cases (en ligne)
# Un bloc de cases est une serie continue de cases remplies d'un 'X'
# (pour compter les blocs "colonnes", il faudra appeller cette fonction en inversant le tableau
######
# entrée : une grille de jeu (taille aléatoire)
# sortie : un tableau de comptage des blocs en ligne.
###
#########################################
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
#########################################
### fonction inver_col_lig
# Cette fonction permet d'inverser un tableau
# Les lignes passent en colonne et vice-versa
######
# entrée : une grille de jeu (taille aléatoire)
# sortie : la grille de jeu inversée.
###
#########################################
    tab_f = []
    for i in range(len(tab[0])):
        tab_inter = []
        for j in range(len(tab)):
            tab_inter.append(tab[j][i])
        tab_f.append(tab_inter)
    return tab_f