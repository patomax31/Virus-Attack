import pygame, sys


pygame.init()

screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("MENU")

#fuentes
font = pygame.font.SysFont("arialblack", 40)
TEXT_COL = (255, 255, 255)

#define variables
game_paused = False
#imagne boton---------------------------------------------------
start_img = pygame.image.load("boton.png").convert_alpha()
#class boton
class button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        
    def draw(self):
        
        #mouse
        pos = pygame.mouse.get_pos()
        #check mouse
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                print("clicked")
         
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False    
            
        #draw boton on screen
        screen.blit(self.image, (self.rect.x, self.rect.y))
        
#crear boton

start_button= button(100, 200, start_img, 0.5)
           
#textooo
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))
#Lista?

run = True
while run:

    screen.fill((0, 0, 100,))
#boton
    start_button.draw()
    
#juego pausa

    if game_paused == True:
      pass
    #Display menu
    else:
       draw_text(":B", font, TEXT_COL, 160, 250)    
    
    #event handler/For loop
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_paused = True
              
        
        
        if event.type ==pygame.QUIT:
            run=False

    pygame.display.update()

pygame.quit