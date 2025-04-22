#%%
import math
from actions_robots import * 
import pyperclip

PI = 3.14





def generer_commande_actions(Liste_des_actions) : 
    commande = ""
    for action in Liste_des_actions :
        if isinstance(action,Position) :
             commande += "d " + str(5*action.x) + " " + str(5*action.y) + " " + str(action.angle)

        if isinstance(action,Attente) :
             commande += "w " + str(action.temps) 

        if isinstance(action,Action) :
            commande += "a " + str(action.action) 
        commande += "\n"

    return commande


def creer_fichier(Liste_des_actions) :
    commande = generer_commande_actions(Liste_des_actions)
    with open("commande.txt", 'w') as fichier:
            fichier.write(commande)



def copier_texte_dans_presse_papiers(fichier):
    try:
        # Lire le contenu du fichier
        with open(fichier, 'r') as file:
            contenu = file.read()

        # Copier le contenu dans le presse-papiers
        pyperclip.copy(contenu)
        print("Le texte a été copié dans le presse-papiers.")

    except FileNotFoundError:
        print(f"Le fichier {fichier} n'existe pas.")
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")
   