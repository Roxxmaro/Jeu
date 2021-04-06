from tkinter import *
from tkinter.messagebox import *
import webbrowser
import numpy as np

#Les Fonctions

def lien_github():
    webbrowser.open_new("https://github.com/Roxxmaro/Jeu")

def alert():
    showinfo("En Dev")

def play():
   for ligne in range(5):
    for colonne in range(5):
        Button(fenetre, text='L%s-C%s' % (ligne, colonne), borderwidth=1).grid(row=ligne, column=colonne)

def plateauX():
    label_x = Label(fenetre, text="Mettre un chiffre", font=("Courrier",14) , bg="#E68A11" , fg="#FFFFFF")
    label_x.pack()
    x = Entry(fenetre)
    x.pack()
    def afficherX():
     print(x.get())
    bouton1=Button(fenetre, text="Valider", command=afficherX)
    bouton1.pack(side=TOP, padx=50, pady=10)

def plateauY():
    label_y = Label(fenetre, text="Mettre un chiffre", font=("Courrier",14) , bg="#E68A11" , fg="#FFFFFF")
    label_y.pack()
    y = Entry(fenetre)
    y.pack()
    def afficherY():
     print(y.get())
    bouton2=Button(fenetre, text="Valider", command=afficherY)
    bouton2.pack(side=TOP, padx=50, pady=10)


def grille ():
    label_x = Label(fenetre, text="Mettre le nombre de colonne", font=("Courrier",14) , bg="#E68A11" , fg="#FFFFFF")
    label_x.pack()
    x = Entry(fenetre)
    x.pack()
    def afficherX():
     print(x.get())
    bouton1=Button(fenetre, text="Valider", command=afficherX)
    bouton1.pack(side=TOP, padx=50, pady=10)
    label_y = Label(fenetre, text="Mettre le nombre de ligne", font=("Courrier",14) , bg="#E68A11" , fg="#FFFFFF")
    label_y.pack()
    y = Entry(fenetre)
    y.pack()
    def afficherY():
     print(y.get())
    bouton2=Button(fenetre, text="Valider", command=afficherY)
    bouton2.pack(side=TOP, padx=50, pady=10)



#Création Fenêtre
fenetre = Tk()

#Informations Fenêtre
fenetre.title("Logimage")
fenetre.geometry("1080x720")

fenetre.iconbitmap("logo.ico")
fenetre.config(background = "#E68A11")

#Création des Frames
framesign = Frame(fenetre, bg="#E68A11")
frametitle = Frame(fenetre, bg="#E68A11")

#Texte Fenêtre Titre
label_title = Label(frametitle, text="Bienvenue sur Logimage", font=("Courrier",30) , bg="#E68A11" , fg="#FFFFFF")
label_title.pack()

#Creation Bouton Grille
grille_button = Button(frametitle, text="Lancer une Partie", font=("Courrier",30) , fg="#E68A11" , bg="#FFFFFF", command=grille)
grille_button.pack(pady=30)

#Texte Fenêtre Signature
label_sign1 = Label(framesign, text="Quentin & Guillaume", font=("Courrier",14) , bg="#E68A11" , fg="#FFFFFF")
label_sign1.pack()
label_sign2 = Label(framesign, text="ISEN Project", font=("Courrier",14) , bg="#E68A11" , fg="#FFFFFF")
label_sign2.pack()

#Ajout des Frames
frametitle.pack(expand=YES)
framesign.pack(expand=YES, side=BOTTOM)

#Menu Principale
menubar = Menu(fenetre)

#Choix du Plateau
menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label="10x10", command=alert)
menu1.add_separator()
menu1.add_command(label="10x10", command=alert)
menu1.add_separator()
menu1.add_command(label="10x10", command=alert)
menu1.add_separator()
menu1.add_command(label="10x10", command=alert)
menubar.add_cascade(label="Plateau", menu=menu1)

#Choix des Numéros
menu2 = Menu(menubar, tearoff=0)
menu2.add_command(label="Numéro X", command=alert)
menu2.add_separator()
menu2.add_command(label="Numéro Y", command=alert)
menubar.add_cascade(label="Numéros", menu=menu2)

#Page d'aide
menu3 = Menu(menubar, tearoff=0)
menu3.add_command(label="Github", command=lien_github)
menubar.add_cascade(label="Aide", menu=menu3)

fenetre.config(menu=menubar)

#Fin de Fenêtre
fenetre.mainloop()
