import pygame
import pygame.image
import sys
from settings import TILE_SIZE # Importa las configuraciones necesarias
from bubble import Bubble

# Clase Player para manejar al jugadorr
class Soap:
    def __init__(self, x, y):
        super().__init__()
        # Inicializa las propiedades del jugador
        self.x = x # Posicion actual del jugador en el eje x
        self.y = y # Posicion acutal edl jugador en el eje y
        self.target_x = self.x # Posicion objetivo en el eje x
        self.target_y = self.y # Posicion objetivo en el eje y
        self.speed = 2 # velocida de movimiento
        self.moving = False # Maraca para verificar si el jugador se esta moviento
        self.width = TILE_SIZE
        self.height = TILE_SIZE
        self.direction = "Down"
        # Cargar las imágenes (sprites)
        self.image = self.sprite_down  # sprite inicial 
        self.rect = self.image.get_rect(topleft=(self.x, self.y))


    def check_collision(self, new_x, new_y, obstacles):
        # COmprueba si la nueva colision que se registre choca con algun obstaculo
        player_rect = pygame.Rect(new_x, new_y, TILE_SIZE, TILE_SIZE)
        for obstacle in obstacles:
            if player_rect.colliderect(obstacle):
                return True
        return False
    
    def check_and_play_walk_sound(self):
        current_position = (self.x // TILE_SIZE, self.y // TILE_SIZE)

    def update(self):
        
        self.rect.topleft = (self.x, self.y)
    
      
    def snap_to_grid(self):
        if not self.moving:
            self.target_x = round(self.x / TILE_SIZE) * TILE_SIZE
            self.target_y = round(self.y / TILE_SIZE) * TILE_SIZE
            self.moving = True # Mueve el jugador a la casilla mas cercana

    def draw(self, surface):
        # Dibuja al jugasdor
        surface.blit(self.image, self.rect)
        self.draw_health_bar(surface)
    
    def draw_health_bar(self, surface):
        if self.health > 0:
            health_image = self.health_images[self.health - 1] # selecciona la imagen correspondiente a la vida
            surface.blit(health_image, (10, 10)) # Dibuja la barra de vida en las coordenadas
            
    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)


    def shoot(self, all_bubbles):
        current_time = pygame.time.get_ticks() # Con esto obtenemos el tiempo actual
        if current_time - self.last_shot_time >= self.shoot_cooldown: # Si ha pasado el cooldwon
            bubble = Bubble(self.rect.centerx, self.rect.centery, self.direction) # Craemos una instancia de la burbuja  en la posicion actual del jugador (el centro de su sprite)
            all_bubbles.add (bubble) # Añade la burbuja recien creada al grupo de burbujas para que se actualice y se dibuje en pantalla
            self.last_shot_time = current_time # Reiniciamos el contadorr