import tkinter as tk
from random import randint
from time import sleep

class Fenetre(tk.Tk):
#Permet d'afficher toute les boites dans la fenetre principal (clavier, image et emplacements de lettres)
    def MaFenetre(self, grille=None,abscisse=None, ordonnée=None):
        grille = self.grille()
        grille.place(x=300,y=300)
        ordonnee = self.abscisse()
        ordonnee.place (x=300, y=200)
        ordonnee = self.ordonnee()
        ordonnee.place(x=250, y=300)
#Permet de cree la fenetre principal et de lancer le creation des boites
    def __init__(self):
        tk.Tk.__init__(self)
        self.MaFenetre()



#Permet de créer la 'boite' qui permet d'afficher la grille
#en utilisant la fonction de création des boutons et le bouton ENTREE
    def grille(self):
        grille = tk.Frame(self)
        for r in range(10):
            for c in range(10):
                btn = Bouton(grille, text = '',width=5, height=1, bg='white')
                btn['command'] = btn.cliquer
                btn.grid(row=r, column=c)
        return grille

    def ordonnee (self):
        ab = [[2,3],[1],[2,3],[1],[2,3],[1],[2,3],[1],[2,3],[1]]
        ordonnee = tk.Frame(self)
        D = 0
        for a in range (10):
            for b in range(1):
                 n_ordonnee = tk.Label(ordonnee, text = ab[D])
                 n_ordonnee.grid (row=a, column=b)
                 D+=1
        return ordonnee

    def abscisse (self):
        orr = [[2,3],[1],[2,3],[1],[2,3],[1],[2,3],[1],[2,3],[1]]
        abscisse = tk.Frame(self)
        E = 0
        for c in range (10):
            for d in range(1):
                 n_abscisse = tk.Label (abscisse, text = orr[E])
                 n_abscisse.grid (row=d, column=c)
                 E+=1
        return abscisse


class Bouton(tk.Button):
    def cliquer(self):
        if self['bg'] == 'black':
             self.config(bg='white')
        else:
            self['bg'] = 'black'



# définit les paramètres de la fenêtre

app = Fenetre()
app.geometry('500x650')
app.mainloop()