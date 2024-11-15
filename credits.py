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
            {"type": "text", "content": "Integrante 1 - Rol 1", "x": 50, "image_x": 800},
            {"type": "text", "content": "Integrante 2 - Rol 2", "x": 50, "image_x": 800},
            {"type": "text", "content": "Integrante 3 - Rol 3", "x": 50, "image_x": 800},
            {"type": "text", "content": "Integrante 4 - Rol 4", "x": 50, "image_x": 800},
            {"type": "text", "content": "Integrante 5 - Rol 5", "x": 50, "image_x": 800},
            {"type": "text", "content": "Integrante 6 - Rol 6", "x": 50, "image_x": 800},
        ]
        
        self.credits2 = [
            {"type": "text", "content": "Integrante 1 - Rol 1", "x": 800, "image_x": 50},
            {"type": "text", "content": "Integrante 2 - Rol 2", "x": 800, "image_x": 50},
            {"type": "text", "content": "Integrante 3 - Rol 3", "x": 800, "image_x": 50},
            {"type": "text", "content": "Integrante 4 - Rol 4", "x": 800, "image_x": 50},
            {"type": "text", "content": "Integrante 5 - Rol 5", "x": 800, "image_x": 50},
            {"type": "text", "content": "Integrante 6 - Rol 6", "x": 800, "image_x": 50},
        ]
        
        self.credits3 = [
            {"type": "text", "content": "Integrante 1 - Rol 1", "x": 50, "image_x": 800},
            {"type": "text", "content": "Integrante 2 - Rol 2", "x": 50, "image_x": 800},
            {"type": "text", "content": "Integrante 3 - Rol 3", "x": 50, "image_x": 800},
            {"type": "text", "content": "Integrante 4 - Rol 4", "x": 50, "image_x": 800},
            {"type": "text", "content": "Integrante 5 - Rol 5", "x": 50, "image_x": 800},
            {"type": "text", "content": "Integrante 6 - Rol 6", "x": 50, "image_x": 800},
        ]
   
        # Imágenes para cada lista de créditos
        self.image1 = pygame.image.load("c:\\Users\\Erick Ibarra\\OneDrive\\Imágenes\\Capturas de pantalla\\Captura de pantalla 2024-10-16 185653.png")
        self.image2 = pygame.image.load("c:\\Users\\Erick Ibarra\\OneDrive\\Imágenes\\Capturas de pantalla\\Captura de pantalla 2024-11-12 111425.png")
        self.image3 =pygame.image.load("c:\\Users\\Erick Ibarra\\OneDrive\\Imágenes\\Capturas de pantalla\\Captura de pantalla 2024-11-12 111442.png")
        # Variables de desplazamiento del texto
        self.scroll_y = 720  # Comienza fuera de la pantalla por abajo
        self.scroll_speed = 1  # Velocidad de desplazamiento


    def get_font(self, size):
        return pygame.font.Font("assets/fonts/GAME.TTF", size)
    
    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.back_button.checkForInput(pygame.mouse.get_pos()):
                    self.state_manager.set_state("main_menu", level=None, character_index=None)


         # Actualiza la posición de desplazamiento del texto
        self.scroll_y -= self.scroll_speed  # El texto se mueve hacia arriba
       
        # Reiniciar el desplazamiento al llegar al final
        total_height = self.scroll_y + (len(self.credits) + len(self.credits2) + len(self.credits3)) * 80
        if total_height < 0:
            self.scroll_y = 720  # Reinicia la posición para el bucle de créditos

        

    def draw(self, screen):
        # Dibujar los elementos en pantalla
        screen.blit(self.background, (0, 0))
        
        for i, element in enumerate(self.credits):
            y_position = self.scroll_y + i * 80
            # Texto
            text = self.font.render(element["content"], True, (0, 0, 0))
            screen.blit(text, (50, y_position))
    
            # Dibujar imagen al final de la primera lista de créditos
        screen.blit(self.image1, (800, self.scroll_y + (len(self.credits) - 1) * 80 - 350))

        # Dibujar segunda lista de créditos e imagen al lado izquierdo
        offset1 = len(self.credits) * 80  # Desplazamiento vertical adicional
        for i, element in enumerate(self.credits2):
            y_position = self.scroll_y + offset1 + i * 80
            
            # Texto
            text = self.font.render(element["content"], True, (0, 0, 0))
            screen.blit(text, (600, y_position))

             # Dibujar imagen al final de la segunda lista de créditos
        screen.blit(self.image2, (200, self.scroll_y + offset1 + (len(self.credits2) - 1) * 80 - 200))


        # Dibujar tercera lista de créditos con imagen al lado derecho
        offset2 = offset1 + len(self.credits2) * 80
        for i, element in enumerate(self.credits3):
            y_position = self.scroll_y + offset2 + i * 80
            # Texto
            text = self.font.render(element["content"], True, (0, 0, 0))
            screen.blit(text, (50, y_position))

          # Dibujar imagen al final de la tercera lista de créditos
        screen.blit(self.image3, (800, self.scroll_y + offset2 + (len(self.credits3) - 1) * 80 - 250))

        # Dibujar botón de regreso
        self.back_button.update(screen)
        
        
        
        # Actualizar la pantalla
        pygame.display.flip()
        