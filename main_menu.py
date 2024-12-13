import pygame 
import sys
from button import Button
from settings_menu import Button
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
class MainMenu:
    def __init__(self, state_manager):
        self.state_manager = state_manager
        self.screen = pygame.display.set_mode((1280, 720))
        self.clock = pygame.time.Clock()

        # Carga de recursos
        self.background = pygame.image.load("assets/sprites/Fondo.jpeg")
        self.play_image = pygame.image.load("assets/sprites/BOTON_VERDE2.png")
        self.quit_image = pygame.image.load("assets/sprites/BOTON_ROJO2.png")
        self.options_image = pygame.image.load("assets/sprites/BOTON_AJUSTES.png")
        self.credits_image = pygame.image.load("assets/sprites/boton_crditos1.png")
        self.tutorial_image = pygame.image.load("assets/sprites/boton_crditos1.png")
        self.controls_image = pygame.image.load("assets/sprites/controles.png")

        # Musica y sonidos
        self.select_sound = pygame.mixer.Sound("assets/sounds/select.mp3")
        self.main_music = pygame.mixer.music.load("assets/sounds/MENUMUSICA.mp3")
        pygame.mixer_music.play(-1)
     
        # Carga de imágenes de la animación del título
        self.title_frames = [
            pygame.transform.scale(pygame.image.load("assets/sprites/TITULOREDISEÑO1.png"), (900, 500)),
            pygame.transform.scale(pygame.image.load("assets/sprites/TITULOREDISEÑO2.png"), (900, 500)),
            pygame.transform.scale(pygame.image.load("assets/sprites/TITULOREDISEÑO3.png"), (900, 500)),
            pygame.transform.scale(pygame.image.load("assets/sprites/TITULOREDISEÑO4.png"), (900, 500)),
            pygame.transform.scale(pygame.image.load("assets/sprites/TITULOREDISEÑO5.png"), (900, 500)),
            pygame.transform.scale(pygame.image.load("assets/sprites/TITULOREDISEÑO6.png"), (900, 500)),
            pygame.transform.scale(pygame.image.load("assets/sprites/TITULOREDISEÑO7.png"), (900, 500))
        ]
        self.current_frame = 0
        self.animation_timer = 0
        self.animation_speed = 180

        # Escalar los recursos
        self.play_image = pygame.transform.scale(self.play_image, (200, 200))
        self.quit_image = pygame.transform.scale(self.quit_image, (170, 170))
        self.options_image = pygame.transform.scale(self.options_image, (170, 170))
        self.credits_image = pygame.transform.scale(self.credits_image, (200, 150))
        self.tutorial_image = pygame.transform.scale(self.tutorial_image, (200, 150))
        self.controls_image = pygame.transform.scale(self.controls_image, (100, 100))

        # Creacion de los botones
        self.play_button = Button(self.play_image, (640, 615), "", self.get_font(25), "Black", "Green")
        self.options_button = Button(self.options_image, (440, 615), "", self.get_font(25), "Black", "Green")
        self.quit_button = Button(self.quit_image, (840, 615), "", self.get_font(25), "Black", "Green")
        self.credits_button = Button(self.credits_image, (1180, 680), "Credits", self.get_font(20), "Black", "Green")
        self.tutorial_button = Button(self.tutorial_image, (120, 680), "Tutorial", self.get_font(20), "Black", "Green")
        self.controls_button = Button(self.controls_image, (1220, 40), "", self.get_font(20), "Black", "Green")
        
        self.credits_button = Button(
            self.credits_image, (1180, 680), localization.get_text("credits"),
            self.get_font(20), "Black", "Green", text_offset=(0, 0)
        )

    def get_font(self, size):
        return pygame.font.Font("assets/fonts/GAME.TTF", size)

    def update_animation(self, dt):
        self.animation_timer += dt
        if self.animation_timer >= self.animation_speed:
            self.animation_timer = 0
            self.current_frame = (self.current_frame + 1) % len(self.title_frames)

    def update(self):
        dt = self.clock.tick(60)
        self.update_animation(dt)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.play_button.checkForInput(pygame.mouse.get_pos()):
                    self.state_manager.set_state("player_selector")
                    self.select_sound.play()
                if self.tutorial_button.checkForInput(pygame.mouse.get_pos()):
                    self.state_manager.set_state("Tutorial")
                    self.select_sound.play()
                if self.quit_button.checkForInput(pygame.mouse.get_pos()):
                    pygame.quit()
                    sys.exit()
                if self.options_button.checkForInput(pygame.mouse.get_pos()):
                    self.state_manager.set_state("settings")
                    self.select_sound.play()
                if self.credits_button.checkForInput(pygame.mouse.get_pos()):
                    pygame.mixer.music.pause()
                    self.state_manager.set_state("credits")
                    self.select_sound.play()
                if self.controls_button.checkForInput(pygame.mouse.get_pos()):
                    pygame.mixer.music.pause()
                    self.state_manager.set_state("controls_zzz")
                    self.select_sound.play()

        # Cambio de tamaño de los botones al pasar el mouse por encima
        mouse_pos = pygame.mouse.get_pos()
        self.play_button.changeImage(mouse_pos)
        self.options_button.changeImage(mouse_pos)
        self.quit_button.changeImage(mouse_pos)
        self.credits_button.changeImage(mouse_pos)
        self.tutorial_button.changeImage(mouse_pos)
        self.controls_button.changeImage(mouse_pos)

    def draw(self, screen):
        screen.blit(self.background, (0, 0))
        # Dibujar el frame actual de la animación del título
        title_image = self.title_frames[self.current_frame]
        title_rect = title_image.get_rect(center=(640, 280))
        self.screen.blit(title_image, title_rect)
        self.play_button.update(screen)
        self.options_button.update(screen)
        self.quit_button.update(screen)
        self.credits_button.update(screen)
        self.tutorial_button.update(screen)
        self.controls_button.update(screen)
        pygame.display.flip()
