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
        self.background = pygame.image.load("Manual.jpg")
        font_game = pygame.font.Font("assets/fonts/GAME.TTF", 27)
        self.back_image = pygame.image.load("assets/sprites/BOTONCONTINUAR.png")
        #Textos
        self.w_text = font_game.render(localization.get_text("w_text"), True, (0, 0, 0))  # Negro
        self.a_text = font_game.render(localization.get_text("a_text"), True, (0, 0, 0))  # Negro
        self.s_text = font_game.render(localization.get_text("s_text"), True, (0, 0, 0))  # Negro
        self.d_text = font_game.render(localization.get_text("d_text"), True, (0, 0, 0))  # Negro
        self.spacebar_text = font_game.render(localization.get_text("spacebar_text"), True, (0, 0, 0))  # Negro
        self.howtoplay_text = font_game.render(localization.get_text("how_to_play"), True, (0, 0, 0))  # Negro
        self.howtowin_text = font_game.render(localization.get_text("how_to_win"), True, (0, 0, 0))  # Negro
        self.howtolose_text = font_game.render(localization.get_text("how_to_lose"), True, (0, 0, 0))  # Negro
        

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
        self.w_text = self.get_font(1).render(localization.get_text("w_text"), True, (0, 0, 0))
        self.a_text = self.get_font(1).render(localization.get_text("a_text"), True, (0, 0, 0))
        self.s_text = self.get_font(1).render(localization.get_text("s_text"), True, (0, 0, 0))
        self.d_text = self.get_font(1).render(localization.get_text("d_text"), True, (0, 0, 0))
        self.spacebar_text = self.get_font(1).render(localization.get_text("spacebar_text"), True, (0, 0, 0))
        self.howtoplay_text = self.get_font(1).render(localization.get_text("how_to_play"), True, (0, 0, 0))
        self.win_text = self.get_font(1).render(localization.get_text("how_to_win"), True, (0, 0, 0))
        self.lose_text = self.get_font(1).render(localization.get_text("how_to_lose"), True, (0, 0, 0))

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
        self.screen.blit(self.w_text, self.w_text.get_rect(center=(500, 160)))
        self.screen.blit(self.a_text, self.a_text.get_rect(center=(560, 295)))
        self.screen.blit(self.s_text, self.s_text.get_rect(center=(498, 420)))
        self.screen.blit(self.d_text, self.d_text.get_rect(center=(550, 545)))
        self.screen.blit(self.spacebar_text, self.spacebar_text.get_rect(center=(600, 660)))
        self.screen.blit(self.howtoplay_text, self.howtoplay_text.get_rect(center=(660, 30)))
        self.screen.blit(self.howtowin_text, self.howtowin_text.get_rect(center=(1070, 130)))
        self.screen.blit(self.howtolose_text, self.howtolose_text.get_rect(center=(1070, 500)))

        # Actualizar la pantalla
        pygame.display.flip()