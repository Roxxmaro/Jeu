import tkinter as tk
from random import randint
from time import sleep
from PIL import ImageTk, Image

class Fenetre(tk.Tk):
#Permet d'afficher toute les boites dans la fenetre principal (clavier, image et emplacements de lettres)
    def MaFenetre(self, grille=None,abscisse=None, ordonnée=None):
        grille = self.grille()
        grille.place(x=300,y=300)
        abscisse = self.abscisse()
        abscisse.place (x=300, y=100)
        ordonnee = self.ordonnee()
        ordonnee.place(x=190, y=300)
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
                btn = Bouton(grille, text = 'A%s-O%s' %(r,c), width=5, height=1, bg='white', fg='white')
                btn.res_abs()
                btn.res_global_abscisse
                btn['command'] = btn.cliquer

                btn.grid(row=r, column=c)
        return grille


    def ordonnee (self):
        ab = [[10],[2,1,1],[4,1],[3,3,1],[7],[1,3,2],[2,2],[2,2,1],[3,3,1],[1,2,3]]
        ordonnee = tk.Frame(self)
        D = 0
        for a in range (10):
            for b in range(1):
                 n_ordonnee = tk.Label(ordonnee, text = ab[D])
                 n_ordonnee.grid (row=a, column=b, pady= len(ab) -1)
                 D+=1
        return ordonnee

    def abscisse (self):
        orr = [[10],[1,3,3],[10],[5],[10],[10],[1,2,1],[1,1,1],[1,1],[10]]
        abscisse = tk.Frame(self)
        E = 0
        A = 0
        F=[]

        for c in range(10):
            for d in range(1):
                 t = orr[E]
                 final = ''
                 for i in range(len(t)):
                     final += str(t[i]) + '\n'
                 n_abscisse = tk.Label (abscisse, text = final)
                 n_abscisse.grid (row = d, column=c , padx= 6*len(orr)/2 -2 )
                 E+=1
        return abscisse

    def final(self):
        btn['command'] = btn.res_abs
        btn ['command'] = btn.res_global_abscisse


class Bouton(tk.Button):
    def cliquer(self):
        if self['bg'] == 'black':
             self.config(bg='white',text='X')
        elif self['text'] == 'X':
            self['text']= ''
        else:
            self['bg'] = 'black'
            self['fg'] = 'black'
    def res_abs(self):
        orr = [[10],[1,3,3],[10],[5],[10],[10],[1,2,1],[1,1,1],[1,1],[10]]
        for A in range (len(orr)):
            B = str(A)
            C = orr[A]
            for i in range (len(C)):
                D = C[i]
                if D == len(orr):
                    for j in range(10):
                        x = 'A'+str(j)+'-O'+B
                        if self['text'] == x:
                            self.config(bg='black')

    def res_global_abscisse(self):
        orr = [[10],[1,3,3],[5,2],[5],[1,1,6],[2,7],[1,2,1],[1,1,1],[1,1],[1,1,1]]
        ab = [[0],[10],[4,1],[3,3,1],[7],[1,3,2],[2,2],[2,2,1],[3,3,1],[1,2,3]]
        A=0
        print(x)
        for i in range (ab[A]):
            if ab[i] == len(orr):
               self.config(bg='black')
               print(i)
        A+=1
        return res_global_abscisse



# définit les paramètres de la fenêtre

app = Fenetre()
app.geometry('500x650')
app.mainloop()