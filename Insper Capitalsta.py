# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *
import pickle
#import image 
#import time
    
   
# Imagens Importadas
Insper_background = pygame.image.load('teste.png')
icone = pygame.image.load('insperLogo.jpg')
aluno = pygame.image.load('alunocapitalistas.png')
alunoR = pygame.image.load('alunocapitalistasR.png')
dollar = pygame.image.load('Dollars.png')
FabLab = pygame.image.load('FabLab 8Bit.png')
Fabulas = pygame.image.load('Calculo.png')
FabulasBW = pygame.image.load('CalculoBW.png')
Cafe = pygame.image.load("cafe.jpg")
CafeBW = pygame.image.load("cafeBW.jpg")

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


#Shortcut pra Key
key = pygame.key

def Mouse():
    X,Y = pygame.mouse.get_pos()
    pygame.mouse.set_visible(True)
    return(X,Y)

def dinheiro(count):
    font = pygame.font.SysFont(None,50)
    text = font.render("Dollars:$"+str(count),True,(0,200,0))
    screen.blit(text,(40,165))

def contagem_livros(livros):
    font = pygame.font.SysFont(None,50)
    text = font.render("livros:"+str(livros),True,(0,200,0))
    screen.blit(text,(850,30))

def contagem_cafes(cafes):
    font = pygame.font.SysFont(None,50)
    text = font.render("Cafes:"+str(cafes),True,(0,200,0))
    screen.blit(text,(850,70))
 
def Save(count,inflacaocafe,inflacaolivro,Multi,livros,MultiT1,cafes):
    listData = [count,inflacaocafe,inflacaolivro,Multi,livros,MultiT1,cafes]
    outFile = open('DataSave.txt','wb')
    pickle.dump(listData, outFile)
    outFile.close()

def Load():
    inFile = open('DataSave.txt','rb')
    LoadList = pickle.load(inFile)
    inFile.close()
    return LoadList
    
def Reset():
    count = 0
    inflacaolivro = 1.0
    inflacaocafe = 1.0  
    Multi = 1
    MultiT1 = 1
    cafes = 0
    livros = 0
    return count,inflacaolivro,inflacaocafe,Multi,MultiT1,cafes,livros
    
    
    
    






#definir função Jogo            

#variáveis
inflacaolivro = 1.0
inflacaocafe = 1.0   
DINHEIROTEMPO = USEREVENT + 1 
pygame.time.set_timer(DINHEIROTEMPO, 1000)
#Working Condition
Crashed = False
count = 0 
Multi = 1
livros = 0
cafes = 0
MultiT1 = 1

    
    
    
while not Crashed:
    screen.blit(Insper_background, [0, 0])
    screen.blit(aluno,[-40,197])
    
    #cafe
    if count >= 300 * inflacaocafe:
        screen.blit(Cafe,[600,300])
        pygame.draw.rect(screen,(0,0,0),(600,300,225,225),1)
    elif count < 300 * inflacaocafe:
        screen.blit(CafeBW,[600,300])
        pygame.draw.rect(screen,(0,0,0),(600,300,225,225),1)
    Xmouse,Ymouse = Mouse()
    dinheiro(count)
    contagem_cafes(cafes)
    #aluno e livro
    if count >= 200 * inflacaolivro:
        screen.blit(Fabulas,[600,50])
        pygame.draw.rect(screen,(0,0,0),(600,50,225,225),1)
    
    elif count < 200 * inflacaolivro:
        screen.blit(FabulasBW,[600,50])
        pygame.draw.rect(screen,(0,0,0),(600,50,225,225),1)
    pygame.draw.rect(screen, (255,255,255),(30,197,195,380),True) #aluno
    dinheiro(count)
    contagem_livros(livros)
    
    for event in pygame.event.get():
        print(event)
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                Crashed = True
                pygame.quit()
            
            elif event.key == K_h:
                pygame.display.toggle_fullscreen()

            elif event.key == K_s:
                Save(count,inflacaocafe,inflacaolivro,Multi,livros,MultiT1,cafes)  
                
            elif event.key == K_l:
                count,inflacaocafe,inflacaolivro,Multi,livros,MultiT1,cafes = Load()
                
            elif event.key == K_r:
                count,inflacaocafe,inflacaolivro,Multi,MultiT1,cafes,livros = Reset()
                
        elif event.type == QUIT:
            pygame.quit()

        elif event.type == DINHEIROTEMPO:
            if cafes == 1:
                count += 1 
            elif cafes > 1:
                count += 1 + MultiT1    
        
        elif event.type == MOUSEBUTTONDOWN:
            if 30+195 > Xmouse > 30:
                if 197+380 > Ymouse > 197:
                    aluno =  alunoR
                    screen.blit(aluno,[-40,197])

        elif event.type == MOUSEBUTTONUP:
            Xmouse,Ymouse = event.pos
            if 30+195 > Xmouse > 30:
                if 197+380 > Ymouse > 197:
                    aluno = pygame.image.load('alunocapitalistas.png')
                    screen.blit(aluno,[-40,197])



        
            

            #Botao Aluno
            if 30+195 > Xmouse > 30:
                if 197+380 > Ymouse > 197:       
                    count += 1*Multi
                    
            #Botao Livro 
            if count >= 200 * inflacaolivro:
                if 600+225 > Xmouse > 600:
                    if 50+225 > Ymouse > 50:
                            livros += 1
                            Multi *= 2
                            count -= 200
                            inflacaolivro *= 1.5
            #Botao Cafe
            if count >= 300 * inflacaocafe:
                if 600+225 > Xmouse > 600:
                    if 300+225 > Ymouse > 300:
                        cafes += 1
                        MultiT1 *= 2
                        count -= 300
                        inflacaocafe *= 1.7  






                            
            
    pygame.display.update()                
    clock.tick(60)