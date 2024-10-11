import pygame
import sys
from settings import SCREEN_WIDTH, SCREEN_HEIGHT
from button import Button
import lv_selector 

def levels():
    lv_selector.level_selector()

def main_menu():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # Creamos la ventana con sus medidas
    clock = pygame.time.Clock() # Creamos est amadre que es para controlar los FPS
    
    # Inicializamos el grupo de burbujas
    all_bubbles = pygame.sprite.Group()

    #FONDO
    bg= pygame.image.load("assets/sprites/Fondo.jpeg")
    #Fuentes de texto
    def get_font(size): # Funcion para obtener la fuente de texto
        return pygame.font.Font("font.ttf", size) # Devuelve la fuente de texto con el tamaño especificado

    running = True # Creamos esta variable que controla is el juego esta corriendo
    
    #IMAGENES DE LOS BOTONES
    Play=pygame.image.load("assets/sprites/Play.png")
    Play = pygame.transform.scale(Play, (200, 200))

    Quit=pygame.image.load("assets/sprites/Quit.png")
    Quit = pygame.transform.scale(Quit, (200, 200))

    Options = pygame.image.load("assets/sprites/Options.png")
    Options = pygame.transform.scale(Options, (200, 200))
    
    title = pygame.image.load("assets/sprites/Title.png")
    title = pygame.transform.scale(title, (1300, 1000))
    while True:
        screen.fill((0, 0, 100,))


        MENU_MOUSE_POS = pygame.mouse.get_pos()

        #MENU_TEXT = get_font(60).render("VIRUS ATTACK", True, "#f57842")
        #MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=Play, pos=(640, 350), 
                            text_input=None, font=get_font(75), base_color="green", hovering_color="White")
       
        QUIT_BUTTON = Button(image=Quit, pos=(1000, 350), 
                            text_input=None, font=get_font(75), base_color="black", hovering_color="white")

        OPTIONS_BUTTON = Button(image=Options, pos=(250, 350), 
                                    text_input=None, font=get_font(75), base_color="black", hovering_color="white")
        #Muestra el fondo y el titulo del videojuego
        screen.blit(bg, (0, 0))
        screen.blit(title, (0, 0))
      #  screen.blit(MENU_TEXT, MENU_RECT)
        
        
        for button in [PLAY_BUTTON, QUIT_BUTTON, OPTIONS_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
       #     button.update(screen=pygame.image.load("Quit.png"))
            button.update(screen)

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    levels()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()
        
main_menu()