'''
Youtube vid that helped
https://www.youtube.com/watch?v=jyrP0dDGqgY
'''
#changed Color_list[0] to Color_list[0] and blue to COlor_list[1]
#Changed location1 and location2 to 50!!!!!!!!
#removed button text
#added Class
import pygame
from pygame.locals import *
#pygame.draw.circle(Screen,Color, [X location, Y location], Radius)
pygame.display.set_caption('Maze game')
clock = pygame.time.Clock()
done = False
pygame.init()
SCREEN_WIDTH = 1050
SCREEN_HEIGHT = 600
size = [SCREEN_WIDTH, SCREEN_HEIGHT]
#Replaced with list
Color_list = [(255,255,255),(0,0,255),(139,0,0),(128,128,128),(0,0,0),(0,0,139)]
#              white         Blue?      Red       gray         Color_list[4]   Dark blue
bb_color = Color_list[1]
box_color = Color_list[2]
move_x = 0
move_y = 0
#Added a click var and font
font = pygame.font.SysFont('Constantia', 30)
clicked = False

#Box Rects
box_rect=pygame.Rect(0, 0, 100,600)
box_rect2=pygame.Rect(100, 150, 950,50)
box_rect3=pygame.Rect(100, 300, 950,50)
box_rect4=pygame.Rect(100, 450, 950,50)
end_rect = pygame.Rect(950, 150,100,50)
buttonrect = pygame.Rect(200,200,300,200)
buttonrect2 = pygame.Rect(500,200,300,200)



class button():

	#colours for button and text
	button_col = (255, 0, 0)
	hover_col = (75, 225, 255)
	click_col = (50, 150, 255)
	text_col = (0,0,0)
	width = 180
	height = 70

	def __init__(self, x, y, text):
		self.x = x
		self.y = y
		self.text = text

	def draw_button(self):

		global clicked
		action = False

		#get mouse position
		pos = pygame.mouse.get_pos()

		#create pygame Rect object for the button
		button_rect = Rect(self.x, self.y, self.width, self.height)

		#check mouseover and clicked conditions
		if button_rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1:
				clicked = True
				pygame.draw.rect(screen, self.click_col, button_rect)
			elif pygame.mouse.get_pressed()[0] == 0 and clicked == True:
				clicked = False
				action = True
			else:
				pygame.draw.rect(screen, self.hover_col, button_rect)
		else:
			pygame.draw.rect(screen, self.button_col, button_rect)

		#add text to button
		text_img = font.render(self.text, True, self.text_col)
		text_len = text_img.get_width()
		screen.blit(text_img, (self.x + int(self.width / 2) - int(text_len / 2), self.y + 25))
		return action


again = button(300, 300, 'Play Again?')
quit = button(650, 300, 'Quit?')


while not done:

    location = [50+move_x,50+move_y]
    locationx = 50 + move_x
    locationy = 50 + move_y
    #Close program
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    #Movement
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and circle_blue.left>0:
        move_x += -2
    if key[pygame.K_RIGHT]and circle_blue.right < SCREEN_WIDTH:
        move_x += 2
    if key[pygame.K_UP] and circle_blue.top > 0:
        move_y += -2
    if key[pygame.K_DOWN] and circle_blue.bottom < SCREEN_HEIGHT:
        move_y += 2
    #Shape draw
    screen = pygame.display.set_mode(size)
    screen.fill(Color_list[3])
    box = pygame.draw.rect(screen,box_color,box_rect)
    line1 = pygame.draw.rect(screen,box_color,box_rect2)
    falseline1 = pygame.draw.rect(screen,box_color,box_rect3)
    falseline2 = pygame.draw.rect(screen,box_color,box_rect4)
    end_box = pygame.draw.rect(screen,box_color,end_rect)
    circle_blue = pygame.draw.circle(screen,bb_color,location,20)
    #pygame.draw.rect(surface, color, rect)
    # pygame.Rect(left, top, width, height)

#Not sure what this it
    if (locationx <= box.right and locationy <= box.bottom and locationx >= box.left and locationy >= box.top) or (locationx <= line1.right and locationy <= line1.bottom and locationx >= line1.left and locationy >= line1.top):
        bb_color = Color_list[0]
    else:
        bb_color = Color_list[1]

    if bb_color == Color_list[1]:
        move_x = 0
        move_y = 0
#End box
    if locationx <= end_box.right and locationy <= end_box.bottom and locationx >= end_box.left and locationy >= end_box.top:
        if again.draw_button():
            move_x = 0
            move_y = 0
        if quit.draw_button():
            pygame.quit()
            done = True



#FPS/Speed of ball
    if not done:
        pygame.display.update()
        clock.tick(240)
