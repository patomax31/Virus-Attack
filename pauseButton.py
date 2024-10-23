import pygame
from settings import SCREEN_WIDTH

class PauseButton:
    def __init__(self):
        self.image = pygame.image.load("assets/sprites/pauseButton.png").convert_alpha() # Cargamos la imagen del boton de pausa
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH // 2, 50)) # cnb esto centramos el boton en el centro

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def is_clicked(self, pos): # funcion para en caso de que se le de click al boton
        return self.rect.collidepoint(pos) # Devuelve true si el boton ha sido clickeado