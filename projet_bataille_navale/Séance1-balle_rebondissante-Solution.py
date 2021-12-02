#test
import time

def effaceEcran ():
    for i in range (1,100) :
        print("\n")


# Initialise la grille de facon a ce qu'elle contienne ce qui se trouve 
# a la figure de droite 

def initGrille (grille, pos_balle_x, pos_balle_y) :
    # initialiser la grille à vide :
    for ligne in range (10) :
        for colonne in range (10) :
            grille[ligne][colonne]=' '
           
    for colonne in range (10) :
        grille[0][colonne]='*'
        grille[9][colonne]='*'

    for ligne in range (10) :
        grille [ligne][0]='*'
        grille [ligne][9]='*'

    grille [pos_balle_x][pos_balle_y]='O'



    
    
# Affiche le rectangle d'etoiles et la balle (tout ceci en meme
# temps et non pas le rectangle puis la balle...) 

def afficheGrille (grille) : 
    for ligne in range (10) :
        for colonne in range (10) :
            print (grille[ligne][colonne],end="")
        print(" ")
    


    
# Calcule la nouvelle position de la balle en fonction de 
# l'ancienne position de la balle (old_pos_balle_x, old_pos_balle_y) 
#  et du vecteur de deplacement (deplacement_x, deplacement_y).
# supprime l'ancienne position de la balle et place cette dernière 
# a la nouvelle position

def modifiePositionBalle (grille, pos_balle_x, pos_balle_y, deplacement_x, deplacement_y) :

    theo_pos_x=0
    theo_pos_y=0;

	# On efface l'ancienne balle
    grille[pos_balle_x][pos_balle_y]=' '

    print ("Position actuelle : (",str(pos_balle_x)," , ",str(pos_balle_y),")")
    print ("Deplacement actuel : (",str(deplacement_x)," , ",str(deplacement_y),")")

	# On calcule la future position theorique de la balle
    theo_pos_x = pos_balle_x + deplacement_x 
    theo_pos_y = pos_balle_y + deplacement_y

	# En fonction de la position theorique de la balle
    # si elle tape sur la bordure, 
    # on modifie le vecteur de deplacement
    if (grille[theo_pos_x][theo_pos_y]=='*') :
		# Si on tape sur l'axe vertical
        if (( theo_pos_x == 0 ) or ( theo_pos_x == 9 )) :
            deplacement_x = - deplacement_x

        # Si on tape sur l'axe horizontal
        if (( theo_pos_y == 0 ) or ( theo_pos_y == 9 )) :
            deplacement_y = - deplacement_y

    # On calcule la nouvelle position de la balle
    pos_balle_x = pos_balle_x + deplacement_x
    pos_balle_y = pos_balle_y + deplacement_y

    print ("Nouvelle position : (",str(pos_balle_x)," , ",str(pos_balle_y),")")
	
    # On met la balle dans la grille a sa nouvelle position
    grille[pos_balle_x][pos_balle_y]='O'
    
    return grille, pos_balle_x, pos_balle_y, deplacement_x, deplacement_y


##################################
# programme principal :
##################################
    
    
grille= [[' ' for i in range(10)] for j in range(10)] 	# grille qui pourra contenir
                # 3 sortes de caractères : '*' ou 'O' ou le caractere espace ' '

    
pos_balle_x=3   # position  balle au depart
pos_balle_y=4     


deplacement_x=1
deplacement_y=1;  # vecteur de deplacement de la balle

initGrille (grille, pos_balle_x, pos_balle_y) ;

s='*'
while (s!='s') :
    effaceEcran ()
    afficheGrille(grille);
    grille, pos_balle_x, pos_balle_y, deplacement_x, deplacement_y = modifiePositionBalle (grille, pos_balle_x, pos_balle_y, deplacement_x, deplacement_y)
	
    s=input("Appuyez sur la touche entrée ou 's' pour sortir... ")
    
    
    
    
    