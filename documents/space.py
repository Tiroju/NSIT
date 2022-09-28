import pygame  # necessaire pour charger les images et les sons
import random
import math

class Joueur(): # classe pour créer le vaisseau du joueur
    def __init__(self):
        self.position = 400
        self.hauteur = 500
        self.image = pygame.image.load("Doom Slayer.png")
        self.image = pygame.transform.scale(self.image, (64, 64))
        self.sens = "O"
        self.vitesse = 2
        self.score = 0
        self.vie = 5
    
    def deplacer(self):
        if (self.sens == "droite") and (self.position < 740):
            self.position = self.position + self.vitesse
        elif (self.sens == "gauche") and (self.position > 0):
            self.position = self.position - self.vitesse
            
    def tirer(self):
        self.sens = "O"
        
    def marquer(self):
        self.score = self.score + 1
        
    def losePV(self):
        """
        Fonction qui eneleve des PV au joueur
        """
        self.vie = self.vie - 1

    def PV(self):
        """
        Fonction qui renvoie True si le joueur n'a plus de PV
        """
        if self.vie <= 0:
            return True
        
            
            
class Balle():
    def __init__(self, tireur):
        self.tireur = tireur
        self.depart = tireur.position + 16
        self.hauteur = 492
        self.image = pygame.image.load("balle.png")
        self.etat = "chargee"
        self.vitesse = 5
        
    def bouger(self):
        if self.etat == "chargee":
            self.depart = self.tireur.position + 16
            self.hauteur = 492
        elif self.etat == "tiree" :
            self.hauteur = self.hauteur - self.vitesse
        if self.hauteur < 0:
            self.etat = "chargee"
            
    def toucher(self, vaisseau):
        if (math.fabs(self.hauteur - vaisseau.hauteur) < 40) and (math.fabs(self.depart - vaisseau.depart) < 40):
            self.etat = "chargee"
            return True
            
    def toucherBoss(self, vaisseau):
        """
        Fonction qui permet à la balle de toucher n'importe quelle partie du boss pour être comptabilisé comme un tir réussi
        """
        if (math.fabs(self.hauteur - vaisseau.hauteur) < 100) and (0 <= self.depart - vaisseau.depart < 150):
            self.etat = "chargee"
            return True
            
class Ennemi():
    NbEnnemis = random.randint(3,4)
    
    def __init__(self):
        self.depart = random.randint(1,700)
        self.hauteur = 10
        self.type = random.randint(1,3)
        if  (self.type == 1):
            self.image = pygame.image.load("Baron Of Hell.png")
            self.image = pygame.transform.scale(self.image, (80, 80))
            self.vitesse = 0.5
        elif (self.type ==2):
            self.image = pygame.image.load("Lost Soul.png")
            self.image = pygame.transform.scale(self.image, (80, 80))
            self.vitesse = 1
        elif (self.type ==3):
            self.image = pygame.image.load("Cacodemon.png")
            self.image = pygame.transform.scale(self.image, (80, 80))
            self.vitesse = 0.75
        
    def avancer(self):
        self.hauteur = self.hauteur + self.vitesse
        
    def disparaitre(self):
        self.depart = random.randint(1,700)
        self.hauteur = 10
        self.type = random.randint(1,3)
        if  (self.type == 1):
            self.image = pygame.image.load("Baron Of Hell.png")
            self.image = pygame.transform.scale(self.image, (80, 80))
            self.vitesse = 0.5
        elif (self.type ==2):
            self.image = pygame.image.load("Lost Soul.png")
            self.image = pygame.transform.scale(self.image, (80, 80))
            self.vitesse = 1
        elif (self.type ==3):
            self.image = pygame.image.load("Cacodemon.png")
            self.image = pygame.transform.scale(self.image, (80, 80))
            self.vitesse = 0.75
            
    def degats(self, vaisseau):
        """
        Fonction qui renvoie True lorsqu'un ennemi touche le joueur
        """
        if (math.fabs(self.hauteur - vaisseau.hauteur) < 40) and (math.fabs(self.depart - vaisseau.position) < 40):
            return True
            
class Boss(): # Classe qui permet de créer le boss
    def __init__(self):
        self.depart = 350
        self.hauteur = 10
        self.image = pygame.image.load("Cyberdemon.png")
        self.vitesse = 2
        self.vie = 20
        
    def avancer(self):
        """
        Fonction qui fait se déplacer le boss aléatoirement
        """
        move = random.randint(1,4)
        if move == 1 and self.hauteur > 12 :
            self.hauteur = self.hauteur - self.vitesse
        elif move == 2 and self.hauteur < 198:
            self.hauteur = self.hauteur + self.vitesse
        elif move == 3 and self.depart > 12:
            self.depart = self.depart - self.vitesse
        elif move == 4 and self.depart < 698:
            self.depart = self.depart + self.vitesse
    
    def mort(self):
        """
        Fonction qui fait disparaitre le boss lorsque ses PV passent à 0
        """
        if self.vie == 0:
            self.hauteur = 800
            return True
        

class BalleBoss(): # Classe qui permet de créer la balle du boss
    def __init__(self, tireur):
        self.tireur = tireur
        self.depart = tireur.depart + 75
        self.hauteur = tireur.hauteur
        self.image = pygame.image.load("balle Boss.png")
        self.etat = "chargee"
        self.vitesse = 3
        
    def tirBoss(self):
        """
        Fonction qui déplace la balle du boss lors d'un tir
        """
        if self.etat == "chargee":
            self.depart = self.tireur.depart + 75
            self.hauteur = self.tireur.hauteur
        elif self.etat == "tiree" :
            self.hauteur = self.hauteur + self.vitesse
        if self.hauteur > 600:
            self.etat = "chargee"
            
    def toucherJoueur(self, vaisseau):
        """
        Fonction qui permet à la balle du boss de toucher le joueur
        """
        if (math.fabs(self.hauteur - vaisseau.hauteur) < 40) and (math.fabs(self.depart - vaisseau.position) < 40):
            self.etat = "chargee"
            return True
