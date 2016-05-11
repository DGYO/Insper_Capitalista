# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 10:38:02 2016

@author: francisco
"""
import pygame
from pygame.locals import *
import shelve

    
   
# Imagens Importadas
Insper_background = pygame.image.load('teste.png')
icone = pygame.image.load('insperLogo.jpg')
aluno = pygame.image.load('alunocapitalistas.png')
dollar = pygame.image.load('Dollars.png')
FabLab = pygame.image.load('FabLab 8Bit.png')
Fabulas = pygame.image.load('Calculo.png')
Cafe = pygame.image.load("cafe.jpg")

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
                        
                        
                        
       
 
def Save(count,):
    SaveGameClick = shelve.open('InsperCap.Save 1')
    Count = SaveGameClick[count]
    






#definir função Jogo            

#variáveis
inflacaolivro = 1.0
inflacaocafe = 1.0   
#Working Condition
Crashed = False
count = 0
Multi = 1

    
    
    
while not Crashed:
    screen.blit(Insper_background, [0, 0])
    screen.blit(aluno,[-30,50])
    
    #cafe
    if count >= 300 * inflacaocafe:
        screen.blit(Cafe,[600,300])
        pygame.draw.rect(screen,(0,0,0),(600,300,225,225),1)
    Xmouse,Ymouse = Mouse()
    dinheiro(count)
    #aluno e livro
    if count >= 200 * inflacaolivro:
        screen.blit(Fabulas,[600,50])
        pygame.draw.rect(screen,(0,0,0),(600,50,225,225),1)
    pygame.draw.rect(screen, (0,0,0),(40,50,195,380),True)
    Xmouse,Ymouse = Mouse()
    dinheiro(count)
    
    
    for event in pygame.event.get():
        print(event)
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                Crashed = True
                pygame.quit()
            
            elif event.key == K_F11:
                pygame.display.toggle_fullscreen()
                
        elif event.type == QUIT:
            pygame.quit()
        
        elif event.type == MOUSEBUTTONUP:
            Xmouse,Ymouse = event.pos
            #Botao Aluno
            if 40+195 > Xmouse > 40:
                if 50+380 > Ymouse > 50:       
                    count += 1*Multi
                    
            #Botao Livro 
            if count >= 200 * inflacaolivro:
                if 600+225 > Xmouse > 600:
                    if 50+225 > Ymouse > 50:
                        if pygame.mouse.get_pressed()[0]:
                            Multi *= 2
                            count -= 200
                            inflacaolivro *= 1.5
            #Botao Cafe
            if count >= 300 * inflacaocafe:
                if 600+225 > Xmouse > 600:
                    if 300+225 > Ymouse > 300:
                        if pygame.mouse.get_pressed()[0]:
                            Multi *= 2
                            count -= 300
                            inflacaocafe *= 1.7        
    pygame.display.update()                
    clock.tick(60)
    

                
                
                


