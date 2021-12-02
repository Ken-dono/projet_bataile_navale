#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
TP AP1
Licence SESI 1ère année
Univ. Lille 1

bataille_navale.py

Module pour le jeu de bataille navale.

Pour une description générale du jeu voir
http://fr.wikipedia.org/wiki/Bataille_navale_%28jeu%29

"""

__author__ = 'ICI VOS NOMS'
__date_creation__ = 'ICI LA DATE'


###############################################
# Modules utilisés
###############################################

# Pour la disposition aléatoire des navires
from random import randint

# Pour le fichier des scores
from datetime import datetime 

###############################################
# Constantes nommées utilisées
###############################################

# les deux dispositions possibles pour un navire
#  sur le plateau :
# - H : horizontale
# - V : verticale
DISPOSITIONS="HV"


# codes réponses d'analyse de tirs
RATE = 0
TOUCHE = 1
COULE = 2

# nom du fichier contenant les scores réalisés
FICHIER_RESULT = 'bataille_navale_scores.txt'

###############################################
# Procédure principale du jeu
###############################################

def jouer (nom,descr):
    """
    str, str -> ()
    procédure de jeu complet de bataille navale,
    le nom du joueur est donné par le paramètre nom, 
    et le jeu est décrit dans le fichier descr.

    CU : le fichier jeu doit exister et être conforme
    à un fichier de description.
    """
    jeu = cree_jeu(descr)
    decrire_le_jeu(jeu)
    nbre_tirs = 0
    while not tous_coules(jeu):
        tir = lire_un_tir (nom)
        nbre_tirs += 1
        nav,res = analyse_un_tir (jeu,tir)
        if res == RATE:
            print ("raté.")
        elif res == TOUCHE:
            print (nav + " touché.")
        else:
            print (nav + " coulé.")
    sauver_result (nom,descr,nbre_tirs)
    print ("Terminé en {0} tirs".format(nbre_tirs))

###############################################
# Opérations sur les fichiers
###############################################

def lire_donnees(num_descr):
    """
    str -> tuple
    renvoie un triplet dont les deux premières composantes sont 
    et la troisième une liste de couples (nature, taille) où
    nature est une chaîne de caractères décrivant la nature du navire
    et taille un entier désignant le nombre de cases occupées par ce navire.
    Toutes ces données sont lues dans un fichier nommé 'jeu'+num_descr+'.txt'.

    CU : le fichier 'jeu'+num_descr+'.txt' doit exister et être au bon format, 
    ie un  fichier texte contenant :
    larg : haut
    nature1 : taille1
    nature2 : taille2
    ...
    """



def sauver_result (nom, jeu, nbre):
    """
    str, str, int -> NoneType
    ajoute une ligne dans le fichier FICHIER_RESULT
    contenant le nom, le numéro du jeu joué et le nombre de tirs effectués 
    dans la partie.

    CU : aucune
    """



###############################################
# Procédures de construction du jeu
###############################################
    
def cree_jeu (descr):
    """
    str -> dict
    renvoie un nouveau jeu de bataille navale construit à partir des données 
    lues dans le fichier descr.


    Le jeu est représenté par un dictionnaire à quatre clés :
    - 'plateau' pour représenter le plateau de jeu (l'espace maritime) avec ses navires
    - 'nb_cases_occupees' dont la valeur associée est le nombre de cases du plateau
                          occupées par les navires
    - 'touches' dictionnaire contenant deux champs :
                * l'un nomme 'nb_touches' contenant un entier 
                * l'autre nomme 'etats_navires' qui contient un dictionnaire
                  donnant pour chaque navire le nombre de tirs 
                  qu'ils peuvent encore recevoir avant d'être coulés
    - 'coups_joues' ensemble des coups joués depuis le début de la partie.

    CU : le fichier doit contenir une description correcte du jeu (cf lire_donnees)
    """


def cree_plateau (l, h, l_nav):
    """
    int, int, list -> dict
    renvoie un plateau de largeur l et de hauteur h occupé par les navires 
    de l_nav.
    La disposition est aléatoire.

    CU : les dimensions doivent permettre le placement de tous les navires
    """

def est_placable (esp, nav, pos, disp):
    """
    dict, tuple, tuple, str -> bool
    
    CU : disp = 'H' ou 'V'
    """


def placer (esp, nav):
    """
    dict, tuple -> NoneType
    place le navire nav dans l'espace maritime esp.
    Choix de l'emplacement aléatoire.

    CU : il doit rester de la place
    """


###############################################
# Procédures de déroulement du jeu
###############################################
    
def decrire_le_jeu (jeu):
    """
    dict -> ()
    imprime une description du jeu.
    
    CU : aucune
    """


def lire_un_tir (nom):
    """
    str -> tuple
    renvoie un couple d'entiers lus sur l'entrée standard

    CU : l'entrée doit être de la forme xxx,yyy avec xxx et yyy
         une représentation décimale de deux nombres entiers
    """



def analyse_un_tir (jeu,tir):
    """
    dict, tuple -> str,int
    renvoie 
      - ("",RATE) si tir raté
      - (nav,TOUCHE) si nav touché
      - (nav,COULE) si nav coulé
    et modifie l'état du jeu en conséquence.

    CU : aucune 
    """


def tous_coules (jeu):
    """
    dict -> bool
    renvoie True si tous les navires du plateau de jeu ont été coulés
            et False dans le cas contraire.

    CU : aucune
    """
    return True


    
###############################################
# Pour une utilisation du module depuis un terminal
###############################################    

# if __name__ == '__main__':
#     import sys

#     if len (sys.argv) != 3:
#         jouer ('Jean Bart','1')
#     else:
#         jouer (sys.argv[1],sys.argv[2])



