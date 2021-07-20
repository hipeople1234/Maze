import pygame
#pygame.draw.circle(Screen,Color, [X location, Y location], Radius)
done = False
pygame.init()
SCREEN_WIDTH = 1050
SCREEN_HEIGHT = 600
location1 = 50
location2 = 50
size = [SCREEN_WIDTH, SCREEN_HEIGHT]
WHITE=(255,255,255)
BLUE=(0,0,255)
RED = (255,0,0)
lightred = (255,200,200)
darkwhite = (244,244,244)
GREEN = (0,255,0)
bb_color = BLUE
box_color = RED
button_color2 = RED
button_color = WHITE
button_colorlight= darkwhite
move_x = 0
move_y = 0

#Box Rects
box_rect=pygame.Rect(0, 0, 100,600)
box_rect2=pygame.Rect(100, 150, 950,50)
box_rect3=pygame.Rect(100, 300, 950,50)
box_rect4=pygame.Rect(100, 450, 950,50)
end_rect = pygame.Rect(950, 150,100,50)
buttonrect = pygame.Rect(200,200,300,200)
buttonrect2 = pygame.Rect(500,200,300,200)
#Text/button rects

#Button exit text
font = pygame.font.Font(None, 32)
text = font.render('CLOSE', True, pygame.Color(0,255,0,0))
textRect = text.get_rect()
textRect.center = (buttonrect.centerx, buttonrect.centery)
clock = pygame.time.Clock()

#Button Continue
font2 = pygame.font.Font(None, 32)
text2 = font.render('CONTINUE', True, pygame.Color(0,255,0,0))
textRect2 = text2.get_rect()
textRect2.center = (buttonrect2.centerx, buttonrect2.centery)
clock = pygame.time.Clock()

while not done:
    location = [location1+move_x,location2+move_y]
    locationx = location1 + move_x
    locationy = location2 + move_y
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and circle_blue.left>0:
        move_x += -4
    if key[pygame.K_RIGHT]and circle_blue.right < SCREEN_WIDTH:
        move_x += 4
    if key[pygame.K_UP] and circle_blue.top > 0:
        move_y += -4
    if key[pygame.K_DOWN] and circle_blue.bottom < SCREEN_HEIGHT:
        move_y += 4
    #Shape draw
    screen = pygame.display.set_mode(size)
    box = pygame.draw.rect(screen,box_color,box_rect)
    line1 = pygame.draw.rect(screen,box_color,box_rect2)
    falseline1 = pygame.draw.rect(screen,box_color,box_rect3)
    falseline2 = pygame.draw.rect(screen,box_color,box_rect4)
    end_box = pygame.draw.rect(screen,box_color,end_rect)
    circle_blue = pygame.draw.circle(screen,bb_color,location,20)

    #pygame.draw.rect(surface, color, rect)
    # pygame.Rect(left, top, width, height)

    #Box exit
    if (locationx <= box.right and locationy <= box.bottom and locationx >= box.left and locationy >= box.top) or (locationx <= line1.right and locationy <= line1.bottom and locationx >= line1.left and locationy >= line1.top):
        bb_color = WHITE
    else:
        bb_color = BLUE
    mouse = pygame.mouse.get_pos()

    if bb_color == BLUE:
        move_x = 0
        move_y = 0
    if locationx <= end_box.right and locationy <= end_box.bottom and locationx >= end_box.left and locationy >= end_box.top:
        button1 = pygame.draw.rect(screen,button_color,buttonrect)
        button2 = pygame.draw.rect(screen,button_color2,buttonrect2)
        screen.blit(text, textRect)
        screen.blit(text2, textRect2)
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                done = True
            if ev.type == pygame.MOUSEBUTTONDOWN:
                x = mouse[0]
                y = mouse[1]
                print(x,y)
                print("right",buttonrect.right)
                print("left",buttonrect.left)
                print("top",buttonrect.top)
                print("bottom",buttonrect.bottom)
                if x<= buttonrect.right and y <= buttonrect.bottom and x >= buttonrect.left and y >= buttonrect.top:
                    pygame.quit()
                    done = True
                elif x<= buttonrect2.right and y <= buttonrect2.bottom and x >= buttonrect2.left and y >= buttonrect2.top:
                    move_x = 0
                    move_y = 0
    if not done:
        pygame.display.flip()
        clock.tick(60)
