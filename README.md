# Logimage
Projet Python par l'ISEN 

# Règles
Chaque grille de logimage est un dessin à reconstituer en exploitant les indices. Pour cela, utilisez les nombres à gauche de chaque ligne et en haut de chaque colonne pour noircir des cases vides. Chaque nombre indique la longueur d’un bloc à noircir sachant que l’ordre des blocs suit celui des indices : de gauche à droite (ligne) et de haut en bas (colonne). Entre deux blocs voisins, au moins une case doit rester vide.
Trucs et astuces : commencer par les indices les plus élevés. Inutile de faire des suppositions.

# Programme
Demande le nombre de colonnes et de lignes (X,Y) 
Faire une boucle : X1 à Xn puis de Y1 à Yn pour tracer la grille
Demande les numéros des colonnes et lignes
Faire une boucle : X1 à Xn puis de Y1 à Yn pour mettre les numéros (LISTE)
Associer une case pour chaque X et Y 
résolution en partant du haut avec du bleu
résolution en partant du bas avec du rouge
s'il y a des cases avec du orange et du rouge du même numéro alors la mettre en orange.
effacer les couleurs bleu et rouge
résolution en partant de la droite avec du bleu
résolution en partant de la gauche avec du rouge
s'il y a des cases avec du orange et du rouge du même numéro alors la mettre en orange.
effacer les couleurs bleu et rouge
refaire la méthode droite/gauche, haut/bas mais en prenant en compte les cases oranges (ligne 14-21)
Si un numéro d'une ligne/colonne est validé (toutes les cases associées sont placées), placer une croix avant et après les cases
dés qu'un numéro est validé et qu'il est sur le bord, le supprimer de la colonne/ligne
Si une colonne ou ligne est finie , mettre croix dans les cases différentes du orange 
Si première case est orange , les cases en dessous sont orange par rapport au numéro du haut 
Si dernière case est orange , les cases au-dessus sont orange par rapport au numéro du bas
dés qu'une ligne / colonne du bord est compléter (tous les numéros et croix sont placés), supprimer la colonne
si une ligne/colonne reste un seul numéro, faire technique droite/gauche, haut/bas et mettre une croix la ou il n'y a pas de couleur (car les cases non colorées ne pourront jamais être colorées




