# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 10:38:02 2016

@author: francisco
"""
import pygame
from pygame.locals import *


    
   
# Imagens Importadas
Insper_background = pygame.image.load('8-Bit-Insper1.jpg')
icone = pygame.image.load('insperLogo.jpg')
aluno = pygame.image.load('alunocapitalistas.png')
dollar = pygame.image.load('Dollars.png')
FabLab = pygame.image.load('FabLab 8Bit.png')
Fabulas = pygame.image.load('Calculo.png')

#Botao Start
Icone_start = pygame.image.load('New Piskel.png')
Icone_start2 = pygame.image.load('New Piskel(1).png')


#iniciando o pygame
pygame.init()

green = (0,0,0)


#Icone do Jogo
pygame.display.set_icon(icone)

#Fixando FPS
clock = pygame.time.Clock()
clock.tick(60)

#Iniciar Display e set de Resolução RESOLUÇAO DEFINIDA EM 768x531 POR CAUSA DAS IMAGENS
gameDisplay = pygame.display.init()
screen = pygame.display.set_mode((1024,768))
#pygame.display.toggle_fullscreen()

#Shortcut pra Key
key = pygame.key

def Mouse():
    X,Y = pygame.mouse.get_pos()
    pygame.mouse.set_visible(True)
    return(X,Y)

def dinheiro(count):
    font = pygame.font.SysFont(None,50)
    text = font.render("Dollars:$"+str(count),True,(0,200,0))
    screen.blit(text,(50,20))


#Definir função menu
def Menu():
    Menu  = False
    Xmouse,Ymouse = Mouse()
    while not Menu:
        
        screen.blit(FabLab,[0, 0])
        screen.blit(Icone_start2,[400,50])
        pygame.draw.rect(screen,(0,0,0),(463,338,898,449),1)
    
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
        
                 #Botao Start
                if 1361 > Xmouse > 463:
                    if 787 > Ymouse > 338:
                        if pygame.mouse.get_pressed()[0]:
                            Menu = True
                        
                        
                        
        pygame.display.update()
 

#definir função Jogo       
def game_loop():     



       
    #Working Condition
    Crashed = False
    count = 0
    Multi = 1
    
    
    
    
    while not Crashed:
        screen.blit(Insper_background, [0, 0])
        screen.blit(aluno,[-30,50])
        
        if count >= 200:
            screen.blit(Fabulas,[600,50])
            pygame.draw.rect(screen,(0,0,0),(600,50,225,225),1)
        pygame.draw.rect(screen, (0,0,0),(40,50,195,380),True)
        Xmouse,Ymouse = Mouse()
        dinheiro(count)
        for event in pygame.event.get():
            print(event)
            if key.get_pressed()[K_ESCAPE]:
                Crashed = True
                pygame.quit()
            
            if key.get_pressed()[K_F11]:
                pygame.display.toggle_fullscreen()
                
            if event.type == QUIT:
                pygame.quit()
        
            #Botao Aluno
            if 40+195 > Xmouse > 40:
                if 50+380 > Ymouse > 50:
                    if pygame.mouse.get_pressed()[0]:
                        count += 1*Multi
                        break
            #Botao Livro 
            if count >= 200:
                if 600+225 > Xmouse > 600:
                    if 50+225 > Ymouse > 50:
                        if pygame.mouse.get_pressed()[0]:
                            Multi *= 2
                            count -= 200
        pygame.display.update()                
        
        

                
                
                
#Rodando o Jogo
game_loop() 
