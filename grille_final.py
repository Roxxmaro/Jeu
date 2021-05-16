import tkinter as tk
from logimage_final import*


def jouer():
#########################################
### fonction jouer
# Cette fonction est appellée au lancement du jeu. C'est elle qui initialise l'ensemble des données
# tableau = grille "modele" sur laquelle le programme va calculer les énoncés proposés au joueur.
#           la taille est aléatoire entre 5 et x (max parametrée dans l'exemple = 15)
#           Il pourra y avoir plusieurs réponses répondant à l'énoncé.
# enonce_ab : le tableau de l'"énoncé" des abscisses.
# enonce_orr : le tableau de l'"énoncé"  des ordonnées
# grille_joueur : grille qui sera remplie au fur et a mesure par le joueur.
######
# entrée :
# sortie : les variables sont des globales.
###
#########################################
    global app,tableau,enonce_ab,enonce_orr,grille_joueur

    tableau = creation_tableau()
    enonce_ab = compte_ligne(tableau)
	#enonce_ab = [[2,3],[3],[1],[4],[3,1]
    enonce_orr = compte_ligne(inver_col_lig(tableau))
	#enonce_orr = [[3,1],[1,1,1],[2],[3,1],[2]]
    grille_joueur = [[' ' for i in range(len(enonce_orr))]for i in range(len(enonce_ab))]
    app = Fenetre()
    app.resizable(width=False,height=False)
    app.mainloop()

def verif():
#########################################
### fonction verif
# Cette fonction est appellée pour vérifier la solution proposée par le joueur.
# Elle n'est activée que si toutes les cases sont remplies (plus d'espace présents)
#	(dans le jeu, il faut que toutes les cases soient remplies pour pouvoir dire que la solution soit bonne.
# Il peut y avoir plusieurs solutions répondant à l'énoncé.
# Le message de succès (/l'echec) est affiché dans une petite pop up et permet de relancer le jeu.
######
# entrée : les variables sont des globales.
# sortie : les variables sont des globales.
###
#########################################

    if chaine_2_grille(grille_joueur) == True:
        # On peut controler, car toutes les cases sont remplies)
        pop_up = tk.Toplevel()
        if compte_ligne(grille_joueur) == enonce_ab and enonce_orr == compte_ligne(inver_col_lig(grille_joueur)):
            tk.Label(pop_up, text = 'BRAVO tu as gagné',width=20).grid(row=0,column=0,columnspan=2)
        else:
            tk.Label(pop_up, text = 'DOMMAGE tu as perdu',width=20).grid(row=0,column=0,columnspan=2)
        tk.Button(pop_up, text='rejouer', command=rejouer,width=10).grid(row=1,column=0)
        tk.Button(pop_up, text='quitter', command=quitter,width=10).grid(row=1,column=1)

def rejouer():
#########################################
### fonction rejouer
# Cette fonction relance une grille de jeu, apres avoir libéré la mémoire de la précédente grille.
######
###
#########################################
    app.destroy()
    jouer()

def quitter():
#########################################
### fonction quitter
# Cette fonction permet de quitter le jeu apres avoir libéré la mémoire de la précédente grille.
######
###
#########################################
    app.destroy()

def chaine_2_grille(grille):
#########################################
### fonction chaine_2_grille
# Cette fonction compte combien d'espace il reste dans la grille (c'est à dire combien de cases sans réponse).
######
# entrée : grille remplie par le joueur
# sortie : True  si toutes les cases sont remplies
#########################################
#renvoie sous forme de chaine de caractere :
    n = 0
    for i in range(len(grille)):
        for j in range(len(grille[i])):
            if grille[i][j] == ' ':
                n += 1
    if n == 0:
        return True

class Fenetre(tk.Tk):
#########################################
### classe permet de gérer la fenetre de jeu.
# L'écran est décomposé en différentes zones.
# La grille de jeu est un ensemble de "boutons", dont le texte contient ses coordonnées et sa valeur
#########################################
    def __init__(self):
        tk.Tk.__init__(self)
        self.MaFenetre()

#########################################
### fonction qui structure la fenetre, voir les caracteristiques :
#########################################
# en haut : (row =0)
#   à gauche : bouton "valider" (column = 0)
#   à droite : énoncé des blocs colonnes (column = 1)
# au centre : (row =1)
#   à gauche : enoncé des blocs lignes (column = 0)
#   à droite : grille que le joueur doit remplir (column = 1)
# en bas : lire les dimensions du tableau (row =2, column =1)
#########################################
    def MaFenetre(self):
        grille = self.grille()
        grille.grid(row=1, column=1,padx=10)
        abscisse = self.abscisse()
        abscisse.grid(row=0, column=1)
        ordonnee = self.ordonnee()
        ordonnee.grid(row=1, column=0,padx=10)
        tk.Button(self, text='valider', command=verif).grid(row=0, column=0,padx=10)
        tk.Label(self, text=f'nombre de lignes : {len(enonce_orr)} , nombre de colonnes : {len(enonce_ab)}').grid(column=1,row=2,pady=5)

#########################################
### fonction qui prepare la grille du joueur.
# La grille est un tableau de boutons.
# Pour pouvoir retrouver la place du "bouton", on met dans le texte du bouton ses coordonnées et la valeur.
# Le texte est "caché" car la couleur du texte de la cellule et la meme que la couleur de fond.
# Chaque valeur est séparée par des ",".
# On pourra spliter le texte pour récupérer chacune des valeurs : ligne,colonne,valeur.
#####
# Signification des valeurs
#      le caractere "/" ==> Le joueur est sur qu'il n'y a rien, case =rouge
#      le caractere "X" ==> Le joueur est sur qu'il y a qq chose, case =noir
#      le caractere " " (espace) ==> Le joueur ne sait pas,case =blanche
#########################################

    def grille(self):
#Cette fonction permet d'afficher la grille
        grille = tk.Frame(self)
        for r in range(len(enonce_ab)):
            for c in range(len(enonce_orr)):
                btn = Bouton(grille, text = f'{r},{c}, ' , width=5, height=1,bg='white',fg='white')
                btn['command'] = btn.cliquer
                btn.grid(row=r, column=c)
        return grille
#########################################
### fonction qui prepare la zone d'affichage de l'énoncé des lignes.
#####
#########################################
    def ordonnee (self):
        ordonnee = tk.Frame(self)
        for a in range (len(enonce_ab)):
            n_ordonnee = tk.Label(ordonnee, text = enonce_ab[a])
            n_ordonnee.grid (row=a, column=0, pady= 9)

        return ordonnee

#########################################
### fonction qui prepare la zone d'affichage de l'énoncé des colonnes
#####
#########################################

    def abscisse (self): #Cette fonction permet d'afficher les enoncés colonnes
        abscisse = tk.Frame(self)
        for c in range(len(enonce_orr)):
            t = enonce_orr[c]
            final = ''
            for i in range(len(t)):
                final += str(t[i]) + '\n'
            n_abscisse = tk.Label(abscisse, text = final)
            n_abscisse.grid(row = 0, column=c , padx= 27)
        return abscisse

class Bouton(tk.Button):
#########################################
### class permet de gérer les opérations de click faites sur les boutons
#########################################

#########################################
### fonction qui formate le bouton sur lequel le joueur a cliqué.
# On "cache" les informations en mettant le texte du bouton dans la meme couleur que le fond du bouton.
# le bouton passe successivement de "ne sait pas", à coché (= sur qu'il y a qq chose), à coché (= sur qu'il n'y a rien)
######
# entrée : le bouton
# sortie : le bouton "modifié" suite au click
###
#########################################

    def cliquer(self):
            #/ ==> Le joueur est sur qu'il n'y a rien, case =rouge
            #X ==> Le joueur est sur qu'il y a qq chose, case =noir
            #  ==> Le joueur ne sait pas,case =blanche
        coordonees = self['text'].split(',')
        click_ord = coordonees[0]
        click_abs = coordonees[1]
        valeur = coordonees[2]
        if valeur == ' ':
            valeur = 'X'
            self['bg'] = 'black'
            self['fg'] = 'black'
        elif valeur == 'X':
             valeur = 'O'
             self['bg'] = 'red'
             self['fg'] = 'red'
        else:
            valeur = ' '
            self['bg'] = 'white'
            self['fg'] = 'white'
        self['text'] = f'{click_ord},{click_abs},{valeur}'
        grille_joueur[int(click_ord)][int(click_abs)] = valeur

if __name__ == "__main__":
    jouer()