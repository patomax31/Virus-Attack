import pygame
import sys
from button import Button
from Localization_manager import localization


class Button:
    def __init__(self, image, pos, text_input, font, base_color, hovering_color, text_offset=(0, 0)):
        self.original_image = image
        self.image = image
        self.hover_image = pygame.transform.scale(image, (int(image.get_width() * 1.2), int(image.get_height() * 1.2)))  # Ajustar el tamaño de la imagen al pasar el mouse
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.font = font
        self.base_color = base_color
        self.hovering_color = hovering_color
        self.text_input = text_input
        self.text_offset = text_offset
        self.text = self.font.render(self.text_input, True, self.base_color)
        if self.image is None:
            self.image = self.text
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_rect = self.text.get_rect(center=(self.x_pos + self.text_offset[0], self.y_pos + self.text_offset[1]))

    def update(self, screen):
        screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)

    def checkForInput(self, position):
        return self.rect.collidepoint(position)

    def changeImage(self, position):
        if self.checkForInput(position):
            self.image = self.hover_image
            self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))  # Actualizar la posición del rectángulo
            self.text = self.font.render(self.text_input, True, self.hovering_color)
        else:
            self.image = self.original_image
            self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))  # Actualizar la posición del rectángulo
            self.text = self.font.render(self.text_input, True, self.base_color)
class SettingsMenu:
    def __init__(self, state_manager):
        self.state_manager = state_manager
        self.selected_level = None
        self.screen = pygame.display.set_mode((1280, 720))
        self.clock = pygame.time.Clock()

        # Carga de recursos
        self.background = pygame.image.load("assets/sprites/FONDOSELECCIONPERSONAJE1.png")
        self.dock = pygame.image.load("assets/sprites/PANTALLASELECCIONPERSONAJE1.png")
        self.level1_image = pygame.image.load("assets/sprites/level1.png")
        self.back_image = pygame.image.load("assets/sprites/BOTONSIGUIENTE.png")
        self.mexico_flag = pygame.image.load("assets/sprites/españa.png")
        self.usa_flag = pygame.image.load("assets/sprites/UnitedStatesFlag.png")
        self.volumen_icon = pygame.image.load("assets/sprites/Volume.png")
        font_game = pygame.font.Font("assets/fonts/GAME.TTF", 50)
        font_screen_title = pygame.font.Font("assets/fonts/GAME.TTF", 40)
        self.select_sound = pygame.mixer.Sound("assets/sounds/select.mp3")
        self.difficulty_image = pygame.image.load("assets/sprites/boton_crditos1.png")
        
        # Carga de texto
        self.name = font_game.render("Settings", True, (59, 170, 143))
        self.language = font_screen_title.render("Language", True, (78, 248, 71))
        self.sound = font_screen_title.render("Music", True, (78, 248, 71))
        self.difficulty_text = font_screen_title.render("Difficulty", True, (78, 248, 71))
        
        # Escalar los recursos
        self.dock = pygame.transform.scale(self.dock, (1280, 720))
        self.back_image = pygame.transform.scale(self.back_image, (110, 110))
        self.volumen_icon = pygame.transform.scale(self.volumen_icon, (200, 200))
        self.difficulty_image = pygame.transform.scale(self.difficulty_image, (200, 150))
        self.sound_on = True
        
        # Efecto espejo
        self.back_image = pygame.transform.flip(self.back_image, True, False)
        
        # Crear botones
        self.back_button = Button(self.back_image, (190, 620), "", self.get_font(25), "White", "Green")
        self.spanish_button = Button(self.mexico_flag, (390, 375), "", self.get_font(25), "White", "Green")
        self.english_button = Button(self.usa_flag, (390, 275), "", self.get_font(25), "White", "Green")
        self.volumen_button = Button(self.volumen_icon, (640, 350), "", self.get_font(25), "White", "Green")
        self.beginner_button = Button(
            self.difficulty_image, (890, 275), localization.get_text("beginner"),
            self.get_font(25), "White", "Green", text_offset=(0, 0)
        )
        self.advanced_button = Button(
            self.difficulty_image, (890, 325), localization.get_text("advanced"),
            self.get_font(25), "White", "Green", text_offset=(0, 0)
        )
        
        self.update_texts()

    def get_font(self, size):
        return pygame.font.Font("assets/fonts/SCREEN.TTF", size)
    
    def update_texts(self):
        self.name = self.get_font(50).render(localization.get_text("settings"), True, (59, 170, 143))
        self.language = self.get_font(40).render(localization.get_text("language"), True, (78, 248, 71))
        self.sound = self.get_font(40).render(localization.get_text("music"), True, (78, 248, 71))
        self.difficulty_text = self.get_font(40).render(localization.get_text("difficulty"), True, (78, 248, 71))
        

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.beginner_button.checkForInput(pygame.mouse.get_pos()):
                    self.difficulty = "Beginner"
                    self.state_manager.set_difficulty(self.difficulty)
                    self.select_sound.play()
                if self.advanced_button.checkForInput(pygame.mouse.get_pos()):
                    self.difficulty = "Advanced"
                    print(self.difficulty)
                    self.select_sound.play()
                    self.state_manager.set_difficulty(self.difficulty)
                if self.volumen_button.checkForInput(pygame.mouse.get_pos()):
                    self.sound_on = not self.sound_on
                    if self.sound_on:
                        pygame.mixer.music.set_volume(1.0)
                        self.select_sound.set_volume(1.0)
                    else:
                        pygame.mixer.music.set_volume(0.0)
                        self.select_sound.set_volume(0.0)
                if self.back_button.checkForInput(pygame.mouse.get_pos()):
                    self.state_manager.set_state("main_menu")
                    self.select_sound.play()
                elif self.english_button.checkForInput(pygame.mouse.get_pos()):
                    localization.set_language("en")
                    self.update_texts()
                    self.select_sound.play()
                elif self.spanish_button.checkForInput(pygame.mouse.get_pos()):
                    localization.set_language("es")
                    self.update_texts()
                    self.select_sound.play()

        # Cambio de tamaño de los botones al pasar el mouse por encima
        mouse_pos = pygame.mouse.get_pos()
        self.back_button.changeImage(mouse_pos)
        self.spanish_button.changeImage(mouse_pos)
        self.english_button.changeImage(mouse_pos)
        self.volumen_button.changeImage(mouse_pos)
        self.beginner_button.changeImage(mouse_pos)
        self.advanced_button.changeImage(mouse_pos)

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
