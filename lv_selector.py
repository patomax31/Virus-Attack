import pygame
import sys
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, WHITE, TILE_SIZE
from button import Button
import lv_1
import main

def mainmenu():
    main.main_menu()
def level1():
    lv_1.level_1()

def level_selector():
    running = True
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    bg = pygame.image.load("assets/sprites/Fondo.jpeg")
    
    def get_font(size): # Funcion para obtener la fuente de texto
        return pygame.font.Font("font.ttf", size) # Devuelve la fuente de texto con el tamaño especificado
    
    pygame.init()
    
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        
        screen.fill("black")
        screen.blit(bg, (0, 0))

        PLAY_TEXT = get_font(45).render(" ", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
        screen.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(50), base_color="red", hovering_color="Green")
        Level = Button(image=None, pos=(250, 250), 
                            text_input="NIVEL", font=get_font(50), base_color="red", hovering_color="Green")
        Level_two = Button(image=None, pos=(600, 250), 
                            text_input="NIVEL", font=get_font(50), base_color="red", hovering_color="Green")
        Level_tres = Button(image=None, pos=(1000, 250), 
                            text_input="NIVEL", font=get_font(50), base_color="red", hovering_color="Green")    
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(screen)
        Level.changeColor(PLAY_MOUSE_POS)
        Level.update(screen)
        Level_two.changeColor(PLAY_MOUSE_POS)
        Level_two.update(screen)
        Level_tres.changeColor(PLAY_MOUSE_POS)
        Level_tres.update(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Level.checkForInput(PLAY_MOUSE_POS):
                    level1()    
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Level_two.checkForInput(PLAY_MOUSE_POS):
                    level1()         
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Level_tres.checkForInput(PLAY_MOUSE_POS):
                    level1()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    mainmenu()
            

        pygame.display.update()  