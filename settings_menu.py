import pygame
import sys
from button import Button
from Localization_manager import localization



class SettingsMenu:
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
        self.mexico_flag = pygame.image.load("assets/sprites/MexicanFlag.png")
        self.usa_flag = pygame.image.load("assets/sprites/UnitedStatesFlag.png")
        self.volumen_icon = pygame.image.load("assets/sprites/Volume.png")
        font_game = pygame.font.Font("assets/fonts/GAME.TTF", 50)
        font_screen_title = pygame.font.Font("assets/fonts/SCREEN.TTF", 40)
        self.select_sound = pygame.mixer.Sound("assets/sounds/select.mp3")

        # Carga de texto
        self.name = font_game.render("Settings", True, (59, 170, 143))
        self.language = font_screen_title.render("Language", True, (78, 248, 71))
        self.sound = font_screen_title.render("Sound", True, (78, 248, 71))
        self.difficulty_text = font_screen_title.render("Difficulty", True, (78, 248, 71))
        
        # Escalar los recursos
        self.level1_image = pygame.transform.scale(self.level1_image, (200, 200))
        self.dock = pygame.transform.scale(self.dock, (1280, 720))
        self.back_image = pygame.transform.scale(self.back_image, (110, 110))
        self.volumen_icon = pygame.transform.scale(self.volumen_icon, (200, 200))
        
        # Efecto espejo
        self.back_image = pygame.transform.flip(self.back_image, True, False)
        
        # Crear btnes
        self.back_button = Button(self.back_image, (190, 620), "", self.get_font(25), "White", "Green")   
        self.spanish_button = Button(self.mexico_flag, (390, 375), "", self.get_font(25), "White", "Green")
        self.english_button = Button(self.usa_flag, (390, 275), "", self.get_font(25), "White", "Green")
        self.volumen_button = Button(self.volumen_icon, (640, 350), "", self.get_font(25), "White", "Green")
        self.beginner_button = Button(None, (890, 275), "Beginner", self.get_font(25), "White", "Green")
        self.advanced_button = Button(None, (890, 325), "Advanced", self.get_font(25), "White", "Green")
        
        # Estado de selección del nivel
        self.selected_level = None
        
        # Atributo de dificultad
        self.difficulty = "Beginner"

        #Cargar textos iniciales
        self.update_texts()
       
    
    def get_font(self, size):
        return pygame.font.Font("assets/fonts/SCREEN.TTF", size)
    
    def update_texts(self):
        # Usar localization para obtener los textos actuales según el idioma
        self.name = self.get_font(50).render(localization.get_text("settings"), True, (59, 170, 143))
        self.language = self.get_font(40).render(localization.get_text("language"), True, (78, 248, 71))
        self.sound = self.get_font(40).render(localization.get_text("sound"), True, (78, 248, 71))
        self.difficulty_text = self.get_font(40).render(localization.get_text("difficulty"), True, (78, 248, 71))
        # También puedes actualizar otros botones de nivel de dificultad, si cambian con el idioma
    
    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.beginner_button.checkForInput(pygame.mouse.get_pos()):
                    self.difficulty = "Beginner"
                    self.select_sound.play()
                    self.state_manager.set_difficulty(self.difficulty)
                    
                if self.advanced_button.checkForInput(pygame.mouse.get_pos()):
                    self.difficulty = "Advanced"
                    print(self.difficulty)
                    self.state_manager.set_difficulty(self.difficulty)
                    
                if self.back_button.checkForInput(pygame.mouse.get_pos()):
                    self.state_manager.set_state("main_menu")
                elif self.english_button.checkForInput(pygame.mouse.get_pos()):
                    localization.set_language("en")
                    self.update_texts()  # Actualizar los textos al cambiar de idioma
                    
                elif self.spanish_button.checkForInput(pygame.mouse.get_pos()):
                    localization.set_language("es")
                    self.update_texts()  # Actualizar los textos al cambiar de idioma
                  
    def draw(self, screen):
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.dock, (0, 0))
        # Dibujar botones
        self.back_button.update(screen)
        self.spanish_button.update(screen)
        self.english_button.update(screen)
        self.volumen_button.update(screen)
        self.beginner_button.update(screen)
        self.advanced_button.update(screen)
        # Dibujar texto
        self.screen.blit(self.name, self.name.get_rect(center=(640, 50)))
        self.screen.blit(self.language, self.language.get_rect(center=(390, 200)))
        self.screen.blit(self.sound, self.sound.get_rect(center=(640, 200)))
        self.screen.blit(self.difficulty_text, self.difficulty_text.get_rect(center=(890, 200)))        
        pygame.display.flip()