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
		
playLup=0
playIep=1

mmax=0
alfaB=1
class ReguliJoc:
	player=playLup
	modJoc="pvp"
	dificultate=0
	algoritm=mmax


men=0
optiuni=1
selectP=2

app_state=men

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
		self.heigth=50

	def deseneazaButon(self):
		clicked=False
		mouse = pygame.mouse.get_pos()
		click = pygame.mouse.get_pressed()
		if self.x+self.width > mouse[0] > self.x and self.y+self.heigth > mouse[1] > self.y:
			pygame.draw.rect(ecran, rosu,(self.x,self.y,self.width,self.heigth))

			if click[0] == 1:
				clicked = True		     
		else:
			pygame.draw.rect(ecran, verde,(self.x,self.y,self.width,self.heigth))

		smallText = pygame.font.SysFont("Corbel",20)
		textSurface = smallText.render(self.text, True, (0,0,0))
		textRectangle=textSurface.get_rect()
		textRectangle.center = ( (self.x+(self.width/2)), (self.y+(self.heigth/2)) )
		ecran.blit(textSurface, textRectangle)
		return clicked


play = Button('play' , 280 , 150)
pVp = Button('2 players' , 280 , 100)
pVe = Button('player vs com' , 280 , 100)
eVe = Button('com vs com' , 280 , 100)
selLup = Button('Lupi' , 280 , 200)
selIep = Button('Iepure' , 280 , 200)
minMax = Button('Minimax' , 280 , 200)
alphaBeta = Button('Alpha-Beta' , 280 , 200)
dif1 = Button('Dificultate: Usor' , 280 , 100)
dif2 = Button('Dificulate: Mediu' , 280 , 100)
dif3 = Button('Dificultate: Greu' , 280 , 100)
botOp = Button('Optiuni' , 280 , 250)
meniu = Button('Inapoi la meniu' , 280 , 300)

while True:
		
	for ev in pygame.event.get(): 
		if ev.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

		if app_state == men:
			ecran.fill(culoareEcran)
			
			if play.deseneazaButon():
				app_state=selectP
			if botOp.deseneazaButon():
				app_state=optiuni



		elif app_state == optiuni:
			ecran.fill(culoareEcran)

			if ReguliJoc.algoritm == mmax:
				if minMax.deseneazaButon():
					ReguliJoc.algoritm = alfaB
			else:
				if alphaBeta.deseneazaButon():
					ReguliJoc.algoritm = mmax

			if ReguliJoc.dificultate == 0:
				if dif1.deseneazaButon():
					ReguliJoc.dificultate = 1
			elif ReguliJoc.dificultate == 1:
				if dif2.deseneazaButon():
					ReguliJoc.dificultate = 2
			else:
				if dif3.deseneazaButon():
					ReguliJoc.dificultate = 0

			if meniu.deseneazaButon():
				app_state=men




		elif app_state == selectP:

			ecran.fill(culoareEcran)

			if ReguliJoc.player == playLup:
				if selLup.deseneazaButon():
					ReguliJoc.player = playIep
			else:
				if selIep.deseneazaButon():
					ReguliJoc.player = playLup

			if ReguliJoc.modJoc == "pvp":
				if pVp.deseneazaButon():
					ReguliJoc.modJoc = "pve"
			elif ReguliJoc.modJoc == "pve":
				if pVe.deseneazaButon():
					ReguliJoc.modJoc = "eve"
			else:
				if eVe.deseneazaButon():
					ReguliJoc.modJoc = "pvp"

			if meniu.deseneazaButon():
				app_state=men

		else:
			pygame.quit()
			sys.exit()

		pygame.display.update()


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
