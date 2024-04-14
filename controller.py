# Auteurs:

### Controller
# Ce module comporte le code pour gérer l'interaction avec l'utilisateur-rice

import pygame

# des constantes
texte_bouton = pygame.font.SysFont('Corbel', 30, bold=True)


class Controller:
    """
    Une classe qui s'occupe de gérer toutes les entrées de l'utilisateur-rice.
    """

    def __init__(self, model):
        self.model = model

    def gerer_input(self):

        souris_x, souris_y = pygame.mouse.get_pos()
        souris_x1, souris_y1 = pygame.mouse.get_pos()

        for event in pygame.event.get():

            ### clavier
            if event.type == pygame.KEYDOWN:

                # fermer le jeux
                if event.key == pygame.K_ESCAPE:
                    self.model.done = True

                # deplacer le personnage
                if event.key == pygame.K_UP:
                    self.model.personnage.deplacer("haut")

                if event.key == pygame.K_DOWN:
                    self.model.personnage.deplacer("bas")

                if event.key == pygame.K_LEFT:
                    self.model.personnage.deplacer("gauche")

                if event.key == pygame.K_RIGHT:
                    self.model.personnage.deplacer("droit")

            ### souris
            elif event.type == pygame.MOUSEBUTTONDOWN:

                for bouton in self.model.boutons:
                    if bouton.est_cible(souris_x, souris_y):
                        if bouton.nom == "bouton1":
                            print("coucou le bouton est cliqué")

                for ligne in self.model.grille :
                    for case in ligne :
                        if case.est_cible(souris_x1, souris_y1):
                            if case.bateau == True:
                                case.bat()
                            else:
                                case.attaque()


            ### fenetre
            elif event.type == pygame.QUIT:
                self.model.done = True


class Bouton:
    """
    Classe qui modélise un bouton à cliquer
    """

    def __init__(self, nom, x, y, largeur, longueur, text=None):
        # on utilise un nom pour différencier les boutons
        self.nom = nom
        self.x, self.y = x, y
        self.largeur = largeur
        self.longueur = longueur
        self.text = text
        if text != None:
            self.text = texte_bouton.render(text , True , (200,200,200))

    def est_cible(self, x, y):
        """
        x et y : la position de la souris
        Sortie : Vrai si la souris est sur le bouton, Faux sinon
        """
        return x >= self.x and x <= (self.x + self.largeur) and y >= self.y and x <= (self.y + self.longueur)




