import pygame # importation de la librairie pygame
import space
import sys # pour fermer correctement l'application

# lancement des modules inclus dans pygame
pygame.init() 

# création d'une fenêtre de 800 par 600
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Space Invaders") 
# chargement de l'image de fond
fond = pygame.image.load('Inferno.png')
fond = pygame.transform.scale(fond, (800, 600))
# creation du joueur
player = space.Joueur()
# creation de la balle
tir = space.Balle(player)
tir.etat = "chargee"
# creation des ennemis
listeEnnemis = []
for indice in range(space.Ennemi.NbEnnemis):
    vaisseau = space.Ennemi()
    listeEnnemis.append(vaisseau)
# Création du boss
boss = space.Boss()
# Création de la balle du boss
bossBullet = space.BalleBoss(boss)

# Création du texte pour afficher le score et les points de vie du boss
font = pygame.font.Font('freesansbold.ttf', 32)
#  Création du texte pour afficher les points de vie du joueur
fontPV = pygame.font.Font('freesansbold.ttf', 20)
#  Création du texte pour afficher le Game Over
fontGameOver = pygame.font.Font('freesansbold.ttf', 100)

clock = pygame.time.Clock()

### BOUCLE DE JEU  ###
running = True # variable pour laisser la fenêtre ouverte

while running : # boucle infinie pour laisser la fenêtre ouverte
    # dessin du fond
    screen.blit(fond,(0,0))
    
    # Affichage du score
    textScore = font.render("Score : " + str(player.score), True, (255,255,255))
    screen.blit(textScore, (600, 10))
    # Affichage des PV du joueur
    textPVPlayer = fontPV.render("PV restants : " + str(player.vie), True, (0,255,0))
    screen.blit(textPVPlayer, (10, 575))
    
    ### Gestion des événements  ###
    for event in pygame.event.get(): # parcours de tous les event pygame dans cette fenêtre
        if event.type == pygame.QUIT : # si l'événement est le clic sur la fermeture de la fenêtre
            running = False # running est sur False
            sys.exit() # pour fermer correctement
       
       # gestion du clavier
        if event.type == pygame.KEYDOWN : # si une touche a été tapée KEYUP quand on relache la touche
            if event.key == pygame.K_LEFT : # si la touche est la fleche gauche
                player.sens = "gauche" # on déplace le vaisseau de 1 pixel sur la gauche
            if event.key == pygame.K_RIGHT : # si la touche est la fleche droite
                player.sens = "droite" # on déplace le vaisseau de 1 pixel sur la gauche
            if event.key == pygame.K_SPACE : # espace pour tirer
                player.tirer()
                tir.etat = "tiree"

    ### Actualisation de la scene ###
    # Gestions des collisions
    for ennemi in listeEnnemis:
        if tir.toucher(ennemi):
            ennemi.disparaitre()
            player.marquer()
    # placement des objets
    # le joueur
    player.deplacer()
    screen.blit(tir.image,[tir.depart,tir.hauteur]) # appel de la fonction qui dessine la balle du joueur        
    # la balle
    tir.bouger()
    screen.blit(player.image,[player.position,500]) # appel de la fonction qui dessine le vaisseau du joueur
    # les ennemis
    for ennemi in listeEnnemis:
        ennemi.avancer()
        screen.blit(ennemi.image,[ennemi.depart, ennemi.hauteur]) # appel de la fonction qui dessine les ennemis
        # Inflige des degats au joueur lorsqu'il est touché
        if ennemi.degats(player):
            player.losePV()
            ennemi.disparaitre()
        if ennemi.hauteur > 600 : # Fait disparaitre l'ennemi s'il sort de l'ecran
            ennemi.disparaitre()
    # Apparition d'un boss si score est supérieur à 25
    if player.score >= 25:
        # Affichage des points de vie du boss
        textPV = font.render("PV : " + str(boss.vie), True, (255,255,0))
        screen.blit(textPV, (325, 10))
        
        boss.avancer()
        screen.blit(boss.image,[boss.depart,boss.hauteur]) # Appel de la fonction qui dessine le boss
        
        # Fait tirer la balle du boss
        bossBullet.tirBoss()
        if bossBullet.etat == "chargee":
            bossBullet.etat = "tiree"
            bossBullet.tirBoss()
        
        screen.blit(bossBullet.image,[bossBullet.depart,bossBullet.hauteur]) # Appel de la fonction qui dessine la balle du boss
        
        # Enleve de la vie au boss s'il se fait toucher par une balle
        if tir.toucherBoss(boss):
            boss.vie -= 1
            
        # Enleve de la vie au joueur s'il se fait toucher par une balle du boss
        if bossBullet.toucherJoueur(player):
            player.losePV()
            
        # Fait disparaitre le boss une fois que ses PV passent à 0 et augmente le score du joueur à l'infini
        if boss.mort(): 
            player.score += 25
    # Affiche un Game Over si les PV du joueur passent à 0
    if player.PV():
        textGameOver = fontGameOver.render("Game Over", True, (255,0,0))
        screen.blit(textGameOver, (130, 250))
        
    clock.tick(200)
            
    pygame.display.update() # pour ajouter tout changement à l'écran
