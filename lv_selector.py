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
        self.back_button = Button(None, (640, 600), "Back", self.get_font(25), "Black", "Green")   
        
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
                    self.selected_level = "level2"
                    self.state_manager.set_state("level2")
                if self.level3_button.checkForInput(pygame.mouse.get_pos()):
                    self.selected_level = "level3"
                    self.state_manager.set_state("level3")
                if self.back_button.checkForInput(pygame.mouse.get_pos()):
                    self.state_manager.set_state("main_menu")
                
    def draw(self, screen):
        screen.fill((0, 0, 0))
        
        # Creacion de las columnas
        column_width = self.screen.get_width() // 3
        for i in range(3):
            rect = pygame.Rect(i * column_width, 0, column_width, self.screen.get_height())
            if self.selected_level == f"level{i+1}":
                screen.blit(getattr(self, f"level{i+1}_image"), rect.topleft)
            elif rect.collidepoint(pygame.mouse.get_pos()):
                dark_surface = pygame.Surface((column_width, self.screen.get_height()))
                dark_surface.set_alpha(128)
                dark_surface.fill((255, 255, 255))
                screen.blit(dark_surface, rect.topleft)
                
        # Dibujar botones
        self.level1_button.update(screen)
        self.level2_button.update(screen)
        self.level3_button.update(screen)
        self.back_button.update(screen)
        
        pygame.display.flip()