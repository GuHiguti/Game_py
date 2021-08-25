import pygame
from pygame.locals import *
from sys import exit
import random
import math

#inicializar pygame
pygame.init()

#música de fundo
pygame.mixer.music.set_volume(0.1)
background_music = pygame.mixer.music.load('Audio/Background1.mp3')
pygame.mixer.music.play(-1)

#som de colisão
somzinho = pygame.mixer.Sound('Audio/Coin.wav')
somzinho.set_volume(0.15)

#variáveis
width = 640
height = 480

xobj = int(width/2)
yobj = int(height/2)

xm = random.randint(0, 610)
ym = random.randint(0, 450)

fonte = pygame.font.SysFont('arial',40,bold=True,italic=True)#fonte de texto
spd = 5 #velocidade objeto
pontos = 0

right = True
left = False
up = False
down = False

#configurar a tela
scr = pygame.display.set_mode((width, height))
pygame.display.set_caption("Jogo") #Nome da tela
relogio = pygame.time.Clock()

#loop principal
while True:
    relogio.tick(60) #frames per second
    scr.fill((250,250,250)) #clear screen
    mensagem = f'Pontos: {pontos}'
    texto = fonte.render(mensagem, True, (0,0,0)) #configurar texto

    #Events loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        
    #move object
    if pygame.key.get_pressed()[K_a]:
        right = False
        up = False
        down = False
        left = True
    if pygame.key.get_pressed()[K_d]:
        left = False
        up = False
        down = False
        right = True
    if pygame.key.get_pressed()[K_w]:
        right = False
        left = False
        down = False
        up = True
    if pygame.key.get_pressed()[K_s]:
        right = False
        left = False
        up = False
        down = True

    #move automatically
    if right:
        xobj += spd
    elif left:
        xobj -= spd
    elif up:
        yobj -= spd
    elif down:
        yobj += spd


    #formas na tela
    ret_amarelo = pygame.draw.rect(scr, (0,255,0), (xobj,yobj,30,30)) #draw rectangle
    ret_azul = pygame.draw.rect(scr,(255,0,0), (xm,ym,30,30))

    #configurar colisão
    if ret_amarelo.colliderect(ret_azul): 
        xm = random.randint(0, 610)
        ym = random.randint(0, 450)
        pontos += 1
        somzinho.play()

    #limites da tela
    if xobj + 15>= width:
        xobj = -15
    if yobj + 15 >= height:
        yobj = -15
    if xobj  < -15:
        xobj = width - 15
    if yobj < -15:
        yobj = height - 15

    #imprimir pontuação na tela
    scr.blit(texto, (450, 40))

    #atualizar tela 
    pygame.display.update()
