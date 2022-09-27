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
        self.score = self.score + 25
        
    def losePV(self):
        self.vie = self.vie - 1
        
            
            
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
            
            
class Ennemi():
    NbEnnemis = random.randint(2,5)
    
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
            self.vitesse = 1.5
        elif (self.type ==3):
            self.image = pygame.image.load("Cacodemon.png")
            self.image = pygame.transform.scale(self.image, (80, 80))
            self.vitesse = 1
        
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
            self.vitesse = 1.5
        elif (self.type ==3):
            self.image = pygame.image.load("Cacodemon.png")
            self.image = pygame.transform.scale(self.image, (80, 80))
            self.vitesse = 1
            
    def degats(self, vaisseau):
        if (math.fabs(self.hauteur - vaisseau.hauteur) < 40) and (math.fabs(self.depart - vaisseau.position) < 40):
            return True
            
class Boss():
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
        
