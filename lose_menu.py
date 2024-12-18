import pygame
import sys
from button import Button
from Localization_manager import localization

class LoseMenu:
    def __init__(self, state_manager):
        # Datos de pantalla
        self.state_manager = state_manager
        self.selected_level = None
        self.screen = pygame.display.set_mode((1280, 720))  # Creamos la ventana con sus medidas
        self.clock = pygame.time.Clock() # Reloj para controlar los FPS

        # Carga de recursos
        self.background = pygame.image.load("assets/sprites/FONDOSELECCIONPERSONAJE1.png")
        self.lose_sound = pygame.mixer.Sound("assets/sounds/perder.mp3")
        self.level1_image = pygame.image.load("assets/sprites/level1.png")
        self.back_image = pygame.image.load("assets/sprites/BOTONSIGUIENTE.png")
        self.boton = pygame.image.load("assets/sprites/BOTONSIGUIENTE.png")
        self.reinicio = pygame.image.load("assets/sprites/BOTONreinicio.png")
        font_game = pygame.font.Font("assets/fonts/GAME.TTF", 50)
        font_screen_title = pygame.font.Font("assets/fonts/SCREEN.TTF", 40)
        
        # Carga de imágenes de la animación del título
        self.lose_frames = [
        
            pygame.transform.scale(pygame.image.load("assets/sprites/PANTALLAPERDER1.png"), (1280, 720)),
            pygame.transform.scale(pygame.image.load("assets/sprites/PANTALLAPERDER2.png"), (1280, 720)),
            pygame.transform.scale(pygame.image.load("assets/sprites/PANTALLAPERDER3.png"), (1280, 720)),
            pygame.transform.scale(pygame.image.load("assets/sprites/PANTALLAPERDER4.png"), (1280, 720)),
            pygame.transform.scale(pygame.image.load("assets/sprites/PANTALLAPERDER5.png"), (1280, 720))
        ]
        self.current_frame = 0
        self.animation_timer = 0
        self.animation_speed = 200  # Velocidad de la animación en milisegundos
        # Carga de texto
        self.name = font_game.render("loae_text", True, (59, 170, 143))
        # Escalar los recursos
        self.level1_image = pygame.transform.scale(self.level1_image, (200, 200))
        self.boton = pygame.transform.scale(self.boton, (110, 110))
        self.back_image = pygame.transform.scale(self.back_image, (110, 110))
        
        self.reinicio = pygame.transform.scale(self.reinicio, (110, 110))
        
        
        # Efecto espejo

        self.back_image = pygame.transform.flip(self.back_image, True, False)
        
        # Crear btnes 
        self.accept_button = Button(self.boton, (1110, 620), "", self.get_font(25), "White", "Green")
        self.back_button = Button(self.back_image, (190, 620), "", self.get_font(25), "White", "Green")
        self.reiniciar_button = Button(self.reinicio, (660, 630), "", self.get_font(25), "White", "Green")
        # Estado de selección del nivel
        self.selected_level = None
    
    def get_font(self, size):
        return pygame.font.Font("assets/fonts/GAME.TTF", size)
    
    def update_text(self):
        self.name = self.get_font(50).render(localization.get_text("lose_text"), True, (59, 170, 143))
    
    def update_animation(self, dt):
        self.animation_timer += dt
        if self.animation_timer >= self.animation_speed:
            self.animation_timer = 0
            self.current_frame = (self.current_frame + 1) % len(self.lose_frames)
    
    def update(self):
        dt = self.clock.tick(60)
        self.update_animation(dt)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.back_button.checkForInput(pygame.mouse.get_pos()):
                    self.state_manager.set_state("levels")
                if self.reiniciar_button.checkForInput(pygame.mouse.get_pos()):
                    current_level = self.state_manager.get_current_level()
                    self.state_manager.set_state(f"level{current_level}")

        self.update_text()         

    def draw(self, screen):
        self.screen.blit(self.background, (0, 0))
        loser_image = self.lose_frames[self.current_frame]
        loser_rect = loser_image.get_rect(center=(660, 390))
        self.screen.blit(loser_image, loser_rect)
        self.back_button.update(screen)
        self.reiniciar_button.update(screen)

        # Dibujar botones
        
        # Dibujar texto
        self.screen.blit(self.name, self.name.get_rect(center=(640, 50)))        
        pygame.display.flip()