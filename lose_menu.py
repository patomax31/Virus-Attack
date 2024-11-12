import pygame
import sys
from button import Button

class LoseMenu:
    def __init__(self, state_manager):
        # Datos de pantalla
        self.state_manager = state_manager
        self.selected_level = None
        self.screen = pygame.display.set_mode((1280, 720))  # Creamos la ventana con sus medidas
        self.clock = pygame.time.Clock() # Reloj para controlar los FPS

        # Carga de recursos
        self.lose_sound = pygame.mixer.Sound("assets/sounds/perder.mp3")
        self.background = pygame.image.load("assets/sprites/FONDOSELECCIONPERSONAJE1.png")
        self.dock = pygame.image.load("assets/sprites/PANTALLASELECCIONPERSONAJE1.png")
        self.level1_image = pygame.image.load("assets/sprites/level1.png")
        self.back_image = pygame.image.load("assets/sprites/BOTONSIGUIENTE.png")
        font_game = pygame.font.Font("assets/fonts/GAME.TTF", 50)
        font_screen_title = pygame.font.Font("assets/fonts/SCREEN.TTF", 40)
        
        # Carga de texto
        self.name = font_game.render("Echale mas ganas we", True, (59, 170, 143))
        # Escalar los recursos
        self.level1_image = pygame.transform.scale(self.level1_image, (200, 200))
        self.dock = pygame.transform.scale(self.dock, (1280, 720))
        
        # Efecto espejo

        # Crear btnes 
        
        # Estado de selección del nivel
        self.selected_level = None
    
    def get_font(self, size):
        return pygame.font.Font("assets/fonts/GAME.TTF", size)
    
    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
    def draw(self, screen):
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.dock, (0, 0))

        # Dibujar botones
        # Dibujar texto
        self.screen.blit(self.name, self.name.get_rect(center=(640, 50)))        
        pygame.display.flip()