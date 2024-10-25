import pygame
import sys
from button import Button

class LevelSelector:
    def __init__(self, state_manager):
        # Datos de pantalla
        self.state_manager = state_manager
        self.screen = pygame.display.set_mode((1280, 720))  # Creamos la ventana con sus medidas
        self.clock = pygame.time.Clock() # Reloj para controlar los FPS
        
        # Carga de recursos
        self.background = pygame.image.load("assets/sprites/Fondo.jpeg")
        self.level1_image = pygame.image.load("assets/sprites/level1.png")
        
        # Escalar los recursos
        self.level1_image = pygame.transform.scale(self.level1_image, (200, 200))
        
        # Crear btnes
        self.level1_button = Button(self.level1_image, (213, 360), "", self.get_font(25), "Black", "Green")
        self.level2_button = Button(self.level1_image, (640, 360), "", self.get_font(25), "Black", "Green")
        self.level3_button = Button(self.level1_image, (1067, 360), "", self.get_font(25), "Black", "Green")
        self.back_button = Button(None, (640, 600), "Back", self.get_font(25), "White", "Green")   
        
        # Estado de selección del nivel
        self.selected_level = None
    
    def get_font(self, size):
        return pygame.font.Font("font.ttf", size)
    
    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.level1_button.checkForInput(pygame.mouse.get_pos()):
                    self.selected_level = "level1"
                    self.state_manager.set_state("level1")
                if self.level2_button.checkForInput(pygame.mouse.get_pos()):
                    self.selected_level = "Tutorial"
                    self.state_manager.set_state("Tutorial")
                if self.level3_button.checkForInput(pygame.mouse.get_pos()):
                    self.selected_level = "level3"
                    self.state_manager.set_state("level3")
                if self.back_button.checkForInput(pygame.mouse.get_pos()):
                    self.state_manager.set_state("main_menu")
                
    def draw(self, screen):
        self.screen.fill((0, 0, 0))
        # Dibujar botones
        self.level1_button.update(screen)
        self.level2_button.update(screen)
        self.level3_button.update(screen)
        self.back_button.update(screen)
        
        pygame.display.flip()