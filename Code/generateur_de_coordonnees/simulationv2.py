
#%%
from tkinter import *
from tkinter import simpledialog
import math
from PIL import Image, ImageTk
from generercommande import * 
from actions_robots import *



#Les dimensions de la table 
WIDTH = 600
HEIGHT = 400




def create_circle(x, y, r, color="black"): #center coordinates, radius
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return canvas.create_oval(x0, y0, x1, y1, fill=color)

       
    
def record_point(event):
    if (event.widget==canvas):
        new_position = Position(canvas,event.x,HEIGHT - event.y,angle,couleur_equipe,all_point_recorded)
        new_position.relier_point(actions_recorded)
        actions_recorded.append(new_position)
        all_point_recorded.append(new_position)

             



# Fonctions reliés aux boutons 
    
def Generer():
    print("Le fichier commandes.txt contient les déplacement")
    creer_fichier(actions_recorded)
    copier_texte_dans_presse_papiers("commande.txt")

    


def Couleur():
    global couleur_equipe
    if (couleur_equipe=="yellow"):
        couleur_equipe = "blue"
        colors.configure(bg=couleur_equipe, fg="white")
    else:
        couleur_equipe = "yellow"
        colors.configure(bg=couleur_equipe, fg="black")
    # points_recorded.append(colors['bg'])






def add_wait() : 
    ## demande à l'utilisateur le nombre de seconde, default à 0.5 sec 
    print("ajout d'un wait")
    temps_de_wait = simpledialog.askstring("Ajout d'un delay", "Entrez un delay d'attente en ms, par défaut 500ms")
    if temps_de_wait : 
        new_delay = Attente(canvas,temps_de_wait,actions_recorded[-1])
        actions_recorded.append(new_delay)
    
    else : # default temps 
        temps_default = "500"
        new_delay = Attente(canvas,temps_default,actions_recorded[-1])
        actions_recorded.append(new_delay)


def changer_orientation() : 
    ## demande à l'utilisateur le nombre de seconde, default à 0.5 sec 
    print("changement d'orientation")
    new_orientation = simpledialog.askstring("Changement d'orientation", "Choisissez une nouvelle orientation en radian")
    if new_orientation : 
        global angle 
        angle = new_orientation
        texte = "Choisir orientation \n Actuel  :" + new_orientation
        button_orientation.config(text=texte)

    
    
def add_action() :
     ## demande à l'utilisateur le nombre de seconde, default à 0.5 sec 
    print("Ajout d'une action")
    action = simpledialog.askstring("Ajout action", "Entrez une action")
    if action : 
        new_action = Action(canvas,action,actions_recorded[-1])
        actions_recorded.append(new_action)


def annuler_action(event) :
    ### quand un contrôle z est fait : 
    print("control z")
    derniere_action = actions_recorded.pop()
    derniere_action.supprimer_element()
    del derniere_action




### main 

fenetre = Tk()

actions_recorded = []
angle = "0" # default
couleur_equipe = "Yellow" ## default
all_point_recorded = [] ### point par défaut déja présent 









#### LES ELEMENTS DE L'INTERFACE 

FrameT = Frame(fenetre, borderwidth=2, relief=GROOVE)
FrameT = LabelFrame(fenetre, text="Carte", padx=20, pady=20)
FrameT.pack(side=TOP)
FrameB = Frame(fenetre)
FrameB = LabelFrame(fenetre, text="Selection", padx=20, pady=20)
FrameB.pack(side=BOTTOM)

image = Image.open('table2025.png')
image = image.resize((600,500))
photo = ImageTk.PhotoImage(image)


canvas = Canvas(FrameT,width=600, height=400)
canvas.create_image(0,0,anchor=NW, image=photo,tags="image_ajoute")
canvas.pack(side=TOP, anchor=NW)


Label(FrameT).pack()
Label(FrameB).pack()


#creation d'une liste pour savoir l'orientation du robot 



#creation des boutons d'action 

colors=Button(FrameB, text ='Couleur', bg=couleur_equipe,command=Couleur)
colors.pack(side=LEFT, padx=10, pady=10)


button_wait = Button(FrameB, text ='Wait',command=add_wait)
button_wait.pack(side=RIGHT, padx=10, pady=10)


button_orientation = Button(FrameB, text ='Changer orientation \n Actuel 0',command=changer_orientation)
button_orientation.pack(side=RIGHT, padx=10, pady=10)


button_action = Button(FrameB, text ='Ajouter Action',command=add_action)
button_action.pack(side=RIGHT, padx=10, pady=10)



generer =  Button(FrameB, text ='Generer code', command=Generer)
generer.pack(side=RIGHT, padx=10, pady=10)


# #Les fonctions bind permette d'excuter fonction lors d'une action
fenetre.bind('<ButtonRelease-1>	', record_point)
fenetre.bind("<Control-z>",annuler_action)






########
### POINT PAR DEFAUTS 
position_retenu_pour_action_specifique = Position(canvas,200,200,"0","gray",all_point_recorded)
# attention !! pour que l'affichage rentre dans l'écran, les coordonnés x,y sont divisé par 5 sur l'interface
# Pour sauvegarder un point, bien penser à rediviser par 5 x et y
all_point_recorded.append(position_retenu_pour_action_specifique)


fenetre.mainloop()

# %%
