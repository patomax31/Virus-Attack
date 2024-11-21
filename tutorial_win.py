import pygame
import sys
from button import Button
from Localization_manager import localization

class WinMenu_Tutorial:
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
        self.moreno = pygame.image.load("assets/sprites/medicDown.png")
        self.guero = pygame.image.load("assets/sprites/MEDICORUBIOFRENTE.png")
        self.morenita = pygame.image.load("assets/sprites/DOCTORACASTAÑAFRENTE.png")
        self.rojo = pygame.image.load("assets/sprites/DOCTORAVISTAFRENTE.png")
        self.copa = pygame.image.load("assets/sprites/win.png")
        self.boton = pygame.image.load("assets/sprites/BOTONSIGUIENTE.png")
        self.back_image = pygame.image.load("assets/sprites/BOTONSIGUIENTE.png")
        self.reinicio = pygame.image.load("assets/sprites/BOTONreinicio.png")
        font_game = pygame.font.Font("assets/fonts/GAME.TTF", 50)
        font_screen_title = pygame.font.Font("assets/fonts/SCREEN.TTF", 40)
        
        # Carga de texto
        self.name = font_game.render("win_text", True, (59, 170, 143))
        
        # Escalar los recursos
        self.level1_image = pygame.transform.scale(self.level1_image, (200, 200))
        self.dock = pygame.transform.scale(self.dock, (1280, 720))
        self.moreno = pygame.transform.scale(self.moreno, (100, 100))
        self.morenita = pygame.transform.scale(self.morenita, (100, 100))
        self.guero = pygame.transform.scale(self.guero, (100, 100))
        self.rojo = pygame.transform.scale(self.rojo, (100, 100))
        self.copa = pygame.transform.scale(self.copa, (100, 100))
        self.boton = pygame.transform.scale(self.boton, (110, 110))
        self.back_image = pygame.transform.scale(self.back_image, (110, 110))
        self.reinicio = pygame.transform.scale(self.reinicio, (110, 110))
        # Efecto espejo
        self.back_image = pygame.transform.flip(self.back_image, True, False)
        # Crear btnes 
        self.accept_button = Button(self.boton, (1110, 620), "", self.get_font(25), "White", "Green")
        self.back_button = Button(self.back_image, (190, 620), "", self.get_font(25), "White", "Green") 
        # Estado de selección del nivel
        self.selected_level = None
    
    def get_font(self, size):
        return pygame.font.Font("assets/fonts/GAME.TTF", size)
    
    def update_text(self):
        self.name = self.get_font(50).render(localization.get_text("win_text"), True, (59, 170, 143))
    
    def update(self):
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:  
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.accept_button.checkForInput(pygame.mouse.get_pos()):
                    self.selected_level = "level2"
                    self.state_manager.set_state("level2", self.selected_level)
                if self.back_button.checkForInput(pygame.mouse.get_pos()):
                    self.state_manager.set_state("main_menu")
        self.update_text()
                    
    def draw(self, screen):
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.dock, (0, 0))
        self.screen.blit(self.moreno, (450, 330))
        self.screen.blit(self.morenita, (650, 330))
        self.screen.blit(self.guero, (550, 330))
        self.screen.blit(self.rojo, (750, 330))
        self.screen.blit(self.copa, (600, 200))
        self.screen.blit(self.boton,(1050, 580 ))
        self.screen.blit(self.back_image, (150, 580))
        self.screen.blit(self.reinicio, (610, 580))
        # Dibujar botones
        
        # Dibujar texto
        self.screen.blit(self.name, self.name.get_rect(center=(640, 50)))        
        pygame.display.flip()