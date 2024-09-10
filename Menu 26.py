import pygame, sys
from button import Button
import random
pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Videojuego")
player = pygame.Rect((300, 250, 50, 50))
pixel = 64
def get_font(size):
    return pygame.font.Font("font.ttf", size)

def play():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        
        SCREEN.fill("black")
    
           
        PLAY_TEXT = get_font(45).render(" ", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")
        Level = Button(image=None, pos=(250, 250), 
                            text_input="NIVEL", font=get_font(75), base_color="White", hovering_color="Green")
        Level_two = Button(image=None, pos=(600, 250), 
                            text_input="NIVEL", font=get_font(75), base_color="White", hovering_color="Green")
        Level_tres = Button(image=None, pos=(1000, 250), 
                            text_input="NIVEL", font=get_font(75), base_color="White", hovering_color="Green")    
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        Level.changeColor(PLAY_MOUSE_POS)
        Level.update(SCREEN)
        Level_two.changeColor(PLAY_MOUSE_POS)
        Level_two.update(SCREEN)
        Level_tres.changeColor(PLAY_MOUSE_POS)
        Level_tres.update(SCREEN)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Level.checkForInput(PLAY_MOUSE_POS):
                    level()    
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Level_two.checkForInput(PLAY_MOUSE_POS):
                    level_two()         
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Level_tres.checkForInput(PLAY_MOUSE_POS):
                    level_tres()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
            

        pygame.display.update()
def main_menu():
    while True:
        SCREEN.fill((0, 0, 100,))
        
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(80).render("Menu principal", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=None, pos=(640, 250), 
                            text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=None, pos=(640, 550), 
                            text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="red")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()
def level():   
 while True:
    
    SCREEN.fill("black")


    pygame.draw.rect(SCREEN, (255, 0, 0), player)
    
    key = pygame.key.get_pressed()
    if key[pygame.K_a] == True:
        player.move_ip(-1, 0)
    elif key[pygame.K_d] == True:
        player.move_ip(1, 0)    
    elif key[pygame.K_w] == True:
        player.move_ip(0, -1)    
    elif key[pygame.K_s] == True:
        player.move_ip(0, 1)    
     

    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            pygame.quit()
            sys.exit()
    for event in pygame.event.get():
        if event.type ==pygame.K_SPACE:
            play()
            #ESCAPE
    if key[pygame.K_ESCAPE] == True:
        play()      
        
#El bucle se mantiene siempre true hasta darle salir que se vuelve false
    pygame.display.update()
    #actualiza la pantalla       
def level_two(): 

 while True:
    
    SCREEN.fill("black")

    pygame.draw.rect(SCREEN, (255, 0, 0), player)
    
    key = pygame.key.get_pressed()
    if key[pygame.K_a] == True:
        player.move_ip(-1, 0)
    elif key[pygame.K_d] == True:
        player.move_ip(1, 0)    
    elif key[pygame.K_w] == True:
        player.move_ip(0, -1)    
    elif key[pygame.K_s] == True:
        player.move_ip(0, 1)    
        
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            pygame.quit()
            sys.exit()
            #escape
    if key[pygame.K_ESCAPE] == True:
        play()  
#El bucle se mantiene siempre true hasta darle salir que se vuelve false
    pygame.display.update()
    #actualiza la pantalla             
def level_tres():

 while True:
    
    SCREEN.fill("black")

    pygame.draw.rect(SCREEN, (255, 0, 0), player)
    
    key = pygame.key.get_pressed()
    if key[pygame.K_a] == True:
        player.move_ip(-1, 0)
    elif key[pygame.K_d] == True:
        player.move_ip(1, 0)    
    elif key[pygame.K_w] == True:
        player.move_ip(0, -1)    
    elif key[pygame.K_s] == True:
        player.move_ip(0, 1)    
        
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            pygame.quit()
            sys.exit()
            #escape
    if key[pygame.K_ESCAPE] == True:
        play()  
#El bucle se mantiene siempre true hasta darle salir que se vuelve false
    pygame.display.update()
    #actualiza la pantalla             
 c


main_menu()