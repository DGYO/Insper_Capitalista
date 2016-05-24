# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *
# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *
import pickle
#import image 
#import time
    
   
# Imagens Importadas
Insper_background = pygame.image.load('teste.png')
#Insper_background2 = pygame.image.load('teste2.png')
icone = pygame.image.load('insperLogo.jpg')
aluno = pygame.image.load('alunocapitalistas.png')
alunoR = pygame.image.load('alunocapitalistasR.png')
dollar = pygame.image.load('Dollars.png')
FabLab = pygame.image.load('FabLab 8Bit.png')
Fabulas = pygame.image.load('Calculo.png')
calculosemdinheiro = pygame.image.load('Calculosemdinheiro.png')
FabulasBW = pygame.image.load('CalculoBW.png')
Cafe = pygame.image.load("coffe.png")
cafesemdinheiro = pygame.image.load("cafesemdinheiro.png")
botaosemdinheiro = pygame.image.load("botaosemdinheiro.png")
imagemacai = pygame.image.load("acai.png")
acaisemdinheiro = pygame.image.load("acaisemdinheiro.png")
imagemcomputer = pygame.image.load("computer.png")
computersemdinheiro = pygame.image.load("computersemdinheiro.png")
imagemninja = pygame.image.load("ninjanerd.png")
ninjasemdinheiro = pygame.image.load("ninjanerdsemdinheiro.png")
imagemcar = pygame.image.load("car.png")
carsemdinheiro = pygame.image.load("carsemdinheiro.png")
imagemprofessor = pygame.image.load("professor.png")
professorsemdinheiro = pygame.image.load("professorsemdinheiro.png")
imagemfablab = pygame.image.load("fablab.png")
fablabsemdinheiro = pygame.image.load("fablabsemdinheiro.png")
imgaematletica = pygame.image.load("Atletica.png")
atleticasemdinheiro = pygame.image.load("Atleticasemdinheiro.png")
imageminsper = pygame.image.load("insperLogo.png")
insperLogosemdinheiro = pygame.image.load("insperLogosemdinheiro.png")
retangulo = pygame.image.load("rect.png")
#oficina = pygame.image.load("oficina.png")

#Botoes loja
imagembotao1 = pygame.image.load("botao.png")
imagembotao2 = pygame.image.load("botao.png")
imagembotao3 = pygame.image.load("botao.png")
imagembotao4 = pygame.image.load("botao.png")
imagembotao5 = pygame.image.load("botao.png")
imagembotao6 = pygame.image.load("botao.png")
imagembotao7 = pygame.image.load("botao.png")
imagembotao8 = pygame.image.load("botao.png")
imagembotao9 = pygame.image.load("botao.png")
imagembotao10 = pygame.image.load("botao.png")
imagembotaoapertado1 = pygame.image.load("botaoapertado.png")
imagembotaoapertado2 = pygame.image.load("botaoapertado.png")
imagembotaoapertado3 = pygame.image.load("botaoapertado.png")
imagembotaoapertado4 = pygame.image.load("botaoapertado.png")
imagembotaoapertado5 = pygame.image.load("botaoapertado.png")
imagembotaoapertado6 = pygame.image.load("botaoapertado.png")
imagembotaoapertado7 = pygame.image.load("botaoapertado.png")
imagembotaoapertado8 = pygame.image.load("botaoapertado.png")
imagembotaoapertado9 = pygame.image.load("botaoapertado.png")
imagembotaoapertado10 = pygame.image.load("botaoapertado.png")

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
screen = pygame.display.set_mode((1024,768),pygame.FULLSCREEN)
#screen = pygame.display.set_mode((1024,768))


#Shortcut pra Key
key = pygame.key

def Mouse():
    X,Y = pygame.mouse.get_pos()
    pygame.mouse.set_visible(True)
    return(X,Y)

def dinheiro(count):
    screen.blit(retangulo,(0,30))
    font = pygame.font.SysFont("Back to 1982" ,25)
    if count < 1000:    
        text = font.render("Dollars:$"+str('{0:,.1f}'.format(count)),True,(0,200,0))
    elif 1000 < count < 1000000:
        text = font.render("Dollars:$"+str('{0:,.2f}'.format(count/1000))+"K",True,(0,200,0))
    elif 1000000 < count < 1000000000:
        text = font.render("Dollars:$"+str('{0:,.2f}'.format(count/1000000))+"M",True,(0,200,0))
    elif 1000000000 < count < 1000000000000:
        text = font.render("Dollars:$"+str('{0:,.2f}'.format(count/1000000000))+"Bi",True,(0,200,0))
    elif 1000000000000 < count < 1000000000000000:
        text = font.render("Dollars:$"+str('{0:,.2f}'.format(count/1000000000000))+"T",True,(0,200,0))
    screen.blit(text,(10,50))

def contagem_livros(livros,precolivro,inflacaolivro):
    font = pygame.font.SysFont("Back to 1982",20)
    text = font.render("livros:"+str(livros),True,(0,0,0))
    if precolivro*inflacaolivro < 1000:    
        text2 = font.render("Preco:$"+str('{0:,.1f}'.format(precolivro*inflacaolivro)),True,(0,0,0))
    elif 1000 < precolivro*inflacaolivro < 1000000:
        text2 = font.render("Preco:$"+str('{0:,.2f}'.format(precolivro*inflacaolivro/1000))+"K",True,(0,0,0))
    elif 1000000 < precolivro*inflacaolivro < 1000000000:
        text2 = font.render("Preco:$"+str('{0:,.2f}'.format(precolivro*inflacaolivro/1000000))+"M",True,(0,0,0))
    elif 1000000000 < precolivro*inflacaolivro < 1000000000000:
        text2 = font.render("Preco:$"+str('{0:,.2f}'.format(precolivro*inflacaolivro/1000000000))+"Bi",True,(0,0,0))
    elif 1000000000000 < precolivro*inflacaolivro < 1000000000000000:
        text2 = font.render("Preco:$"+str('{0:,.2f}'.format(precolivro*inflacaolivro/1000000000000))+"T",True,(0,0,0))
    screen.blit(text,(850,15))
    screen.blit(text2,(800,40))

def contagem_cafes(cafes,precocafe,inflacaocafe):
    font = pygame.font.SysFont("Back to 1982",20)
    text = font.render("Cafes:"+str(cafes),True,(0,0,0))
    if precocafe*inflacaocafe < 1000:    
        text2 = font.render("Preco:$"+str('{0:,.1f}'.format(precocafe*inflacaocafe)),True,(0,0,0))
    elif 1000 < precocafe*inflacaocafe < 1000000:
        text2 = font.render("Preco:$"+str('{0:,.2f}'.format(precocafe*inflacaocafe/1000))+"K",True,(0,0,0))
    elif 1000000 < precocafe*inflacaocafe < 1000000000:
        text2 = font.render("Preco:$"+str('{0:,.2f}'.format(precocafe*inflacaocafe/1000000))+"M",True,(0,0,0))
    elif 1000000000 < precocafe*inflacaocafe < 1000000000000:
        text2 = font.render("Preco:$"+str('{0:,.2f}'.format(precocafe*inflacaocafe/1000000000))+"Bi",True,(0,0,0))
    elif 1000000000000 < precocafe*inflacaocafe < 1000000000000000:
        text2 = font.render("Preco:$"+str('{0:,.2f}'.format(precocafe*inflacaocafe/1000000000000))+"T",True,(0,0,0))
    screen.blit(text,(850,90))
    screen.blit(text2,(800,115))

def contagem_acais(acais,precoacai,inflacaoacai):
    font = pygame.font.SysFont("Back to 1982",20)
    text = font.render("Acais:"+str(acais),True,(0,0,0))
    if precolivro*inflacaolivro < 1000:    
        text2 = font.render("Preco:$"+str('{0:,.1f}'.format(precolivro*inflacaolivro)),True,(0,0,0))
    elif 1000 < precolivro*inflacaolivro < 1000000:
        text2 = font.render("Preco:$"+str('{0:,.2f}'.format(precolivro*inflacaolivro/1000))+"K",True,(0,0,0))
    elif 1000000 < precolivro*inflacaolivro < 1000000000:
        text2 = font.render("Preco:$"+str('{0:,.2f}'.format(precolivro*inflacaolivro/1000000))+"M",True,(0,0,0))
    elif 1000000000 < precolivro*inflacaolivro < 1000000000000:
        text2 = font.render("Preco:$"+str('{0:,.2f}'.format(precolivro*inflacaolivro/1000000000))+"Bi",True,(0,0,0))
    elif 1000000000000 < precolivro*inflacaolivro < 1000000000000000:
        text2 = font.render("Preco:$"+str('{0:,.2f}'.format(precolivro*inflacaolivro/1000000000000))+"T",True,(0,0,0))
    screen.blit(text,(850,165))
    screen.blit(text2,(800,190))

def contagem_comps(comps,precocomp,inflacaocomp):
    font = pygame.font.SysFont("Back to 1982",13)
    text = font.render("Computadores:"+str(comps),True,(0,0,0))
    if precolivro*inflacaolivro < 1000:    
        text2 = font.render("Preco:$"+str('{0:,.1f}'.format(precolivro*inflacaolivro)),True,(0,0,0))
    elif 1000 < precolivro*inflacaolivro < 1000000:
        text2 = font.render("Preco:$"+str('{0:,.2f}'.format(precolivro*inflacaolivro/1000))+"K",True,(0,0,0))
    elif 1000000 < precolivro*inflacaolivro < 1000000000:
        text2 = font.render("Preco:$"+str('{0:,.2f}'.format(precolivro*inflacaolivro/1000000))+"M",True,(0,0,0))
    elif 1000000000 < precolivro*inflacaolivro < 1000000000000:
        text2 = font.render("Preco:$"+str('{0:,.2f}'.format(precolivro*inflacaolivro/1000000000))+"Bi",True,(0,0,0))
    elif 1000000000000 < precolivro*inflacaolivro < 1000000000000000:
        text2 = font.render("Preco:$"+str('{0:,.2f}'.format(precolivro*inflacaolivro/1000000000000))+"T",True,(0,0,0))
    screen.blit(text,(850,240))
    screen.blit(text2,(800,265))

def contagem_ninjas(ninjas):
    font = pygame.font.SysFont("Back to 1982",20)
    text = font.render("Ninjas:"+str(ninjas),True,(0,0,0))
    if precolivro*inflacaolivro < 1000:    
        text2 = font.render("Preco:$"+str('{0:,.1f}'.format(precolivro*inflacaolivro)),True,(0,0,0))
    elif 1000 < precolivro*inflacaolivro < 1000000:
        text2 = font.render("Preco:$"+str('{0:,.2f}'.format(precolivro*inflacaolivro/1000))+"K",True,(0,0,0))
    elif 1000000 < precolivro*inflacaolivro < 1000000000:
        text2 = font.render("Preco:$"+str('{0:,.2f}'.format(precolivro*inflacaolivro/1000000))+"M",True,(0,0,0))
    elif 1000000000 < precolivro*inflacaolivro < 1000000000000:
        text2 = font.render("Preco:$"+str('{0:,.2f}'.format(precolivro*inflacaolivro/1000000000))+"Bi",True,(0,0,0))
    elif 1000000000000 < precolivro*inflacaolivro < 1000000000000000:
        text2 = font.render("Preco:$"+str('{0:,.2f}'.format(precolivro*inflacaolivro/1000000000000))+"T",True,(0,0,0))
    screen.blit(text,(850,325))

def contagem_carros(carros):
    font = pygame.font.SysFont("Back to 1982",20)
    text = font.render("Carros:"+str(carros),True,(0,0,0))
    screen.blit(text,(850,400))

def contagem_profs(profs):
    font = pygame.font.SysFont("Back to 1982",14)
    text = font.render("Professores:"+str(profs),True,(0,0,0))
    screen.blit(text,(850,475))

def contagem_entidades(entidades):
    font = pygame.font.SysFont("Back to 1982",16)
    text = font.render("Entidades:"+str(entidades),True,(0,0,0))
    screen.blit(text,(850,550))

def contagem_FabLabs(FabLabs):
    font = pygame.font.SysFont("Back to 1982",20)
    text = font.render("FabLabs:"+str(FabLabs),True,(0,0,0))
    screen.blit(text,(850,625))

def contagem_Inspers(Inspers):
    font = pygame.font.SysFont("Back to 1982",20)
    text = font.render("Inspers:"+str(Inspers),True,(0,0,0))
    screen.blit(text,(850,700))

def Save(count,Multi,MultiT1,inflacaolivro,inflacaocafe,inflacaoacai,inflacaocomp,inflacaoninja,inflacaocarro,inflacaoprof,inflacaoent,inflacaoFab,inflacaoInsper,livros,cafes,acais,comps,ninjas,carros,profs,entidades,FabLabs,Inspers):
    listData = [count,Multi,MultiT1,inflacaolivro,inflacaocafe,inflacaoacai,inflacaocomp,inflacaoninja,inflacaocarro,inflacaoprof,inflacaoent,inflacaoFab,inflacaoInsper,livros,cafes,acais,comps,ninjas,carros,profs,entidades,FabLabs,Inspers]
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
    inflacaoacai = 1
    inflacaocomp = 1
    inflacaoninja = 1
    inflacaocarro = 1
    inflacaoprof = 1
    inflacaoent = 1
    inflacaoFab = 1
    inflacaoInsper = 1
    Multi = 1
    MultiT1 = 1
    livros = 0
    cafes = 0
    acais = 0
    comps = 0
    ninjas = 0
    carros = 0
    profs = 0
    entidades = 0
    FabLabs = 0
    Inspers = 0
    return count,Multi,MultiT1,inflacaolivro,inflacaocafe,inflacaoacai,inflacaocomp,inflacaoninja,inflacaocarro,inflacaoprof,inflacaoent,inflacaoFab,inflacaoInsper,livros,cafes,acais,comps,ninjas,carros,profs,entidades,FabLabs,Inspers  
    
    
    






#definir função Jogo            


#variáveis
DINHEIROTEMPO = USEREVENT + 1 
pygame.time.set_timer(DINHEIROTEMPO, 1000)

#Preços Lojas
precolivro = 20
precocafe = 50
precoacai = 100
precocomp = 250
preconinja = 1000
precocarro = 2500
precoprof = 5000
precoent = 10000
precofab = 25000
precoinsper = 100000

#Working Condition
Crashed = False
count = 0 
Multi = 1
MultiT1 = 1

#inflacao
inflacaolivro = 1.0
inflacaocafe = 1.0   
inflacaoacai = 1
inflacaocomp = 1
inflacaoninja = 1
inflacaocarro = 1
inflacaoprof = 1
inflacaoent = 1
inflacaoFab = 1
inflacaoInsper = 1

#Quantidade
livros = 0
cafes = 0
acais = 0
comps = 0
ninjas = 0
carros = 0
profs = 0
entidades = 0
FabLabs = 0
Inspers = 0
 
#animação
#screen.blit(oficina,[-130,430])   
    
while not Crashed:
    #screen.blit(Insper_background2, [0, 0])
    screen.blit(aluno,[-5,101])
    screen.blit(Insper_background, [0, 0])
      
    #livro
    if count >= precolivro * inflacaolivro:
        screen.blit(imagembotao1,[600,0])
        screen.blit(Fabulas,[620,15])
    elif count < precolivro * inflacaolivro:
        screen.blit(botaosemdinheiro,[600,0])
        screen.blit(calculosemdinheiro,[620,15])
    #cafe
    if count >= precocafe * inflacaocafe:
        screen.blit(imagembotao2,[600,75]) 
        screen.blit(Cafe,[620,80])  
    elif count < precocafe * inflacaocafe:
        screen.blit(botaosemdinheiro,[600,75])
        screen.blit(cafesemdinheiro,[620,80])
    #acai
    if count >= precoacai * inflacaoacai:
        screen.blit(imagembotao3,[600,150]) 
        screen.blit(imagemacai,[617,160])  
    elif count < precoacai * inflacaoacai:
        screen.blit(botaosemdinheiro,[600,150])
        screen.blit(acaisemdinheiro,[617,160])
    #computador
    if count >= precocomp * inflacaocomp:
        screen.blit(imagembotao4,[600,225]) 
        screen.blit(imagemcomputer,[618,235])  
    elif count < precocomp * inflacaocomp:
        screen.blit(botaosemdinheiro,[600,225])
        screen.blit(computersemdinheiro,[618,235])
    #Ninja
    if count >= preconinja * inflacaoninja:
        screen.blit(imagembotao5,[600,300])
        screen.blit(imagemninja,[628,308])
    elif count < preconinja * inflacaoninja:
        screen.blit(botaosemdinheiro,[600,300])
        screen.blit(ninjasemdinheiro,[628,308])
    #Carro
    if count >= precocarro * inflacaocarro:
        screen.blit(imagembotao6,[600,375])
        screen.blit(imagemcar,[615,400])
    elif count < precocarro * inflacaocarro:
        screen.blit(botaosemdinheiro,[600,375])
        screen.blit(carsemdinheiro,[615,400])
    #Prof
    if count >= precoprof * inflacaoprof:
        screen.blit(imagembotao7,[600,450])
        screen.blit(imagemprofessor,[635,455])
    elif count < precoprof * inflacaoprof:
        screen.blit(botaosemdinheiro,[600,450])
        screen.blit(professorsemdinheiro,[635,455])
    #entidade
    if count >= precoent * inflacaoent:
        screen.blit(imagembotao8,[600,525])
        screen.blit(imgaematletica,[622,532])
    elif count < precoent * inflacaoent:
        screen.blit(botaosemdinheiro,[600,525])
        screen.blit(atleticasemdinheiro,[622,532])   
    #FabLab
    if count >= precofab * inflacaoFab:
        screen.blit(imagembotao9,[600,600])
        screen.blit(imagemfablab,[625,610])
    elif count < precofab * inflacaoFab:
        screen.blit(botaosemdinheiro,[600,600])
        screen.blit(fablabsemdinheiro,[625,610])
    #Insper
    if count >= precoinsper * inflacaoInsper:
        screen.blit(imagembotao10,[600,675])
        screen.blit(imageminsper,[620,698])
    elif count < precoinsper * inflacaoInsper:
        screen.blit(botaosemdinheiro,[600,675])
        screen.blit(insperLogosemdinheiro,[620,698])
   
    
       
    Xmouse,Ymouse = Mouse()
    dinheiro(count)
    contagem_cafes(cafes,precocafe,inflacaocafe)
    contagem_livros(livros,precolivro,inflacaolivro)
    contagem_acais(acais,precoacai,inflacaoacai)
    contagem_comps(comps,precocomp,inflacaocomp)
    contagem_ninjas(ninjas)
    contagem_carros(carros)
    contagem_profs(profs)
    contagem_entidades(entidades)
    contagem_FabLabs(FabLabs)
    contagem_Inspers(Inspers)

    for event in pygame.event.get():
        print(event)
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                Crashed = True
                pygame.quit()
            
            elif event.key == K_h:
                pygame.display.toggle_fullscreen()

            elif event.key == K_s:
                Save(count,Multi,MultiT1,inflacaolivro,inflacaocafe,inflacaoacai,inflacaocomp,inflacaoninja,inflacaocarro,inflacaoprof,inflacaoent,inflacaoFab,inflacaoInsper,livros,cafes,acais,comps,ninjas,carros,profs,entidades,FabLabs,Inspers)  
                
            elif event.key == K_l:
                count,Multi,MultiT1,inflacaolivro,inflacaocafe,inflacaoacai,inflacaocomp,inflacaoninja,inflacaocarro,inflacaoprof,inflacaoent,inflacaoFab,inflacaoInsper,livros,cafes,acais,comps,ninjas,carros,profs,entidades,FabLabs,Inspers = Load()
                
            elif event.key == K_r:
                count,Multi,MultiT1,inflacaolivro,inflacaocafe,inflacaoacai,inflacaocomp,inflacaoninja,inflacaocarro,inflacaoprof,inflacaoent,inflacaoFab,inflacaoInsper,livros,cafes,acais,comps,ninjas,carros,profs,entidades,FabLabs,Inspers = Reset()
                
            elif event.key == K_q:
            	count = 10000000000
            
            elif event.key == K_a:
            	count = 0


        elif event.type == QUIT:
            pygame.quit()

        elif event.type == DINHEIROTEMPO:
            if cafes == 1 or acais == 1 or comps == 1 or ninjas == 1 or carros == 1 or profs == 1 or entidades == 1 or FabLabs == 1 or Inspers == 1:
                count += 1 
            elif cafes > 1 or acais > 1 or comps > 1 or ninjas > 1 or carros > 1 or profs > 1 or entidades > 1 or FabLabs > 1 or Inspers > 1:
                count += 1 + MultiT1    
        
        elif event.type == MOUSEBUTTONDOWN:
            if 30+195 > Xmouse > 30:
                if 197+380 > Ymouse > 197:
                    aluno =  alunoR
                    screen.blit(aluno,[-5,101])
            #livro
            if 600+500 > Xmouse > 600:
                if 0+75 > Ymouse > 0:
                    if count >= precolivro * inflacaolivro:
                        imagembotao1 = imagembotaoapertado1
                        screen.blit(imagembotao1,[600,0])
            #cafe
                if 150 > Ymouse > 75:
                    if count >= precocafe * inflacaocafe:
                        imagembotao2 = imagembotaoapertado2 
                        screen.blit(imagembotao2,[600,75])
            #acai
                if 225 > Ymouse > 150:
                    if count >= precoacai * inflacaoacai:
                        imagembotao3 = imagembotaoapertado3
                        screen.blit(imagembotao3,[600,150])
            #comutador
                if 300 > Ymouse > 225:
                    if count >= precocomp * inflacaocomp:
                        imagembotao4 = imagembotaoapertado4
                        screen.blit(imagembotao4,[600,225])
            #ninjas
                if 375 > Ymouse > 300:
                    if count >= preconinja * inflacaoninja:
                        imagembotao5 = imagembotaoapertado5
                        screen.blit(imagembotao5,[600,300])
            #carro
                if 450 > Ymouse > 375:
                    if count >= precocarro * inflacaocarro:
                        imagembotao6 = imagembotaoapertado6
                        screen.blit(imagembotao6,[600,375])
            #professor
                if 525 > Ymouse > 450:
                    if count >= precoprof * inflacaoprof:
                        imagembotao7 = imagembotaoapertado7
                        screen.blit(imagembotao7,[600,450])
            #entidades
                if 600 > Ymouse > 525:
                    if count >= precoent * inflacaoent:
                        imagembotao8 = imagembotaoapertado8
                        screen.blit(imagembotao8,[600,525])
            #fablab
                if 675 > Ymouse > 600:
                    if count >= precofab * inflacaoFab:
                        imagembotao9 = imagembotaoapertado9
                        screen.blit(imagembotao9,[600,600])
            #insper
                if 825 > Ymouse > 675:
                    if count >= precoinsper * inflacaoInsper:
                        imagembotao10 = imagembotaoapertado10
                        screen.blit(imagembotao10,[600,675])


        elif event.type == MOUSEBUTTONUP:
            Xmouse,Ymouse = event.pos
            if 30+195 > Xmouse > 30:
                if 197+380 > Ymouse > 197:
                    aluno = pygame.image.load('alunocapitalistas.png')
                    screen.blit(aluno,[-5,101])
            if 600+500 > Xmouse > 600:
                if 0+75 > Ymouse > 0:
                    if count >= precolivro * inflacaolivro:
                        imagembotao1 = pygame.image.load("botao.png")
                        screen.blit(imagembotao1,[600,0])
                        livros += 1
                        Multi += 2
                        count -= precolivro * inflacaolivro
                        inflacaolivro *= 1.5

                if 0+150 > Ymouse > 75:
                    if count >= precocafe * inflacaocafe:
                        imagembotao2 = pygame.image.load("botao.png")
                        screen.blit(imagembotao2,[600,75])
                        cafes += 1
                        MultiT1 += 2
                        count -= precocafe * inflacaocafe
                        inflacaocafe *= 1.7  

                if 0+225 > Ymouse > 150:
                    if count >= precoacai * inflacaoacai:
                        imagembotao3 = pygame.image.load("botao.png")
                        screen.blit(imagembotao3,[600,150])
                        acais += 1
                        MultiT1 += 5
                        count -= precoacai * inflacaoacai
                        inflacaoacai *= 2

                if 0+300 > Ymouse > 225:
                    if count >= precocomp * inflacaocomp:
                        imagembotao4 = pygame.image.load("botao.png")
                        screen.blit(imagembotao4,[600,225])
                        comps += 1
                        MultiT1 += 10
                        count -= precocomp * inflacaocomp
                        inflacaocomp *= 2.2
                
                if 0+375 > Ymouse > 300:
                    if count >= preconinja * inflacaoninja:
                        imagembotao5 = pygame.image.load("botao.png")
                        screen.blit(imagembotao5,[600,300])
                        ninjas += 1
                        MultiT1 += 15
                        count -= preconinja * inflacaoninja
                        inflacaoninja *= 2.5

                if 0+450 > Ymouse > 375:
                    if count >= precocarro * inflacaocarro:
                        imagembotao6 = pygame.image.load("botao.png")
                        screen.blit(imagembotao6,[600,375])
                        carros += 1
                        MultiT1 += 20
                        count -= precocarro * inflacaocarro
                        inflacaocarro *= 2.5

                if 0+525 > Ymouse > 450:
                    if count >= precoprof * inflacaoprof:
                        imagembotao7 = pygame.image.load("botao.png")
                        screen.blit(imagembotao7,[600,450])
                        profs += 1
                        MultiT1 += 50
                        count -= precoprof * inflacaoprof
                        inflacaoprof *= 2.5

                if 0+600 > Ymouse > 525:
                    if count >= precoent * inflacaoent:
                        imagembotao8 = pygame.image.load("botao.png")
                        screen.blit(imagembotao8,[600,525])
                        entidades += 1
                        MultiT1 += 100
                        count -= precoent * inflacaoent
                        inflacaoent *= 2.5
                
                if 0+675 > Ymouse > 600:
                    if count >= precofab * inflacaoFab:
                        imagembotao9 = pygame.image.load("botao.png")
                        screen.blit(imagembotao9,[600,600])
                        FabLabs += 1
                        MultiT1 += 250
                        count -= precofab * inflacaoFab
                        inflacaoFab *= 2.5
                
                if 0+825 > Ymouse > 675:
                    if count >= precoinsper * inflacaoInsper:
                        imagembotao10 = pygame.image.load("botao.png")
                        screen.blit(imagembotao10,[600,675])
                        Inspers += 1
                        MultiT1 *= 2
                        count -= precoinsper * inflacaoInsper
                        inflacaoInsper *= 5

            

            #Botao Aluno
            if 30+195 > Xmouse > 30:
                if 197+380 > Ymouse > 197:       
                    count += 0.1 * Multi
                    



              
                        





                            
            
    pygame.display.update()                
    clock.tick(60)