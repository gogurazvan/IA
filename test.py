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

piesaAlba = pygame.image.load('piesa-alba.png')
diametruPiesa=2*Tabla.razaPiesa
piesaAlba = pygame.transform.scale(piesaAlba, (diametruPiesa,diametruPiesa))
piesaNeagra = pygame.image.load('piesa-neagra.png')
piesaNeagra = pygame.transform.scale(piesaNeagra, (diametruPiesa,diametruPiesa))
piesaSelectata = pygame.image.load('piesa-rosie.png')
piesaSelectata = pygame.transform.scale(piesaSelectata, (diametruPiesa,diametruPiesa))
nodPiesaSelectata=False
cN=[[Tabla.translatie + Tabla.scalare * x for x in nod] for nod in Tabla.noduri]
pieseAlbe=[cN[10]]
nodPiesaSelectata=None
pieseNegre=[cN[0],cN[1],cN[3]]

class Stare:
	def __init__(self, noduriNegre, nodAlb, randMutare, parinte, randParinte):
		self.noduriNegre=noduriNegre
		self.noduriAlbe=noduriAlbe
		self.randMutare=randMutare
		self.parinte=parinte
		self.randParinte=randParinte

	def verificaJoc(self):
		jocContinua=False
		
		for nNg in noduriNegre:
			if Tabla.noduri[nNg][0] < Tabla.noduri[nodAlb][0]:
				jocContinua=True
		if jocContinua == False: 
			return 'a'
		if rand == 0:  #rand alb
			for muchie in (muc for muc in Tabla.muchii if muc[0]==nodAlb or muc[1]==nodAlb):  #generator muchii jucator alb
				if muchie[0] not in noduriNegre or muchie[1] not in noduriNegre:
					JocContinua=True
			if jocContinua == False: 
				return 'n'
		return True

	def estimeaza_scor(self,depth):
		sfarsitJ=self.verificaJoc()
		if self.randParinte==0:
			if sfarsitJ=='a':
				return 99+adancime
			elif sfarsitJ=='n':
				return -99+adancime
			else:
				return self.calculeaza_h()
		else:
			if sfarsitJ=='a':
				return 99+adancime
			elif sfarsitJ=='n':
				return -99+adancime
			else:
				return self.calculeaza_h()


	def calculeaza_h():
		return 1

	

def deseneazaEcranJoc():
	ecran.fill(culoareEcran)
	for nod in cN:
		pygame.draw.circle(surface=ecran, color=culoareLinii, center=nod, radius=Tabla.razaPct,width=0) #width=0 face un cerc plin
		
	for muchie in Tabla.muchii:
		p0=cN[muchie[0]]
		p1=cN[muchie[1]]
		pygame.draw.line(surface=ecran,color=culoareLinii,start_pos=p0,end_pos=p1,width=5)
	for nod in pieseAlbe:
		ecran.blit(piesaAlba,(nod[0]-Tabla.razaPiesa,nod[1]-Tabla.razaPiesa))
	for nod in pieseNegre:
		ecran.blit(piesaNeagra,(nod[0]-Tabla.razaPiesa,nod[1]-Tabla.razaPiesa))
	if nodPiesaSelectata:
		ecran.blit(piesaSelectata,(nodPiesaSelectata[0]-Tabla.razaPiesa,nodPiesaSelectata[1]-Tabla.razaPiesa))
	pygame.display.update()


deseneazaEcranJoc()
rand=0

print("Muta "+ ("negru" if rand else "alb"))
while True:
		
	for ev in pygame.event.get(): 
		if ev.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if ev.type == pygame.MOUSEBUTTONDOWN: 
			pos = pygame.mouse.get_pos()
			for nod in cN:
				if distEuclid(pos,nod)<=Tabla.razaPct:
					if rand==1:
						piesa=piesaNeagra
						pieseCurente=pieseNegre
					else:
						piesa=piesaAlba
						pieseCurente=pieseAlbe
					
					if nod not in pieseAlbe+pieseNegre:
						
						if nodPiesaSelectata :
							n0=cN.index(nod)
							n1=cN.index(nodPiesaSelectata)
							if ((n0,n1) in Tabla.muchii or (n1,n0) in Tabla.muchii):
								pieseCurente.remove(nodPiesaSelectata)
								pieseCurente.append(nod)
								rand=1-rand
								print("Muta "+ ("negru" if rand else "alb"))
								nodPiesaSelectata=False
					else:
						if nod in pieseCurente:	
							if nodPiesaSelectata==nod:					
								nodPiesaSelectata=False  
							else:
								nodPiesaSelectata= nod
							

					
					
					
					deseneazaEcranJoc()
					break


				
