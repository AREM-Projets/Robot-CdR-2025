"""
Classe de controle de navigation du robot
"""
from Embase import *

class Autopilot:
    def __init__(self, navFileName):
        """
        navFile: string
            fichier contenant le parcours du robot sous le format:

            d <x> <y> <theta> // commande de deplacement. Distances en mm et en degres (?)
            w <temps en s> // commande de delai d'attente
            a <n° d'action> // commande pour executer une action avec les actionneurs (a paufiner)
        """

        self.navFile = open(navFileName, "r") # ouverture du fichier de trajectoire
        self.embase = Embase()
        self.embase.connect()
        self.embase.reset()
        

    def move(self, target_x, target_y, target_theta):
        """
        Execution de la commande de deplacement.

        Version: 1
            Deplacement successif en x, y puis theta
            Pas encore d'arret lidar
        """

        x, y, theta = self.embase.getpos()

        # mouvement sur x
        if x < target_x:
            self.embase.move(AVANCER)
            while self.embase.getpos()[0] < target_x:
                pass
            self.embase.stop()

        elif x > target_x:
            self.embase.move(RECULER)
            while self.embase.getpos()[0] > target_x:
                pass
            self.embase.stop()

        # mouvement sur y
        if y < target_y:
            self.embase.move(TRANSLATION_GAUCHE)
            while self.embase.getpos()[1] < target_y:
                pass
            self.embase.stop()

        elif x > target_x:
            self.embase.move(TRANSLATION_DROITE)
            while self.embase.getpos()[1] > target_y:
                pass
            self.embase.stop()

        # mouvement sur theta
        if theta < target_theta:
            self.embase.move(ROTATION_GAUCHE)
            while self.embase.getpos()[2] < target_theta:
                pass
            self.embase.stop()

        elif theta > target_theta:
            self.embase.move(ROTATION_DROITE)
            while self.embase.getpos()[2] > target_theta:
                pass
            self.embase.stop()

    def home(self):
        self.move(0, 0, 0)

        


    def runloop(self):
        """
        Methode principale pour l'execution du robot
        """
        pass