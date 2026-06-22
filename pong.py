# Requiere pygame instalado: pip install pygame y Python 3.12 Prueba
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600)) #Tamaño de la ventana
clock = pygame.time.Clock() #Frames por segundo del juegp
font = pygame.font.Font(None, 75) #Tamaño de la fuente para el marcador

ball = pygame.Rect(400, 300, 20, 20) #Tamaño de la pelota
player1 = pygame.Rect(50, 250, 10, 100) #Tamaño de la paleta del jugador 1
player2 = pygame.Rect(740, 250, 10, 100) #Tamaño de la paleta del jugador 2
ball_speed = [5, 5] #Velocidad de la pelota
score1, score2 = 0, 0 #Marcador de los jugadores

running = True
while running:
    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Movimiento paletas
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]: player1.y -= 5 #Movimiento hacia arriba de la paleta del jugador 1
    if keys[pygame.K_s]: player1.y += 5 #Movimiento hacia abajo de la paleta del jugador 1
    if keys[pygame.K_UP]: player2.y -= 5 #Movimiento hacia arriba de la paleta del jugador 2
    if keys[pygame.K_DOWN]: player2.y += 5 #Movimiento hacia abajo de la paleta del jugador 2

    # Movimiento pelota
    ball.x += ball_speed[0] #Movimiento horizontal de la pelota
    ball.y += ball_speed[1] #Movimiento vertical de la pelota

    # Colisiones
    if ball.top <= 0 or ball.bottom >= 600: #Rebote de la pelota en los bordes superior e inferior
        ball_speed[1] = -ball_speed[1] #Rebote vertical
    if ball.colliderect(player1) or ball.colliderect(player2): #Rebote de la pelota en las paletas
        ball_speed[0] = -ball_speed[0] #Rebote horizontal

    # Puntos
    if ball.left <= 0: #Si la pelota sale por la izquierda, el jugador 2 anota un punto
        score2 += 1 #Si la pelota sale por la izquierda, el jugador 2 anota un punto
        ball.center = (400, 300) #Reinicia la posición de la pelota al centro de la pantalla
    if ball.right >= 800: #Si la pelota sale por la derecha, el jugador 1 anota un punto
        score1 += 1 #Si la pelota sale por la derecha, el jugador 1 anota un punto
        ball.center = (400, 300) #Reinicia la posición de la pelota al centro de la pantalla

    # Dibujar
    screen.fill((0, 0, 0)) 
    pygame.draw.rect(screen, (255, 255, 255), player1) #Dibuja la paleta del jugador 1
    pygame.draw.rect(screen, (255, 255, 255), player2) #Dibuja la paleta del jugador 2
    pygame.draw.ellipse(screen, (255, 255, 255), ball) #Dibuja la pelota

    # Marcador
    text1 = font.render(str(score1), True, (255,255,255)) #Dibuja el marcador del jugador 1
    text2 = font.render(str(score2), True, (255,255,255)) #Dibuja el marcador del jugador 2
    screen.blit(text1, (250, 10)) #Dibuja el marcador del jugador 1
    screen.blit(text2, (500, 10)) #Dibuja el marcador del jugador 2

    pygame.display.flip() #Actualiza la pantalla
    clock.tick(60) #Frames por segundo del juego

pygame.quit()
