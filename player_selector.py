import pygame
import sys
from button import Button
from Localization_manager import localization

class PlayerSelector:
    def __init__(self, state_manager):
        # Datos de pantalla
        self.state_manager = state_manager
        self.selected_level = None
        self.screen = pygame.display.set_mode((1280, 720))  # Creamos la ventana con sus medidas
        self.clock = pygame.time.Clock() # Reloj para controlar los FPS
        
        # Carga de recursos
        self.select_sound = pygame.mixer.Sound("assets/sounds/select.mp3")
        font_game = pygame.font.Font("assets/fonts/GAME.TTF", 50)
        font_screen = pygame.font.Font("assets/fonts/SCREEN.TTF", 65)
        # Carga de imagenes
        self.background = pygame.image.load("assets/sprites/FONDOSELECCIONPERSONAJE1.png")
        self.dock = pygame.image.load("assets/sprites/PANTALLASELECCIONPERSONAJE1.png")
        self.continue_image = pygame.image.load("assets/sprites/BOTONSIGUIENTE.png")
        self.back_image = pygame.image.load("assets/sprites/BOTONSIGUIENTE.png")
        # Carga de texto
        self.name = font_game.render("Select your character", True, (59, 170, 143))
        self.pj_text = ["DR. JUAN\nHERNANDEZ", "DR. MARIA\nGARCIA", "DR. PEDRO\nLOPEZ", "DR. ANA\nMARTINEZ"]  # Lista de textos
        self.current_pj_index = 0
        self.pj = self.render_multiline_text(self.pj_text[self.current_pj_index], font_screen, (78, 248, 71))
        # Rectangulo del texto
        self.name_rect = self.name.get_rect(center=(680, 50))
        self.pj_rect = self.pj.get_rect(center=(490, 330))
        
        # Escalar los recursos
        self.dock = pygame.transform.scale(self.dock, (1280, 720))
        self.continue_image = pygame.transform.scale(self.continue_image, (110, 110))
        self.back_image = pygame.transform.scale(self.back_image, (110, 110))
        
        # Efecto espejo
        self.back_image = pygame.transform.flip(self.back_image, True, False)
        
        # Crear btnes
        self.accept_button = Button(self.continue_image, (1110, 620), "", self.get_font_screen(25), "White", "Green")
        self.back_button = Button(self.back_image, (190, 620), "", self.get_font_screen(25), "White", "Green")   
        
        # Estado de selección del nivel
        self.selected_level = None
        
        # Cargar imagenes de personajes
        
        self.character_images = [
            pygame.transform.scale(pygame.image.load("assets/sprites/OPCIONPERSONAJEMORENO.png"), (700, 400)),
            pygame.transform.scale(pygame.image.load("assets/sprites/OPCIONPERSONAJEMORENA.png"), (700, 400)),
            pygame.transform.scale(pygame.image.load("assets/sprites/OPCIONPERSONAJERUBIO.png"), (700, 400)),
            pygame.transform.scale(pygame.image.load("assets/sprites/OPCIONPERSONAJEPELIRROJA.png"), (700, 400)),
        ]
        self.current_character_index = 0
        self.update_text()
        
    def render_multiline_text(self, text, font, color):
        lines = text.split('\n')
        surfaces = [font.render(line, True, color) for line in lines]
        max_width = max(surface.get_width() for surface in surfaces)
        total_height = sum(surface.get_height() for surface in surfaces)
        text_surface = pygame.Surface((max_width, total_height), pygame.SRCALPHA)
        y_offset = 0
        for surface in surfaces:
            text_surface.blit(surface, (0, y_offset))
            y_offset += surface.get_height()
        return text_surface
    
    def get_font(self, size):
        return pygame.font.Font("assets/fonts/GAME.TTF", size)
    
    def update_text(self):
        font_screen = pygame.font.Font("assets/fonts/SCREEN.TTF", 65)
        self.pj = self.render_multiline_text(self.pj_text[self.current_pj_index], font_screen, (78, 248, 71))
        self.pj_rect = self.pj.get_rect(center=(490, 330))
        self.name = self.get_font(45).render(localization.get_text("select your character"), True, (59, 170, 143))

    def get_font_game(self, size):
        return pygame.font.Font("assets/fonts/GAME.TTF", size)
    
    def get_font_screen(self, size):
        return pygame.font.Font("assets/fonts/SCREEN.TTF", size)
    
    def update(self):
        self.selected_level = self.state_manager.get_selected_level()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.accept_button.checkForInput(pygame.mouse.get_pos()):
                    self.select_sound.play()
                    self.state_manager.set_selected_character(self.current_pj_index)
                    print(f"PlayerSelector: selected_character set to {self.current_character_index}")                  
                    self.state_manager.set_state("levels")
                if self.back_button.checkForInput(pygame.mouse.get_pos()):
                    self.select_sound.play()
                    self.state_manager.set_state("main_menu")
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.state_manager.set_state("main_menu")
                elif event.key == pygame.K_RETURN:
                    self.state_manager.set_selected_character(self.current_pj_index)
                    print(f"PlayerSelector: selected_character set to {self.current_character_index}")
                    self.state_manager.set_state("levels")  # Cambia al selector de niveles
                elif event.key == pygame.K_LEFT:
                    self.current_character_index = (self.current_character_index - 1) % len(self.character_images)
                    self.current_pj_index = (self.current_pj_index - 1) % len(self.pj_text)
                    print(f"current_pj_index: {self.current_pj_index}, current_character_index: {self.current_character_index}")
                    self.update_text()
                elif event.key == pygame.K_RIGHT:
                    self.current_character_index = (self.current_character_index + 1) % len(self.character_images)
                    self.current_pj_index = (self.current_pj_index + 1) % len(self.pj_text)
                    print(f"current_pj_index: {self.current_pj_index}, current_character_index: {self.current_character_index}")
                    self.update_text()
            self.update_text()                
                
    def draw(self, screen):
        # Dibujar fondo
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.dock, (0, 0))
        # Dibujar botones
        self.accept_button.update(screen)
        self.back_button.update(screen)
        # Dibujar texto
        self.screen.blit(self.name, self.name_rect)
        self.screen.blit(self.pj, self.pj_rect)
        # Dibujar personaje
        current_character_image = self.character_images[self.current_character_index]
        character_rect = current_character_image.get_rect(center=(720, 310))
        self.screen.blit(current_character_image, character_rect.topleft)
        
        
        pygame.display.flip()