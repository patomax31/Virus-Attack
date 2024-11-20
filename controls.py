import pygame
import sys
from button import Button
from Localization_manager import localization

class ControlsScreen:
    
    def __init__(self, state_manager):
        # Datos de pantalla
        self.state_manager = state_manager
        self.selected_level = None
        self.screen = pygame.display.set_mode((1280, 720)) # Creamos la ventana con sus medidas
        self.clock = pygame.time.Clock() # Reloj para controlar los FPS
        
        # Carga de recursos
        
        font_game = pygame.font.Font("assets/fonts/GAME.TTF", 27)
        self.back_image = pygame.image.load("assets/sprites/BOTONCONTINUAR.png")
        #Textos
    
        self.howtoplay_text = font_game.render(localization.get_text("how_to_play"), True, (0, 0, 0))  # Negro
        
        

        # Escalar los recursos y efecto espejo
        self.back_image = pygame.transform.flip(self.back_image, True, False)
        
        # Crear botones
        self.back_button = Button(self.back_image, (100, 650), "", self.get_font(20), "Black", "Green")
        
        # Carga de texto
        self.font = self.get_font(1)
        
    def get_font(self, size):
        return pygame.font.Font("assets/fonts/GAME.TTF", size)
    
    def update_texts(self):
        # Actualizar el texto del título según el idioma
        self.howtoplay_text = self.get_font(1).render(localization.get_text("how_to_play"), True, (0, 0, 0))
        

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.back_button.checkForInput(pygame.mouse.get_pos()):
                    self.state_manager.set_state("main_menu")
  
        
    def draw(self, screen):
        self.screen.blit(self.background, (0, 0))

        # Dibujar botón de regreso
        self.back_button.update(screen)
        
        self.screen.blit(self.howtoplay_text, self.howtoplay_text.get_rect(center=(660, 30)))
        

        # Actualizar la pantalla
        pygame.display.flip()