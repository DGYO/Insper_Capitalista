# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 10:38:02 2016

@author: francisco
"""
import pygame
from pygame.locals import *


    
    
# Imagens Importadas
Insper_background = pygame.image.load('8-Bit-Insper1.png')
icone = pygame.image.load('insperLogo.jpg')
aluno = pygame.image.load('Aluno.png')
dollar = pygame.image.load('Dollars.png')
FabLab = pygame.image.load('FabLab 8Bit.png')

#Icone do Jogo
pygame.display.set_icon(icone)

#iniciando o pygame
pygame.init()



clock = pygame.time.Clock()

#Iniciar Display e set de Resolução RESOLUÇAO DEFINIDA EM 768x531 POR CAUSA DAS IMAGENS
gameDisplay = pygame.display.init()
screen = pygame.display.set_mode((768,531))

#Shortcut pra Key
key = pygame.key

#Working Condition
Crashed = False



while not Crashed:
    screen.blit(Insper_background, [0, 0])

    
    for event in pygame.event.get():
        
        if key.get_pressed()[K_ESCAPE]:
            Crashed = True
        
        if key.get_pressed()[K_F11]:
            pygame.display.toggle_fullscreen()
