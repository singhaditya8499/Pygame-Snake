import pygame
import time
import random
# import imutils
pygame.init()
display_width=800
display_height=600
last_eat=time.time()

game_display=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Saanp bole hiss")

clock=pygame.time.Clock()

def text_objects(text,fonts):
    text_surface=fonts.render(text,True,(250,250,210))
    return text_surface,text_surface.get_rect()

def start_menu():
	start=True
	x=1
	while start:
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				pygame.quit()
		game_display.fill((0,0,0))
		pygame.draw.rect(game_display,(255,255,255),(x*10,100,10,10))
		pygame.draw.rect(game_display,(255,255,255),((x-1)*10,100,10,10))
		pygame.draw.rect(game_display,(255,255,255),((x-2)*10,100,10,10))
		pygame.draw.rect(game_display,(255,255,255),((x-3)*10,100,10,10))
		pygame.draw.rect(game_display,(255,0,0),((x+2)*10,100,10,10))
		x+=1
		if x==81:
			x=1
		heading=pygame.font.Font('freesansbold.ttf',40)
		textsurf,textrec=text_objects("Tu Saanp badi hai mast mast",heading)
		textrec.center=((400,50))
		game_display.blit(textsurf,textrec)         
		menu_text=pygame.font.Font('freesansbold.ttf',20)
		pygame.draw.rect(game_display,(255,0,0),(150,450,100,50))
		textsurf,textrec=text_objects("Gosszz!!",menu_text)
		textrec.center=((150+100/2,450+50/2))
		game_display.blit(textsurf,textrec)
		pygame.draw.rect(game_display,(255,0,0),(550,450,100,50))
		textsurf,textrec=text_objects("Quit",menu_text)
		textrec.center=((550+100/2,450+50/2))
		game_display.blit(textsurf,textrec)
		mouse=pygame.mouse.get_pos()
		click=pygame.mouse.get_pressed()
		if 150+100>mouse[0]>150 and 450+50>mouse[1]>450 and click[0]==1:
			#start the game here. first create a 
			print("start")
			game()
		if 550+100>mouse[0]>550 and 450+50>mouse[1]>450 and click[0]==1:
			pygame.quit()
		pygame.display.update()
		clock.tick(25)

def overlap(fw,fh,rw,rh):
	if fw==rw and rh==fh:
		return True

	return False

def game():
	collide=0
	position=[]
	score=0
	position.append((40,30))
	rw=random.randint(0,79)
	rh=random.randint(0,59)
	direction=1
	gravity=0
	eat=False
	while not collide:
		# print(len(position))
		fw,fh=position[0]
		if fw==-1 or fw==80 or fh==-1 or fh==60:
			print("Dead")
			collide=True
			continue
		if eat:
			eat=False
			last_eat=time.time()
			print(last_eat)
			rw=random.randint(4,79)
			rh=random.randint(4,59)
		cur_time=time.time()
		global last_eat
		if cur_time-last_eat>20:
			collide=1
			while collide:
				for event in pygame.event.get():
					if event.type==pygame.QUIT:
						pygame.quit()
					if event.type==pygame.KEYDOWN:
						pygame.quit()
				# game_display.fill((0,0,0))
				heading=pygame.font.Font('freesansbold.ttf',40)
				textsurf,textrec=text_objects("Dead!!! Press any key to exit.",heading)
				textrec.center=((400,50))
				game_display.blit(textsurf,textrec)
				heading=pygame.font.Font('freesansbold.ttf',40)
				textsurf,textrec=text_objects("Your Score is: "+str(score),heading)
				textrec.center=((400,300))
				game_display.blit(textsurf,textrec)
				pygame.display.update()
			pygame.quit()
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				pygame.quit()
			if event.type==pygame.KEYDOWN:
				if event.key==pygame.K_LEFT:
					gravity=0
					direction=-1
				if event.key==pygame.K_RIGHT:
					gravity=0
					direction=1
				if event.key==pygame.K_UP:
					gravity=-1
					direction=0
				if event.key==pygame.K_DOWN:
					gravity=1
					direction=0
			if event.type==pygame.KEYUP:
				delete=1
		eat=overlap(fw,fh,rw,rh)
		if eat:
			score+=1
			lw,lh=position[len(position)-1]
		for i in range(len(position)-1,0,-1):
			position[i]=position[i-1]
		position[0]=(fw+direction,fh+gravity)
		if eat:
			position.append((lw,lh))
		game_display.fill((0,0,0))
		for sw,sh in position:
			pygame.draw.rect(game_display,(255,255,255),(sw*10,sh*10,10,10))
		pygame.draw.rect(game_display,(255,0,0),(rw*10,rh*10,10,10))
		# print(fw,fh)
		heading=pygame.font.Font('freesansbold.ttf',20)
		textsurf,textrec=text_objects(str(score),heading)
		textrec.center=((20,20))
		game_display.blit(textsurf,textrec)
		pygame.display.update()
		clock.tick(10+5*(len(position)-1))

	while collide:
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				pygame.quit()
			if event.type==pygame.KEYDOWN:
				pygame.quit()
		# game_display.fill((0,0,0))
		heading=pygame.font.Font('freesansbold.ttf',40)
		textsurf,textrec=text_objects("Dead!!! Press any key to exit.",heading)
		textrec.center=((400,50))
		game_display.blit(textsurf,textrec)
		heading=pygame.font.Font('freesansbold.ttf',40)
		textsurf,textrec=text_objects("Your Score is: "+str(score),heading)
		textrec.center=((400,300))
		game_display.blit(textsurf,textrec)
		pygame.display.update()

start_menu()
game()
