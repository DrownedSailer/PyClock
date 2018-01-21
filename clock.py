#a little digital clock program using pygame

import sys, pygame, datetime
pygame.init()

size = width, height = 400, 240
black = 0, 0, 0


screen = pygame.display.set_mode(size)

fontobj = pygame.font.Font(None, 50)




while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()

	screen.fill(black)

	timeobj = datetime.datetime
	ctime = timeobj.today()
	texsur = fontobj.render(str(ctime), True, (0,0,255), None)

	screen.blit(texsur, (1, height / 2))

	pygame.display.flip()

