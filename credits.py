import pygame
import sys
from button import Button


class CreditsScreen:
    
    def __init__(self, state_manager):
        # Datos de pantalla
        self.state_manager = state_manager
        self.selected_level = None
        self.screen = pygame.display.set_mode((1280, 720)) # Creamos la ventana con sus medidas
        self.clock = pygame.time.Clock() # Reloj para controlar los FPS
        
        # Carga de recursos
        self.background = pygame.image.load("assets/sprites/FONDOSELECCIONPERSONAJE1.png")
        self.back_image = pygame.image.load("assets/sprites/BOTONCONTINUAR.png")
        
        # Escalar los recursos y efecto espejo
        self.back_image = pygame.transform.flip(self.back_image, True, False)
        
        # Crear botones
        self.back_button = Button(self.back_image, (100, 650), "", self.get_font(20), "Black", "Green")
        
        # Carga de texto
        self.font = self.get_font(36)
        self.credits = [
            "Integrante 1 - Rol 1",
            "Integrante 2 - Rol 2",
            "Integrante 3 - Rol 3",
            "Integrante 4 - Rol 4",
            "Integrante 5 - Rol 5",
            "Integrante 6 - Rol 6"
        ]

    def get_font(self, size):
        return pygame.font.Font("assets/fonts/GAME.TTF", size)
    
    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.back_button.checkForInput(pygame.mouse.get_pos()):
                    self.state_manager.set_state("main_menu")
                    
    def draw(self, screen):
        # Dibujar los elementos en pantalla
        screen.blit(self.background, (0, 0))
        
        # Dibujar los botones
        self.back_button.update(screen)
        
        # Dibujar el texto
        for i, line in enumerate(self.credits):
            text = self.font.render(line, True, (0, 0, 0))
            screen.blit(text, (50, 150 + i * 40))
            
        # Actualizar la pantalla
        pygame.display.flip()