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
Icone_start = pygame.image.load('New Piskel.png')
Icone_start2 = pygame.image.load('New Piskel(1).png')


#iniciando o pygame
pygame.init()


#Icone do Jogo
pygame.display.set_icon(icone)

#Fixando FPS
clock = pygame.time.Clock()
clock.tick(60)

#Iniciar Display e set de Resolução RESOLUÇAO DEFINIDA EM 768x531 POR CAUSA DAS IMAGENS
gameDisplay = pygame.display.init()
screen = pygame.display.set_mode((768,531))
pygame.display.toggle_fullscreen()

#Shortcut pra Key
key = pygame.key

def Mouse():
    X,Y = pygame.mouse.get_pos()
    pygame.mouse.set_visible(False)





#Definir função menu
def Menu():
    Menu  = False
    while not Menu:
        screen.blit(Insper_background,[0, 0])
       
         
    
        for event in pygame.event.get():
                
                if key.get_pressed()[K_ESCAPE]:
                    Menu = True
                    pygame.quit()
                    
                if key.get_pressed()[K_F11]:
                    pygame.display.toggle_fullscreen()
                    
                if key.get_pressed()[K_1]:
                    Menu = True
                    
                if event.type == pygame.QUIT:
                    pygame.quit()
        pygame.display.update()
 

#definir função Jogo       
def game_loop():            
    #Working Condition
    Crashed = False
    while not Crashed:
        screen.blit(FabLab, [0, 0])
    
        
        for event in pygame.event.get():
            
            if key.get_pressed()[K_ESCAPE]:
                Crashed = True
            
            if key.get_pressed()[K_F11]:
                pygame.display.toggle_fullscreen()
                
            if event.type == QUIT:
                pygame.quit()
        pygame.display.update()
                
#Rodando o Jogo 
Mouse()
Menu()
game_loop() 
    