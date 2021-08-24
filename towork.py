import pygame
from pygame.locals import *
from sys import exit
import random
import math

pygame.init()

width = 640
height = 480
on = True

scr = pygame.display.set_mode((width, height))
pygame.display.set_caption("Jogo")

while on:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    pygame.display.update()
