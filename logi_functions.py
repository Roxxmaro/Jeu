#les Fonctions

def lien_github():
    webbrowser.open_new("https://github.com/Roxxmaro/Jeu")

def ligne_de_carres(x, y, c, n):
    # dessiner une ligne de n carrés
    i = 0
    while i < n:
        can.create_rectangle(x, y, x+c, y+c, fill='white')
        i += 1
        x += c*2 # espacer les carrés

def damier(c, nl, nc):
    # dessiner nl lignes de nc carrés de taille c avec décalage alterné
    y = 0
    while y < nl:
        if y % 2 == 0: # une ligne sur deux, on
            x = 0 # commencera la ligne de
        else: # carrés avec un décalage
            x = 1 # de la taille d'un carré
        ligne_de_carres(x*c, y*c, c, nc)
        y += 1

def alert():
    showinfo("En Dev")

def new_fenetre():
    c = 40 # côté d'un carré
    nl = 8 # nombre de lignes
    nc = 10 # nombre de colonnes
    can = Tk()
    can.title("Grille")
    can = Canvas(can, width=c*nc-3, height=c*nl-3, bg='white')
    can.pack(side=TOP)
    damier(c, nl, nc)
    can.mainloop()

def play():
    c = 40 # côté d'un carré
    nl = 8 # nombre de lignes
    nc = 10 # nombre de colonnes
    can = Tk()
    can.title("Grille")
    can = Canvas(can, width=c*nc-3, height=c*nl-3, bg='white')
    can.pack(side=TOP)
    damier(c, nl, nc)
    can.mainloop()

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