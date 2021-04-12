import pygame, sys, random

pygame.init()
screen = pygame.display.set_mode((1000, 650))
clock = pygame.time.Clock()
pygame.mouse.set_visible(False)

wood_bg = pygame.image.load('Wood_BG.png')
land_bg = pygame.image.load('Land_BG.png')
water_bg = pygame.image.load('Water_BG.png')
cloud1_bg = pygame.image.load('Cloud1.png')
cloud2_bg = pygame.image.load('Cloud2.png')
crosshair = pygame.image.load('crosshair.png')
ducks_surface = pygame.image.load('duck.png')

game_font = pygame.font.Font(None, 45)
text_surface = game_font.render('You Won!', True, (255, 255, 255))
text_rect = text_surface.get_rect(center = (500, 325))

land_position_y = 525
land_speed = 1

water_position_y = 575
water_speed = 1

ducks_list = []
for ducks in range(9):
	ducks_position_x = random.randrange(0, 950)
	ducks_position_y = random.randrange(150, 500)
	ducks_speed = 1.25
	ducks_rect = ducks_surface.get_rect(center = (ducks_position_x, ducks_position_y))
	ducks_list.append(ducks_rect)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

		if event.type == pygame.MOUSEMOTION:
			crosshair_rect = crosshair.get_rect(center = event.pos)

		if event.type == pygame.MOUSEBUTTONDOWN:
			for index, ducks_rect in enumerate(ducks_list):
				if ducks_rect.collidepoint(event.pos): #crosshair_rect.colliderect(ducks_rect):
					del ducks_list[index]

	screen.blit(wood_bg, (0, 0))

	for ducks_rect in ducks_list:
		ducks_rect[0] += ducks_speed
		if ducks_rect[0] >= 930:
			ducks_speed *= -1
		if ducks_rect[0] <= 0:
			ducks_speed *= -1

		screen.blit(ducks_surface, ducks_rect)

	if len(ducks_list) <= 0:
		screen.blit(text_surface, text_rect)

	land_position_y -= land_speed
	if land_position_y <= 515 or land_position_y >= 560:
		land_speed *= -1
	screen.blit(land_bg, (0, land_position_y))

	water_position_y += water_speed
	if water_position_y <= 560 or water_position_y >= 610:
		water_speed *= -1
	screen.blit(water_bg, (0, water_position_y))

	screen.blit(crosshair, crosshair_rect)

	screen.blit(cloud1_bg, (300, 50))
	screen.blit(cloud1_bg, (675, 0))
	screen.blit(cloud1_bg, (0, 25))

	screen.blit(cloud2_bg, (850, 50))
	screen.blit(cloud2_bg, (450, 25))
	screen.blit(cloud2_bg, (140, 0))

	pygame.display.update()
	clock.tick(120)