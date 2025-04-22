import math
#Les dimensions de la table 
WIDTH = 600
HEIGHT = 400
RAYON = 2

class Position : 
    def __init__(self,canvas,X,Y,Angle,couleur,all_point_recorded):
        self.canvas = canvas
        self.x = X
        self.y = Y 
        self.angle = Angle ## en degree 
        self.couleur = couleur 
        self.liste_point = all_point_recorded
        self.est_alligne()      # corrige la position x, y 
        self.create_marker()       ## appel la fonction create_marker qui va tracer la figure 



    def relier_point(self,liste_point) :
        if len(liste_point) > 0 :
            self.line_id = self.canvas.create_line(liste_point[-1].x,HEIGHT -   liste_point[-1].y, self.x,HEIGHT - self.y, fill=self.couleur, width=2,tags="lines", dash=(4, 2))
        
    
    def create_marker(self): #center coordinates, radius
        x0 = self.x - RAYON
        y0 = HEIGHT - self.y - RAYON
        x1 = self.x + RAYON
        y1 = HEIGHT - self.y + RAYON
        self.rond_id = self.canvas.create_oval(x0, y0, x1, y1, outline=self.couleur,width=2, tags="points")
        self.dir_id = self.canvas.create_line(self.x,HEIGHT - self.y, self.x + 10*math.cos(math.radians(int(self.angle))),HEIGHT - (self.y + 10*math.sin(math.radians(int(self.angle)))), fill=self.couleur, width=2,tags="lines")


    def supprimer_element(self) : 
        self.canvas.delete(self.rond_id)
        self.canvas.delete(self.dir_id)
        self.canvas.delete(self.line_id)



    def __repr__(self): # redefini la fonction print pour le debug
        return f"(x:{self.x},y:{self.y},angle={self.angle})" 
    
    def est_alligne(self) : 
        for point in self.liste_point :
            if point.x-5 < self.x < point.x +5 :
                    self.x =  point.x
            if point.y-5 < self.y < point.y +5 :
                self.y =  point.y


class Attente : 
    def __init__(self,canvas,temps,last_position : Position):
        self.canvas = canvas
        self.x = last_position.x
        self.y = last_position.y 
        self.temps = temps ## en randian 
        self.create_marker()       ## appel la fonction create_marker qui ajouter le temps d'attente sur la table

    
    def create_marker(self): #center coordinates, radius
            self.id = self.canvas.create_text(self.x,HEIGHT- self.y, text=self.temps,fill="white", tags="text")

    def supprimer_element(self) : 
        self.canvas.delete(self.id)


    def __repr__(self): # redefini la fonction print pour le debug
        return f"wait {self.temps}" 
    



class Action :
    def __init__(self,canvas,action,dernier_point) :
        self.canvas = canvas
        self.x = dernier_point.x    ## uniquement pour placer l'action sur la table
        self.y = dernier_point.y
        self.action = action
        self.create_marker()
    
    def create_marker(self) : 
        self.id = self.canvas.create_text(self.x,HEIGHT- self.y, text=self.action,fill="white", tags="text")

    def supprimer_element(self) : 
        self.canvas.delete(self.id)


    def __repr__(self):     # redefini la fonction print pour le debug
        return f"action {self.action}" 
    




### POSITION PAR DEFAUT : 
