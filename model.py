# Auteurs:

### Model
# Ce module comporte tout l'état interne et la logique du jeu

import pygame
from random import*


# des constantes
STEP_SIZE = 20

class Model:
    """
    Une classe qui contient tous les éléments logiques du jeux
    """

    def __init__(self):

        # on initialise les attributs necessaires
        self.personnage = None
        self.boutons = []
        self.grille = None
        self.cree_grille()
        self.ship = False
        self.cree_bat()
        # un booleen qui dit si le jeu est fini
        self.done = False

    def done(self):
        """
        Renvoie si le jeu est fini
        """
        return done

    def ajouter_bouton(self, bouton):
        """
        Fonction qui permet de rajouter un bouton a la liste des boutons
        """
        self.boutons.append(bouton)

    def cree_grille(self):
        """
        Fonction qui dessine la grille
        """
        self.grille = [[None for i in range(10)] for i in range(10)]
        for x in range(10):
            for y in range(10):
                self.grille[x][y] = Case(100+x*60, 100+y*60, 55, 55)

    def cree_bat(self):
        for i in range(5):
            x_bat = randint(0, 9)
            y_bat = randint(0, 9)
            self.grille[x_bat][y_bat].bateau = True
            print(x_bat, y_bat)

    def update(self):
        """
        Fonction appellée à chaque tour de simulation du jeu
        """
        #on update chaque éléments
        self.personnage.update()


class Personnage:
    """
    Une classe qui modélise un personnage
    NOTE: ca ne concerne pas l'affichage (View), que le modéle (M)
    """
    def __init__(self):
        self.x = 0
        self.y = 0

    def get_position(self):
        return (self.x, self.y)

    def set_position(self, pos):
        self.x, self.y = pos

    def deplacer(self, direction):

        if direction == "haut":
            self.y += -STEP_SIZE
        if direction == "bas":
            self.y += +STEP_SIZE
        if direction == "gauche":
            self.x += -STEP_SIZE
        if direction == "droit":
            self.x += +STEP_SIZE

    def taille(self):
        pass

    def update(self):
        pass

class Case :
    """
    Une classe qui s'occupe de gérer les cases
    """

    def __init__(self, position_x, position_y, longueur, largeur):
        self.x = position_x
        self.y = position_y
        self.longueur = longueur
        self.largeur = largeur
        self.touche = False
        self.bateau = False
        self.compteur = 5


    def est_cible(self, x, y):
        souris_x1, souris_y1 = pygame.mouse.get_pos()
        if self.x < souris_x1 < self.x + self.longueur and self.y < souris_y1 < self.y + self.largeur :
            return True
        return False


    def attaque(self):
        self.touche = True
        print("plouf")

    def bat(self):
        self.bateau = True
        self.touche = True
        self.compteur

