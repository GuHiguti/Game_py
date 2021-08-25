import pygame
from pygame.locals import *
from sys import exit
import random
import math

#inicializar pygame
pygame.init()

#resetar
#def reset():


#música de fundo
pygame.mixer.music.set_volume(0.1)
background_music = pygame.mixer.music.load('Audio/Background1.mp3')
pygame.mixer.music.play(-1)

#som de colisão
somzinho = pygame.mixer.Sound('Audio/Coin.wav')
somzinho.set_volume(0.15)

#som de morte
morte = pygame.mixer.Sound('Audio/Death1.wav')
morte.set_volume(0.2)

#variáveis
width = 640
height = 480

xobj = int(width/2)
yobj = int(height/2)

xm = random.randint(0, 610)
ym = random.randint(0, 450)

fonte = pygame.font.SysFont('arial',40,bold=True,italic=True)#fonte de texto
spd_inicial = 20
spd = spd_inicial #velocidade objeto
pontos = 1

lista_corpo = []

right = True
left = False
up = False
down = False

#configurar a tela
scr = pygame.display.set_mode((width, height))
pygame.display.set_caption("Jogo") #Nome da tela
relogio = pygame.time.Clock()

#fazer a cobra crescer
def cresce(lista_corpo):
    for pos in lista_corpo:
        corpo = pygame.draw.rect(scr,(0,255,0),(pos[0],pos[1],30,30))

#loop principal
while True:
    relogio.tick(int(260/spd_inicial)) #frames per second
    scr.fill((250,250,250)) #clear screen
    mensagem = f'Pontos: {pontos-1}'
    texto = fonte.render(mensagem, True, (0,0,0)) #configurar texto

    #Events loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        elif pygame.key.get_pressed()[K_r]:
            xobj = int(width/2)
            yobj = int(height/2)
            pontos = 1
            spd = spd_inicial
            right = True
            left = False
            up = False
            down = False
            lista_corpo = []
        
    #move object
    if pygame.key.get_pressed()[K_a] and right==False:
        up = False
        down = False
        left = True
    if pygame.key.get_pressed()[K_d] and left==False:
        up = False
        down = False
        right = True
    if pygame.key.get_pressed()[K_w] and down==False:
        right = False
        left = False
        up = True
    if pygame.key.get_pressed()[K_s] and up==False:
        right = False
        left = False
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
    cabeca_cobra = pygame.draw.rect(scr, (0,255,0), (xobj,yobj,30,30)) #draw rectangle
    comida = pygame.draw.rect(scr,(255,0,0), (xm,ym,30,30))

    #configurar colisão com comida
    if cabeca_cobra.colliderect(comida): 
        xm = random.randint(0, 610)
        ym = random.randint(0, 450)
        pontos += 1
        somzinho.play()
    
    #morte
    for local in lista_corpo:
        if local[0]==xobj and local[1]==yobj:
            spd = 0
            morte.play()
            #reset()

    #desenhando o corpo cobra
    lista_cabeca = []
    lista_cabeca.append(xobj)
    lista_cabeca.append(yobj)
    lista_corpo.append(lista_cabeca)
    corpo = cresce(lista_corpo)

    #Limitar o tamanho do corpo da cobra
    if len(lista_corpo) > int(35/spd_inicial * pontos):
        lista_corpo.pop(0)

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
