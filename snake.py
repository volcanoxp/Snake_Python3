#Author: Jose Galarza

import pygame
import random

pygame.init()

size = WEIGTH, HEIGHT = 400, 400

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()


font = pygame.font.Font('freesansbold.ttf',30)
score = 0


state_screen = True

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

POS_X = WEIGTH/2
POS_Y = HEIGHT/2

speedy = 10

speedy_X = speedy
speedy_Y = 0


def comida_aleatoria(WEIGHT, HEIGHT):
    x = random.randint(10,(WEIGHT-20)/10)*10
    y = random.randint(10,(HEIGHT-20)/10)*10
    return x, y

estado_comida = True
posX_comida, posY_comida = comida_aleatoria(WEIGTH,HEIGHT)
snake = [[POS_X,POS_Y]]



while state_screen:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state_screen = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_RIGHT and speedy_X != -speedy:
                speedy_X = +speedy
                speedy_Y = 0

            if event.key == pygame.K_LEFT and speedy_X != speedy:
                speedy_X = -speedy
                speedy_Y = 0

            if event.key == pygame.K_DOWN and speedy_Y != -speedy:
                speedy_X = 0
                speedy_Y = +speedy

            if event.key == pygame.K_UP and speedy_Y != speedy:
                speedy_X = 0
                speedy_Y = -speedy

       
    screen.fill(WHITE)

    #BORDERES
    pygame.draw.rect(screen,BLUE,[0,0,WEIGTH,10])
    pygame.draw.rect(screen,BLUE,[WEIGTH-10,0,10,HEIGHT])
    pygame.draw.rect(screen,BLUE,[0,0,10,HEIGHT])
    pygame.draw.rect(screen,BLUE,[0,HEIGHT-10,WEIGTH,10])

              
    for sn in snake:
        pygame.draw.rect(screen,BLACK, [sn[0], sn[1],10,10], 2)




    text_score = str(score)

    OUT_score = font.render(text_score,False, RED)
    screen.blit(OUT_score,( WEIGTH/2, 10))

    # ACTUALIZACIÓN DE ESTADOS SNAKE
    i = len(snake) - 1
    while i > 0 :
        snake[i][0] = snake[i-1][0]
        snake[i][1] = snake[i-1][1]
        i -= 1

    # Dibujo de la comida aleatoria
    pygame.draw.rect(screen,BLACK,[posX_comida,posY_comida,10,10])

    

    
    if POS_X == posX_comida and POS_Y == posY_comida:
        posX_comida, posY_comida = comida_aleatoria(WEIGTH, HEIGHT)
        snake.append([POS_X,POS_Y])
        score += 1

    POS_X += speedy_X
    POS_Y += speedy_Y
    snake[0][0] = POS_X
    snake[0][1] = POS_Y

    # deteccion de colisición
    try:
        for x in snake[1:]:
            if snake[0] == x:
                snake=snake[len(snake):]
                raise SnakeVacio

        if snake[0][0] == 0 or snake[0][1] == 0  or snake[0][0] == WEIGTH-10 or snake[0][1] == HEIGHT-10:
            snake=snake[len(snake):]
            raise SnakeVacio
    except:

        POS_X = WEIGTH/2
        POS_Y = HEIGHT/2
        snake.append([POS_X,POS_Y])
        score=0

        text_lose = 'Perdiste'

        OUT_lose = font.render(text_lose,False, RED)
        screen.blit(OUT_lose,(POS_X-50,POS_Y-30))
        pygame.display.flip()
        pygame.time.delay(1000)
        #Renovamos la posición de la comida
        posX_comida, posY_comida = comida_aleatoria(WEIGTH, HEIGHT)
    
    
    pygame.display.flip()
    clock.tick(30)
    
pygame.quit()
