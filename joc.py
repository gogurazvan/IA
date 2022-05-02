import pygame
import sys
import math

def distEuclid(p0,p1):
	(x0,y0)=p0
	(x1,y1)=p1
	return math.sqrt((x0-x1)**2+(y0-y1)**2)

class Tabla:
	#coordonatele nodurilor ()
	noduri=[
		(1,1),
		(2,0),
		(2,1),
		(2,2),
		(3,0),
		(3,1),
		(3,2),
		(4,0),
		(4,1),
		(4,2),
		(5,1)
	]
	muchii=[(0,1),(0,2),(0,3),(1,2),(1,4),(1,5),(2,3),(2,5),(3,5),(3,6),(4,5),(4,7),(5,6),(5,7),(5,8),(5,9),(6,9),(7,8),(7,10),(8,9),(8,10),(9,10)]
	scalare=100
	translatie=20
	razaPct=10
	razaPiesa=20
		


class ReguliJoc:
	player=None



pygame.init()
culoareEcran=(255,255,255)
culoareLinii=(0,0,0)
ecran=pygame.display.set_mode(size=(700,400))

verde=(0,200,0)
rosu=(200,0,0)




piesaAlba = pygame.image.load('piesa-alba.png')
diametruPiesa=2*Tabla.razaPiesa
piesaAlba = pygame.transform.scale(piesaAlba, (diametruPiesa,diametruPiesa))

piesaNeagra = pygame.image.load('piesa-neagra.png')
piesaNeagra = pygame.transform.scale(piesaNeagra, (diametruPiesa,diametruPiesa))

piesaSelectata = pygame.image.load('piesa-rosie.png')
piesaSelectata = pygame.transform.scale(piesaSelectata, (diametruPiesa,diametruPiesa))
cN=[[Tabla.translatie + Tabla.scalare * x for x in nod] for nod in Tabla.noduri]

nodPiesaSelectata=None
botCaini=False
botIepure=False

class Button:
	def __init__(self, text, x, y):
		self.text=text
		self.x=x
		self.y=y
		self.width=150
		self.heigth=100

	def deseneazaButon(self):
		mouse = pygame.mouse.get_pos()
		click = pygame.mouse.get_pressed()
		if x+width > mouse[0] > x and y+heigth > mouse[1] > y:
			pygame.draw.rect(gameDisplay, rosu,(x,y,width,heigth))

			if click[0] == 1 and functie != None:
				return True         
		else:
			pygame.draw.rect(gameDisplay, verde,(x,y,width,heigth))
		return False

    smallText = pygame.font.SysFont("Corbel",20)
    textSurface = smallText.render(text, True, black)
    textRect.center = ( (x+(width/2)), (y+(heigth/2)) )
    gameDisplay.blit(textSurface, textSurface.get_rect())


play = Button('play' , 300 , 150)
pVp = Button('2 players' , 300 , 100)
pVe = Button('player vs com' , 300 , 200)
eVe = Button('com vs com' , 300 , 300)
selLup = Button('Lupi' , 300 , 100)
selIep = Button('Iepure' , 300 , 100)
minMax = Button('Minimax' , 300 , 200)
alphaBeta = Button('Alpha-Beta' , 300 , 200)
dif1 = Button('Dificultate: Usor' , 300 , 300)
dif2 = Button('Dificulate: Mediu' , 300 , 300)
dif3 = Button('Dificultate: Greu' , 300 , 300)
botOp = Button('Optiuni' , 300 , 250)
meniu = Button('Inapoi la meniu' , 300 , 400)

class Stare:
	def __init__(self, noduriNegre, nodAlb, randMutare):
		self.noduriNegre=noduriNegre
		self.nodAlb=nodAlb
		self.randMutare=randMutare

	def verificaJoc(self):
		jocContinua=False
		
		for nNg in noduriNegre:
			if Tabla.noduri[nNg][0] < Tabla.noduri[nodAlb][0]:
				jocContinua=True
		if jocContinua == False: 
			return 'a'
		if randMutare == 0:  #rand alb
			for muchie in (muc for muc in Tabla.muchii if muc[0]==nodAlb or muc[1]==nodAlb):  #generator muchii jucator alb
				if muchie[0] not in noduriNegre or muchie[1] not in noduriNegre:
					JocContinua=True
			if jocContinua == False: 
				return 'n'
		return True

	def estimeaza_scor(self,depth):
		sfarsitJ=self.verificaJoc()
		if (self.randMutare+depth)%2==0:
			if sfarsitJ=='a':
				return 99+depth
			elif sfarsitJ=='n':
				return -99+depth
			else:
				return self.calculeaza_h('a')
		else:
			if sfarsitJ=='a':
				return 99+depth
			elif sfarsitJ=='n':
				return -99+depth
			else:
				return self.calculeaza_h('n')


	def calculeaza_h(self,culoare):
		if culoare == 'a':
			return 1
		else:
			return 1

	def deseneazaEcranJoc(self):
		ecran.fill(culoareEcran)
		for nod in cN:
			pygame.draw.circle(surface=ecran, color=culoareLinii, center=nod, radius=Tabla.razaPct,width=0) #width=0 face un cerc plin
			
		for muchie in Tabla.muchii:
			p0=cN[muchie[0]]
			p1=cN[muchie[1]]
			pygame.draw.line(surface=ecran,color=culoareLinii,start_pos=p0,end_pos=p1,width=5)

		ecran.blit(piesaAlba,(cN[self.nodAlb][0]-Tabla.razaPiesa,cN[self.nodAlb][1]-Tabla.razaPiesa))

		for nod in self.noduriNegre:
			nodPix=cN[nod]
			ecran.blit(piesaNeagra,(nodPix[0]-Tabla.razaPiesa,nodPix[1]-Tabla.razaPiesa))
		if nodPiesaSelectata:
			ecran.blit(piesaSelectata,(cN[nodPiesaSelectata][0]-Tabla.razaPiesa,cN[nodPiesaSelectata][1]-Tabla.razaPiesa))
		pygame.display.update()




def genereazaSuccesori(st):
	vecini=[]
	if st.randMutare== 0:
		for nod in range(Tabla.noduri):
			if ((nod,st.nodAlb) in Tabla.muchii or (st.nodAlb,nod) in Tabla.muchii):
				vecini.append(Stare(st.noduriNegre,nod,1-st.randMutare))
	else:
		for nodNegru in st.noduriNegre:
			for nod in range(Tabla.noduri):
				if ((nod,nodNegru) in Tabla.muchii or (nodNegru,nod) in Tabla.muchii) and Tabla.noduri[nod][0]>=Tabla.noduri[nodNegru][0]:
					newNegruSet=[nod if x==nodNegru else x for x in st.noduriNegre ]
					vecini.append(Stare(newNegruSet,st.nodAlb,1-st.randMutare))
	return vecini





start= Stare([1,2,3],10,1)
start.deseneazaEcranJoc()
rand=0

print("Muta "+ ("negru" if rand else "alb"))
while True:
		
	for ev in pygame.event.get(): 
		if ev.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
# 		if ev.type == pygame.MOUSEBUTTONDOWN: 
# 			pos = pygame.mouse.get_pos()
# 			for nod in cN:
# 				if distEuclid(pos,nod)<=Tabla.razaPct:
# 					if rand==1:
# 						piesa=piesaNeagra
# 						pieseCurente=pieseNegre
# 					else:
# 						piesa=piesaAlba
# 						pieseCurente=pieseAlbe
					
# 					if cN.index(nod) not in pieseAlbe+pieseNegre:
						
# 						if nodPiesaSelectata :
# 							n0=cN.index(nod)
# 							n1=cN.index(nodPiesaSelectata)
# 							if ((n0,n1) in Tabla.muchii or (n1,n0) in Tabla.muchii):
# 								pieseCurente.remove(nodPiesaSelectata)
# 								pieseCurente.append(nod)
# 								rand=1-rand
# 								print("Muta "+ ("negru" if rand else "alb"))
# 								nodPiesaSelectata=False
# 					else:
# 						if cN.index(nod) in pieseCurente:	
# 							if nodPiesaSelectata==nod:					
# 								nodPiesaSelectata=False  
# 							else:
# 								nodPiesaSelectata= nod
							

					
					
					
# 					deseneazaEcranJoc()
# 					break


				
