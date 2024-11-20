import pygame
import sys
from button import Button
from Localization_manager import localization

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
        self.music = pygame.mixer.music.load("assets/sounds/creditos.mp3")
        pygame.mixer.music.play(-1)
        # Escalar los recursos y efecto espejo
        self.back_image = pygame.transform.flip(self.back_image, True, False)
        
        # Crear botones
        self.back_button = Button(self.back_image, (100, 650), "", self.get_font(20), "Black", "Green")
        
        # Carga de texto
        self.font = self.get_font(25)
        
        # Variables de desplazamiento del texto
        self.scroll_y = 720  # Comienza fuera de la pantalla por abajo
        self.scroll_speed = 5  # Velocidad de desplazamiento

     # Cargar sprites
        self.sprites = [
            {"image": pygame.transform.scale(pygame.image.load("assets/sprites/bubble1.png"), (100, 100)), "pos": (100, 400)},
            {"image": pygame.transform.scale(pygame.image.load("assets/sprites/DOCTORACASTAÑAFRENTE.png"), (100, 100)), "pos": (1100, 600)},
            {"image": pygame.transform.scale(pygame.image.load("assets/sprites/health_1.png"), (200, 100)), "pos": (300, 1000)},
            {"image": pygame.transform.scale(pygame.image.load("assets/sprites/MEDICORUBIOFRENTE.png"), (100, 100)), "pos": (570, 1900)},
            {"image": pygame.transform.scale(pygame.image.load("assets/sprites/Options.png"), (100, 100)), "pos": (100, 2400)},
            {"image": pygame.transform.scale(pygame.image.load("assets/sprites/Play.png"), (100, 100)), "pos": (200, 2400)},
            {"image": pygame.transform.scale(pygame.image.load("assets/sprites/Quit.png"), (100, 100)), "pos": (300, 2400)},
            {"image": pygame.transform.scale(pygame.image.load("assets/sprites/win.png"), (100, 100)), "pos": (1150, 2400)},
            {"image": pygame.transform.scale(pygame.image.load("assets/sprites/VIRUSTITLE3.png"), (500, 450)), "pos": (400, 400)},
             {"image": pygame.transform.scale(pygame.image.load("assets/sprites/alpha_logic.png"), (400, 400)), "pos": (430, 2550)},
        ]


        self.update_texts()

    def get_font(self, size):
        return pygame.font.Font("assets/fonts/GAME.TTF", size)
    
    def update_texts(self):
        """Carga los textos para los créditos desde el archivo de localización."""
        self.credits = [
            {"type": "text", "content": localization.get_text('credits_title'), "align": "center"},
            {"type": "text", "content": localization.get_text('thank_you'), "align": "center"},
            {"type": "text", "content": localization.get_text('development_team'), "align": "left"},
            {"type": "text", "content": "Christopher - " + localization.get_text('project_leader'), "align": "left"},
            {"type": "text", "content": "" + localization.get_text(''), "align": "left"},
            {"type": "text", "content": "" + localization.get_text(''), "align": "left"},
            {"type": "text", "content": localization.get_text('art_and_design'), "align": "right"},
            {"type": "text", "content": "Fatima - " + localization.get_text('visual_artist'), "align": "right"},
            {"type": "text", "content": "Ximena - " + localization.get_text('sound_and_music'), "align": "right"},
            {"type": "text", "content": "Fernando - " + localization.get_text('interface_developer'), "align": "right"},
            {"type": "text", "content": "" + localization.get_text(''), "align": "right"},
            {"type": "text", "content": "" + localization.get_text(''), "align": "right"},
            {"type": "text", "content": localization.get_text('programming'), "align": "left"},
            {"type": "text", "content": "Carlos - " + localization.get_text('enemy_movement'), "align": "left"},
            {"type": "text", "content": "Erick - " + localization.get_text('credits_language_switch'), "align": "left"},
            {"type": "text", "content": "" + localization.get_text(''), "align": "left"},
            {"type": "text", "content": "" + localization.get_text(''), "align": "left"},    
            {"type": "text", "content": localization.get_text('quality_assurance'), "align": "center"},
            {"type": "text", "content": localization.get_text('players_and_testers'), "align": "center"},
            {"type": "text", "content": localization.get_text('final_message'), "align": "center"},
            {"type": "text", "content": localization.get_text('final_message2'), "align": "center"},
            {"type": "text", "content": localization.get_text('licenses_and_rights'), "align": "center"},
            {"type": "text", "content": localization.get_text('license'), "align": "center"},
           
              

        ]
    
    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.back_button.checkForInput(pygame.mouse.get_pos()):
                    self.state_manager.set_state("main_menu")
        self.update_texts()

         # Actualiza la posición de desplazamiento del texto
        self.scroll_y -= self.scroll_speed  # El texto se mueve hacia arriba
        
        # Cálculo dinámico de la altura total de los créditos
        total_credits_height = len(self.credits) * 80  # Espaciado entre líneas (80 px por línea)

        # Reinicia el desplazamiento si los créditos salen completamente de la pantalla
        if self.scroll_y + total_credits_height < 0:
            self.scroll_y = 720  # Reinicia el desplazamiento desde la parte inferior

        

    def draw(self, screen):
        """Dibuja los créditos en pantalla."""
        self.screen.blit(self.background, (0, 0))

        for i, element in enumerate(self.credits):
            y_position = self.scroll_y + i * 80
            text = self.font.render(element["content"], True, (0, 0, 0))
            text_rect = text.get_rect()

            if element["align"] == "center":
                text_rect.center = (640, y_position)
            elif element["align"] == "left":
                text_rect.topleft = (50, y_position)
            elif element["align"] == "right":
                text_rect.topright = (1230, y_position)

            self.screen.blit(text, text_rect)
        
        # Dibujar sprites
        for sprite in self.sprites:
            x, y = sprite["pos"]
            adjusted_y = y - (720 - self.scroll_y)  # Ajustar la posición según el desplazamiento
            if -100 < adjusted_y < 720:  # Solo dibujar si están en pantalla
                self.screen.blit(sprite["image"], (x, adjusted_y))



        # Dibujar botón de regreso
        self.back_button.update(screen)
        
        
        
        # Actualizar la pantalla
        pygame.display.flip()
        