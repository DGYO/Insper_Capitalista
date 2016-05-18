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
calculosemdinheiro = pygame.image.load('Calculosemdinheiro.png')
FabulasBW = pygame.image.load('CalculoBW.png')
Cafe = pygame.image.load("cafe.jpg")
imagembotao = pygame.image.load("botao.png")
imagembotaoapertado = pygame.image.load("botaoapertado.png")
botaosemdinheiro = pygame.image.load("botaosemdinheiro.png")
#Botao Start
Icone_start = pygame.image.load('New Piskel.png')
Icone_start2 = pygame.image.load('New Piskel(1).png')


#iniciando o pygame
pygame.init()
pygame.font.init()

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
    font = pygame.font.SysFont("heineken",50)
    font.set_bold(True)
    text = font.render("Dollars:$"+str(count),True,(0,200,0))
    screen.blit(text,(40,165))

def contagem_livros(livros):
    font = pygame.font.SysFont("heineken",50)
    text = font.render("livros:"+str(livros),True,(0,200,0))
    screen.blit(text,(850,30))

def contagem_cafes(cafes):
    font = pygame.font.SysFont("    heineken",50)
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
    screen.blit(imagembotao,[600,75])
    screen.blit(imagembotao,[600,150])
    screen.blit(imagembotao,[600,225])
    screen.blit(imagembotao,[600,300])
    screen.blit(imagembotao,[600,375])
    screen.blit(imagembotao,[600,450])
    screen.blit(imagembotao,[600,525])
    screen.blit(imagembotao,[600,600])
    screen.blit(imagembotao,[600,675])


    #aluno e livro
    if count >= 200 * inflacaolivro:
        screen.blit(imagembotao,[600,0])
        screen.blit(Fabulas,[610,10])
    elif count < 200 * inflacaolivro:
        screen.blit(botaosemdinheiro,[600,0])
        screen.blit(calculosemdinheiro,[610,10])
        
    dinheiro(count)
    contagem_livros(livros)

    #cafe
    if count >= 300 * inflacaocafe:
        pygame.draw.rect(screen,(0,0,0),(600,300,225,225),1)
    
    elif count < 300 * inflacaocafe:
        screen.blit(Cafe,[600,300])
        #screen.blit(botaosemdinheiro,[600,75])
       
    Xmouse,Ymouse = Mouse()
    dinheiro(count)
    contagem_cafes(cafes)
    
    
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
            if 600+500 > Xmouse > 600:
                if 0+75 > Ymouse > 0:
                    imagembotao = imagembotaoapertado
                    screen.blit(imagembotao,[600,0])

        elif event.type == MOUSEBUTTONUP:
            Xmouse,Ymouse = event.pos
            if 30+195 > Xmouse > 30:
                if 197+380 > Ymouse > 197:
                    aluno = pygame.image.load('alunocapitalistas.png')
                    screen.blit(aluno,[-40,197])
            if 600+500 > Xmouse > 600:
                if 0+75 > Ymouse > 0:
                    imagembotao = pygame.image.load("botao.png")   
                    screen.blit(imagembotao,[600,0]) 



        
            

            #Botao Aluno
            if 30+195 > Xmouse > 30:
                if 197+380 > Ymouse > 197:       
                    count += 1*Multi
                    
            #Botao Livro 
            if count >= 200 * inflacaolivro:
                if 600+500 > Xmouse > 600:
                    if 0+75 > Ymouse > 0:
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