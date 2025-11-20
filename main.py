import pygame
from pygame.locals import *

# inizializza pygame
pygame.init()

# imposta le dimensioni della finestra
width = 800  #largezza
height = 400 #altezza

# crea la finestra e assegna il nome caption
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong-NoOOp-V1.0")

# definizione colori
BLACK = (0,0,0)
WHITE = (255,255,255)

# dimensioni paddle
paddle_width = 10
paddle_height = 60

# posizione iniziale paddle
player1_pos = height // 2 - paddle_height // 2
player2_pos = height // 2 - paddle_height // 2

# velocita paddle
paddle_speed = 5

# genera clock per il framerate
clock = pygame.time.Clock()

running = True

while running:
    #gestione degli eventi
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # input del giocatore
    keys = pygame.key.get_pressed()

    # paddle 1 tasti w+s
    if keys[K_w]:
        player1_pos -= paddle_speed
    if keys[K_s]:
        player1_pos += paddle_speed

    # paddle 2 tasti up+down
    if keys[K_UP]:
        player2_pos -= paddle_speed
    if keys[K_DOWN]:
        player2_pos += paddle_speed

# disegna tutto
    screen.fill(BLACK)

# disegna paddle
    pygame.draw.rect(screen, WHITE, (0, player1_pos, paddle_width, paddle_height))
    pygame.draw.rect(screen, WHITE, (width - paddle_width, player2_pos, paddle_width, paddle_height))

# aggiorna il loop dello schermo
    pygame.display.flip()
    clock.tick(60)

pygame.quit()