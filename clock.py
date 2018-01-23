#a little digital clock program using pygame

import sys, pygame, datetime


pygame.init()

size = width, height = 400, 240 #dimensions of screen surface
black, blue, white = (0, 0, 0), (0, 0 ,255), (255, 255, 255) # colors

screen = pygame.display.set_mode(size) # create surface
mainfont = pygame.font.Font(None, 160) # create font
smallfont = pygame.font.Font(None, 80)

pygame.display.set_caption("PyClock")

while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()

	screen.fill(black)

	# get date and convert to string
	ctime = str(datetime.datetime.today()) 

	# month
	ctimepart = ctime[5:7] 

	# takes string value for month and renders the month in words
	if ctimepart == "01": 
		tex = smallfont.render("JAN", True, white)
		screen.blit(tex, (10, 15))
	elif ctimepart == "02":
		tex = smallfont.render("FEB", True, white)
		screen.blit(tex, (10, 15))
	elif ctimepart == "03":
		tex = smallfont.render("MAR", True, white)
		screen.blit(tex, (10, 15))
	elif ctimepart == "04":
		tex = smallfont.render("APR", True, white)
		screen.blit(tex, (10, 15))
	elif ctimepart == "05":
		tex = smallfont.render("MAY", True, white)
		screen.blit(tex, (10, 15))
	elif ctimepart == "06":
		tex = smallfont.render("JUN", True, white)
		screen.blit(tex, (10, 15))
	elif ctimepart == "07":
		tex = smallfont.render("JUL", True, white)
		screen.blit(tex, (10, 15))
	elif ctimepart == "08":
		tex = smallfont.render("AUG", True, white)
		screen.blit(tex, (10, 15))
	elif ctimepart == "09":
		tex = smallfont.render("SEP", True, white)
		screen.blit(tex, (10, 15))
	elif ctimepart == "10":
		tex = smallfont.render("OCT", True, white)
		screen.blit(tex, (10, 15))
	elif ctimepart == "11":
		tex = smallfont.render("NOV", True, white)
		screen.blit(tex, (10, 15))
	elif ctimepart == "12":
		tex = smallfont.render("DEC", True, white)
		screen.blit(tex, (10, 15))

	# gets current day, creates a surface with text, blits it with original surface
	ctimepart = ctime[8:10] 
	tex = smallfont.render(ctimepart, True, white)
	screen.blit(tex, (150, 15))

	# ditto year
	ctimepart = ctime[:4]
	tex = smallfont.render(ctimepart, True, white)
	screen.blit(tex, (240, 15))

	# ditto hour + minutes
	ctimepart = ctime[11:16] 
	tex = mainfont.render(ctimepart, True, white)
	screen.blit(tex, (10, height / 2))

	# ditto seconds
	ctimepart = ctime[17:19] 
	tex = smallfont.render(ctimepart, True, white)
	screen.blit(tex, (305, height / 2 + 5))

	# used to apply all changes or something like that
	pygame.display.flip()

