import pygame
from pygame.locals import *
from sys import exit
import random
import math

#inicializar pygame
pygame.init()

#variáveis
width = 640
height = 480

xobj = width/2
yobj = height/2

xb = random.randint(0, 610)
yb = random.randint(0, 450)

fonte = pygame.font.SysFont('arial',40,bold=True,italic=True)#fonte de texto
spd = 5 #velocidade objeto
pontos = 0

#configurar a tela
scr = pygame.display.set_mode((width, height))
pygame.display.set_caption("Jogo") #Nome da tela
relogio = pygame.time.Clock()

#loop principal
while True:
    relogio.tick(60) #frames per second
    scr.fill((0,0,0)) #clear screen
    mensagem = f'Pontos: {pontos}'
    texto = fonte.render(mensagem, True, (255,255,255)) #configurar texto

    #Events loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    #move object
    if pygame.key.get_pressed()[K_a]:
        xobj -= spd
    if pygame.key.get_pressed()[K_d]:
        xobj += spd
    if pygame.key.get_pressed()[K_w]:
        yobj -= spd
    if pygame.key.get_pressed()[K_s]:
        yobj += spd

    #formas na tela
    ret_amarelo = pygame.draw.rect(scr, (255,205,0), (xobj,yobj,30,30)) #draw rectangle
    ret_azul = pygame.draw.rect(scr,(0,0,255), (xb,yb,30,30))

    #configurar colisão
    if ret_amarelo.colliderect(ret_azul):
        print("colidiu")        
        xb = random.randint(0, 610)
        yb = random.randint(0, 450)
        pontos += 1

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
