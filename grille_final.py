import tkinter as tk
from logimage_final import*


def jouer():
    global app,tableau,enonce_ab,enonce_orr,grille_joueur
    tableau = creation_tableau()
    enonce_ab = compte_ligne(tableau)
    enonce_orr = compte_ligne(inver_col_lig(tableau))
    grille_joueur = [[' ' for i in range(len(enonce_orr))]for i in range(len(enonce_ab))]
    app = Fenetre()
    app.resizable(width=False,height=False)
    app.mainloop()

def verif():
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
    app.destroy()
    jouer()

def quitter():
    app.destroy()

def chaine_2_grille(grille):
    #renvoie sous forme de chaine de caractere :
    n = 0
    for i in range(len(grille)):
        for j in range(len(grille[i])):
            if grille[i][j] == ' ':
                n += 1
    if n == 0:
        return True

class Fenetre(tk.Tk):
#Permet de cree la fenetre principal et de lancer le creation des boites
    def __init__(self):
        tk.Tk.__init__(self)
        self.MaFenetre()

#Permet d'afficher toute les boites dans la fenetre principal (clavier, image et emplacements de lettres)
    def MaFenetre(self):
        grille = self.grille()
        grille.grid(row=1, column=1)
        abscisse = self.abscisse()
        abscisse.grid(row=0, column=1)
        ordonnee = self.ordonnee()
        ordonnee.grid(row=1, column=0)
        tk.Button(self, text='valider', command=verif).grid(row=0, column=0)

#Permet de créer la 'boite' qui permet d'afficher la grille en utilisant la fonction de création des boutons et le bouton ENTREE
    def grille(self): #Cette fonction permet d'afficher la grille
            #/ ==> Le joueur est sur qu'il n'y a rien, case =rouge
            #X ==> Le joueur est sur qu'il y a qq chose, case =noir
            #  ==> Le joueur ne sait pas,case =blanche
        grille = tk.Frame(self)
        for r in range(len(enonce_ab)):
            for c in range(len(enonce_orr)):
                btn = Bouton(grille, text = f'{r},{c}, ' , width=5, height=1,bg='white',fg='white')
                btn['command'] = btn.cliquer

                btn.grid(row=r, column=c)
        return grille

    def ordonnee (self): #Cette fonction permet d'afficher les enoncés lignes
        ordonnee = tk.Frame(self)
        for a in range (len(enonce_ab)):
            n_ordonnee = tk.Label(ordonnee, text = enonce_ab[a])
            n_ordonnee.grid (row=a, column=0, pady= 9)

        return ordonnee

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