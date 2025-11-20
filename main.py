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

# Ball dimensioni e velocità
ball_size = 8
ball_speed_x = 3
ball_speed_y = 3

# Posizione iniziale ball
ball_x = width // 2 - ball_size // 2
ball_y = height // 2 - ball_size // 2

# Punteggio
score1 = 0
score2 = 0
font = pygame.font.Font(None, 36)

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

# Limiti per le paddle
    if player1_pos < 0:
        player1_pos = 0
    if player1_pos + paddle_height > height:
        player1_pos = height - paddle_height
        
    if player2_pos < 0:
        player2_pos = 0
    if player2_pos + paddle_height > height:
        player2_pos = height - paddle_height

# Logica della palla
    ball_x += ball_speed_x
    ball_y += ball_speed_y

# Collisioni con i bordi
    if ball_y < 0 or ball_y + ball_size > height:
        ball_speed_y *= -1

# Collisioni con le paddle
    if (ball_x < paddle_width and 
        player1_pos <= ball_y <= player1_pos + paddle_height):
        ball_speed_x *= -1
        ball_x = paddle_width

    if (ball_x + ball_size > width - paddle_width and
        player2_pos <= ball_y <= player2_pos + paddle_height):
        ball_speed_x *= -1
        ball_x = width - paddle_width - ball_size

# Punteggio
    if ball_x < 0:
        score2 += 1
        ball_x = width // 2 - ball_size // 2
        ball_y = height // 2 - ball_size // 2
        ball_speed_x *= -1
        ball_speed_y *= -1

    if ball_x + ball_size > width:
        score1 += 1
        ball_x = width // 2 - ball_size // 2
        ball_y = height // 2 - ball_size // 2
        ball_speed_x *= -1
        ball_speed_y *= -1

# disegna tutto
    screen.fill(BLACK)

# disegna paddle
    pygame.draw.rect(screen, WHITE, (0, player1_pos, paddle_width, paddle_height))
    pygame.draw.rect(screen, WHITE, (width - paddle_width, player2_pos, paddle_width, paddle_height))
    
# Ball
    pygame.draw.circle(screen, WHITE, (ball_x + ball_size//2, ball_y + ball_size//2), ball_size//2)

# Punteggio
    score_display = font.render(f"{score1} - {score2}", True, WHITE)
    screen.blit(score_display, (width//2 - 40, 20))

# aggiorna il loop dello schermo
    pygame.display.flip()
    clock.tick(60)

pygame.quit()