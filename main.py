import pygame
from pygame.locals import *

# inizializza pygame
pygame.init()

# imposta le dimensioni della finestra
width = 800
height = 400

# crea la finestra e assegna il nome caption
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong-noOOp-V1.0")

# definizione colori
BLACK = (0,0,0)
WHITE = (255,255,255)

# genera clock per il framerate
clock = pygame.time.Clock()

running = True

while running:
    #gestione degli eventi
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

# disegna tutto
    screen.fill(BLACK)

# aggiorna loop dello schermo
    pygame.display.flip()
    clock.tick(60)

pygame.quit()