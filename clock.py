#a little digital clock program using pygame

import sys, pygame, datetime


pygame.init()

size = width, height = 400, 240 #dimensions of screen surface
black, blue = (0, 0, 0), (0, 0 ,255) # colors
screen = pygame.display.set_mode(size) # create surface
fontobj = pygame.font.Font(None, 45) # create font


while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()

	screen.fill(black)
	
	ctime = str(datetime.datetime.today())
	ctime = ctime[10:19]
	texsur = fontobj.render(ctime, True, blue, None)

	screen.blit(texsur, (1, height / 2))

	pygame.display.flip()

