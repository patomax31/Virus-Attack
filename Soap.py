import pygame
import pygame.image
import sys
from settings import TILE_SIZE # Importa las configuraciones necesarias
from player import Player
# Clase Player para manejar al jugadorr
class soap:
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
        self.image = self.rect 
        self.rect = self.get_rect(topleft=(self.x, self.y))

    def load_sprites(self):
        self.sprite_soap= pygame.image.load("assets/sprites/soap.png").convert_alpha()

    def check_collision(self, obstacles,Player_rect):
        # COmprueba si la nueva colision que se registre choca con algun obstaculo
        soap_rect = pygame.Rect(TILE_SIZE, TILE_SIZE)
        for obstacle in obstacles:
            if soap_rect.colliderect(Player_rect):
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
    
    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)
