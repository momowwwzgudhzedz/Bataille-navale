# Auteurs:

### Main pour notre jeu
# L'architecture du jeu utilise trois modules selon le patron de conception MVC

import pygame

pygame.init()
pygame.font.init()

from model import *
from controller import *
from view import *


try:
    ### Initialisation

    model = Model()
    view = View(model)
    controller = Controller(model)

    # les boutons:
    bouton1 = Bouton("bouton1", 30, 30, 100, 50, "coucou")
    model.ajouter_bouton(bouton1)

    # le personnage et son image:
    perso = Personnage()
    perso.set_position((300, 300))
    model.personnage = perso

    # vue_perso = ViewPersonnage(perso)
    # view.add_elem(vue_perso)


    ### Boucle du jeu
    # chaque tour de boucle est un 'pas' dans le jeux
    while not model.done :
        # d'abord les entrées utilisateur
        controller.gerer_input()
        # puis la logique du jeu
        model.update()
        # puis on affiche

        view.draw()

except Exception as e:
    pygame.quit()
    raise e

pygame.quit()
print("pygame_quit")

