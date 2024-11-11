import pygame
import sys
from button import Button
from Localization_manager import localization
from progress import get_current_level

class LevelSelector:
    def __init__(self, state_manager):
        # Datos de pantalla
        self.state_manager = state_manager
        self.selected_level = None
        self.screen = pygame.display.set_mode((1280, 720))  # Creamos la ventana con sus medidas
        self.clock = pygame.time.Clock() # Reloj para controlar los FPS
        
        # Carga de recursos
        self.background = pygame.image.load("assets/sprites/FONDOSELECCIONPERSONAJE1.png")
        self.dock = pygame.image.load("assets/sprites/PANTALLASELECCIONPERSONAJE1.png")
        self.level1_image = pygame.image.load("assets/sprites/level1.png")
        self.back_image = pygame.image.load("assets/sprites/BOTONSIGUIENTE.png")
        font_game = pygame.font.Font("assets/fonts/GAME.TTF", 50)

        
        # Carga de texto
        self.name = font_game.render(localization.get_text("Select a level"), True, (59, 170, 143))
        
        
        # Escalar los recursos
        self.level1_image = pygame.transform.scale(self.level1_image, (200, 200))
        self.dock = pygame.transform.scale(self.dock, (1280, 720))
        self.back_image = pygame.transform.scale(self.back_image, (110, 110))
        
        # Efecto espejo
        self.back_image = pygame.transform.flip(self.back_image, True, False)
        
        # Crear btnes
        self.level1_button = Button(self.level1_image, (390, 300), "", self.get_font(25), "Black", "Green")
        self.level2_button = Button(self.level1_image, (650, 300), "", self.get_font(25), "Black", "Green")
        self.level3_button = Button(self.level1_image, (910, 300), "", self.get_font(25), "Black", "Green")
        self.back_button = Button(self.back_image, (190, 620), "", self.get_font(25), "White", "Green")   
        
        # Estado de selección del nivel
        self.selected_level = None
        
        self.update_texts()
        
        # Desbloquear niveles segun progreso
        self.current_level = get_current_level()
        self.update_level_buttons()
        
    def update_level_buttons(self):
        if self.current_level < 2:
            self.level2_button.disabled = True
        if self.current_level < 3:
            self.level3_button.disabled = True
        
    def get_font(self, size):
        return pygame.font.Font("font.ttf", size)
    
    def update_texts(self):
        # Actualizar el texto del título según el idioma
        self.name = self.get_font(45).render(localization.get_text("select a level"), True, (59, 170, 143))

        

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.level1_button.checkForInput(pygame.mouse.get_pos()):
                    self.selected_level = "level1"
                    self.state_manager.set_state("player_selector", self.selected_level)
                if self.level2_button.checkForInput(pygame.mouse.get_pos()) and self.current_level >= 2:
                    self.selected_level = "level2"
                    self.state_manager.set_state("player_selector", self.selected_level)
                if self.level3_button.checkForInput(pygame.mouse.get_pos()) and self.current_level >= 3:
                    self.selected_level = "level3"
                    self.state_manager.set_state("player_selector", self.selected_level)
                if self.back_button.checkForInput(pygame.mouse.get_pos()):
                    self.state_manager.set_state("main_menu")
            self.update_texts()  
    def draw(self, screen):
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.dock, (0, 0))
        # Dibujar botones
        self.level1_button.update(screen)
        self.level2_button.update(screen)
        self.level3_button.update(screen)
        self.back_button.update(screen)
        # Dibujar texto
        self.screen.blit(self.name, self.name.get_rect(center=(640, 50)))
        
        pygame.display.flip()