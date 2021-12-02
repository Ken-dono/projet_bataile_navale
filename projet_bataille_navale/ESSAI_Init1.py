# Initialise la grille de facon a ce qu'elle contienne ce qui se trouve
# a la figure de droite

class board()
def initGrille(grille, pos_balle_x, pos_balle_y):
    # initialiser la grille à vide :
    for ligne in range(10):
        for colonne in range(10):
            grille[ligne][colonne] = ' '

    for colonne in range(10):
        grille[0][colonne] = '*'
        grille[9][colonne] = '*'

    for ligne in range(10):
        grille[ligne][0] = '*'
        grille[ligne][9] = '*'

    grille[pos_balle_x][pos_balle_y] = 'O'

# Affiche le rectangle d'etoiles et la balle (tout ceci en meme
# temps et non pas le rectangle puis la balle...)

def afficheGrille (grille) :
    for ligne in range (10) :
        for colonne in range (10) :
            print (grille[ligne][colonne],end="")
        print(" ")

##################################
# programme principal :
##################################

grille= [[' ' for i in range(10)] for j in range(10)]

pos_balle_x = 3  # position  balle au depart
pos_balle_y = 4

initGrille (grille, pos_balle_x, pos_balle_y)
afficheGrille (grille)