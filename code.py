import pygame
import random

# Setup de base
pygame.init()
LARG = 500
HAUT = 600
fenetre = pygame.display.set_mode((LARG, HAUT))
pygame.display.set_caption("Mon Premier Jeu Space")

# Couleurs
NOIR = (0, 0, 0)
BLANC = (255, 255, 255)
ROUGE = (255, 50, 50)

# Variables du joueur
px = 250
py = 530
vitesse = 7

# Listes pour les trucs qui bougent
missiles = []
ennemis = []
clock = pygame.time.Clock()
score = 0

# Police pour le score
font = pygame.font.SysFont("monospace", 25)

continuer = True
while continuer:
    fenetre.fill(NOIR)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = False
            
        # Tirer avec Espace
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                missiles.append([px + 15, py])

    # Mouvement
    touches = pygame.key.get_pressed()
    if touches[pygame.K_LEFT] and px > 0:
        px -= vitesse
    if touches[pygame.K_RIGHT] and px < LARG - 30:
        px += vitesse

    # Création des ennemis (un peu au pif)
    if random.randint(1, 30) == 1:
        ennemis.append([random.randint(0, LARG-30), -40])

    # Update missiles
    for m in missiles[:]:
        m[1] -= 10
        if m[1] < 0:
            missiles.remove(m)

    # Update ennemis
    for e in ennemis[:]:
        e[1] += 5
        if e[1] > HAUT:
            ennemis.remove(e)
            score -= 1 # On perd des points si on les rate

        # Check collision avec le joueur
        if px < e[0] + 30 and px + 30 > e[0] and py < e[1] + 30 and py + 30 > e[1]:
            print("Game Over!")
            continuer = False

    # Check collision missile/ennemi
    for m in missiles[:]:
        for e in ennemis[:]:
            if m[0] < e[0] + 30 and m[0] + 10 > e[0] and m[1] < e[1] + 30 and m[1] + 10 > e[1]:
                if e in ennemis: ennemis.remove(e)
                if m in missiles: missiles.remove(m)
                score += 10

    # Dessin
    pygame.draw.rect(fenetre, (0, 200, 0), (px, py, 30, 30)) # Le joueur
    for m in missiles:
        pygame.draw.rect(fenetre, BLANC, (m[0], m[1], 5, 10))
    for e in ennemis:
        pygame.draw.rect(fenetre, ROUGE, (e[0], e[1], 30, 30))

    texte = font.render(f"Points: {score}", True, BLANC)
    fenetre.blit(texte, (10, 10))

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
