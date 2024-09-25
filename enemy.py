import pygame

class Enemy:
    def __init__(self, x, y):
        # Inicializa las posiciones iniciales del jugador y la posicion que desea alcanzar
        self.x = x # Posicion actual del jugador en el eje x
        self.y = y # Posicion acutal edl jugador en el eje y
        self.enemy_load_sprites()

    # Cargamos los sprites dle jugador
    def enemy_load_sprites(self):
        self.current_sprite = pygame.image.load("assets/sprites/enemy_3.png").convert_alpha()
        self.rect = self.current_sprite.get_rect(center=(self.x, self.y))

    def enemy_draw(self, surface):
        surface.blit(self.current_sprite, self.rect)
    
    def enemy_update(self):
        # Aquí se puede agregar la lógica para actualizar la posición o el estado del enemigo
        pass