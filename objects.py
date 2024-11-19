import pygame
import pygame.image
import sys
from settings import TILE_SIZE # Importa las configuraciones necesarias
from player import Player
# Clase Player para manejar al jugadorr
class soap(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        # Inicializa las propiedades del jugador
        self.x = x # Posicion actual del jugador en el eje x
        self.y = y # Posicion acutal edl jugador en el eje y
        self.target_x = self.x 
        self.target_y = self.y
        self.width = TILE_SIZE
        self.height = TILE_SIZE
        # Cargar las imágenes (sprites)
        borrar = (0, 0, 0, 0)
        soap_collected = False

        self.load_sprites()
        
        self.image = self.sprite_soap
        self.rect = self.image.get_rect(center=(self.x, self.y))

    def load_sprites(self):
        self.sprite_soap= pygame.image.load("assets/sprites/soap.png").convert_alpha()
        self.sprite_soap = pygame.transform.scale(self.sprite_soap, (int(self.sprite_soap.get_width() * 0.1), int(self.sprite_soap.get_height() * 0.1)))

    def check_object_collision(self, obstacles, Player_rect):
        # COmprueba si la nueva colision que se registre choca con algun obstaculo
        soap_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        for obstacle in obstacles:
            if soap_rect.colliderect(Player_rect):  
                soap.kill(self)
                print("hola")
                return True            
        return False
    
    def update(self):
        pass

    def draw(self, surface):
        surface.blit(self.image, self.rect)
        
    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)
