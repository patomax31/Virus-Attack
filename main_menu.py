import pygame
import sys
from button import Button

class MainMenu:
    
    def __init__(self, state_manager):
        # Datos de pantalla
        self.state_manager = state_manager
        self.screen = pygame.display.set_mode((1280, 720)) # Creamos la ventana con sus medidas
        self.clock = pygame.time.Clock() # Reloj para controlar los FPS
        
        # Carga de recursos
        self.background = pygame.image.load("assets/sprites/Fondo.jpeg")
        self.play_image = pygame.image.load("assets/sprites/play.png")
        self.quit_image = pygame.image.load("assets/sprites/quit.png")
        self.options_image = pygame.image.load("assets/sprites/options.png")
        self.title_image = pygame.image.load("assets/sprites/title.png")
        
        # Escalar los recursos
        self.play_image = pygame.transform.scale(self.play_image, (250, 250))
        self.quit_image = pygame.transform.scale(self.quit_image, (200, 200))
        self.options_image = pygame.transform.scale(self.options_image, (200, 200))
                
        # Creacion de los btones
        self.play_button = Button(self.play_image, (640, 615), "", self.get_font(25), "Black", "Green")
        self.options_button = Button(self.options_image, (440, 615), "", self.get_font(25), "Black", "Green")
        self.quit_button = Button(self.quit_image, (840, 615), "", self.get_font(25), "Black", "Green")
        
        # Inicializacion de la futura msica
        
    def get_font(self, size):
        return pygame.font.Font("font.ttf", size) # Devuelve la fuente de texto con el tamaño especificado
    
    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN: # Si se presiona el mouse
                if self.play_button.checkForInput(pygame.mouse.get_pos()):
                    self.state_manager.set_state("levels") # Cambia el estado a levels
                if self.quit_button.checkForInput(pygame.mouse.get_pos()):
                    pygame.quit()
                    sys.exit()
                    
    def draw(self, screen):
        screen.blit(self.background, (0, 0))
        screen.blit(self.title_image, (0, 0))
        self.play_button.update(screen)
        self.options_button.update(screen)
        self.quit_button.update(screen)
        pygame.display.flip()