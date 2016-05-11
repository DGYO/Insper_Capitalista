# -*- coding: utf-8 -*-

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
    screen.blit(text,(40,165))

def contagem_livros(livros):
    font = pygame.font.SysFont(None,50)
    text = font.render("livros:"+str(livros),True,(0,200,0))
    screen.blit(text,(850,30))
 
def Save(count,inflacaocafe,inflacaolivro,Multi):
    SaveGameClick = shelve.open('InsperCap.Save 1')
    SaveGameClick['count'] = count
    SaveGameClick['inflacaocafe'] = inflacaocafe 
    SaveGameClick['inflacaolivro'] = inflacaolivro 
    SaveGameClick['Multi'] = Multi

    SaveGameClick.close()
    
def Load():
    SaveGameClick = shelve.open('InsperCap.Save 1')
    count = SaveGameClick['count']
    inflacaocafe = SaveGameClick['inflacaocafe']
    inflacaolivro = SaveGameClick['inflacaolivro']
    Multi = SaveGameClick['Multi']
    SaveGameClick.close()
    return count,inflacaocafe,inflacaolivro,Multi
    
def Reset():
    count = 0
    inflacaolivro = 1.0
    inflacaocafe = 1.0  
    Multi = 1
    return count,inflacaolivro,inflacaocafe,Multi
    
    
    
    






#definir função Jogo            

#variáveis
inflacaolivro = 1.0
inflacaocafe = 1.0   
#Working Condition
Crashed = False
count = 0
Multi = 1
livros = 0

    
    
    
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
    #aluno e livro
    if count >= 200 * inflacaolivro:
        screen.blit(Fabulas,[600,50])
        pygame.draw.rect(screen,(0,0,0),(600,50,225,225),1)
    
    elif count < 200 * inflacaolivro:
        screen.blit(FabulasBW,[600,50])
        pygame.draw.rect(screen,(0,0,0),(600,50,225,225),1)
    pygame.draw.rect(screen, (0,0,0),(30,197,195,380),True)
    dinheiro(count)
    contagem_livros(livros)
    
    for event in pygame.event.get():
        print(event)
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                Crashed = True
                pygame.quit()
            
            elif event.key == K_F11:
                pygame.display.toggle_fullscreen()
            
            elif event.key == K_s:
                Save(count,inflacaocafe,inflacaolivro)    
                
                
            elif event.key == K_s:
                Save(count,inflacaocafe,inflacaolivro,Multi)  
                
            elif event.key == K_l:
                count, inflacaocafe, inflacaolivro , Multi = Load()
                
            elif event.key == K_r:
                count, inflacaocafe, inflacaolivro , Multi = Reset()
                
        elif event.type == QUIT:
            pygame.quit()
        
        elif event.type == MOUSEBUTTONUP:
            Xmouse,Ymouse = event.pos
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
                        
                            Multi *= 2
                            count -= 300
                            inflacaocafe *= 1.7  
                            
            
    pygame.display.update()                
    clock.tick(60)
                
                
                


