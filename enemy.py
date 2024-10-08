import pygame
from settings import TILE_SIZE # Importa las configuraciones necesarias

class Enemy:
    def __init__(self, x, y):
        # Inicializa las posiciones iniciales del jugador y la posicion que desea alcanzar
        self.x = x # Posicion actual del jugador en el eje x
        self.y = y # Posicion acutal edl jugador en el eje y
        self.target_x = self.x # Posicion objetivo en el eje x
        self.target_y = self.y # Posicion objetivo en el eje y
        self.speed = 4 # velocida de movimiento
        self.moving = False # Maraca para verificar si el jugador se esta moviento

        # Cargar las imágenes (sprites)
        self.sprite_up = None
        self.sprite_down = None
        self.sprite_left = None
        self.sprite_right = None
        self.current_sprite = None

    # Cargamos los sprites dle jugador
    def enemy_load_sprites(self):
        self.sprite = pygame.image.load("assets/sprites/enemy_2.png").convert_alpha()
        self.current_sprite = self.sprite # sprite inicial 

    def enemy_move(self, direction, obstacles):
        #Esto de aqui mueve al jugador en la direccion especificadaa 
        if not self.moving: # Esto de aqui evita inicar un nuevo movimiento si ya esta en uno
            if direction == "UP":
                new_y = self.target_y - TILE_SIZE
                if not self.enemy_check_collision(self.target_x, new_y, obstacles): # Verifica colisiones
                    self.target_y = new_y
                    self.current_sprite = self.sprite_up
            elif direction == "DOWN":
                new_y = self.target_y + TILE_SIZE
                if not self.enemy_check_collision(self.target_x, new_y, obstacles): # Verifica colisiones
                    self.target_y = new_y
                    self.current_sprite = self.sprite_down
            elif direction == "LEFT":
                new_x = self.target_x - TILE_SIZE
                if not self.enemy_check_collision(new_x, self.target_y, obstacles): # Verifica colisiones
                    self.target_x = new_x
                    self.current_sprite = self.sprite_left
            elif direction == "RIGHT":
                new_x = self.target_x + TILE_SIZE
                if not self.enemy_check_collision(new_x, self.target_y, obstacles): # Verifica colisiones
                    self.target_x = new_x
                    self.current_sprite = self.sprite_right
            self.moving = True
    
    def enemy_check_collision(self, new_x, new_y, obstacles):
        # COmprueba si la nueva colision que se registre choca con algun obstaculo
        enemy_rect = pygame.Rect(new_x, new_y, TILE_SIZE, TILE_SIZE)
        for obstacle in obstacles:
            if enemy_rect.colliderect(obstacle):
                return True
        return False

    def enemy_update(self):
        # Aqui se actualiza la posicion del jugador
        # Movimiento suave en el eje x
        if self.x < self.target_x:
            self.x += self.speed # Mueve hacia la derecha
            if self.x > self.target_x: # Corrige si sobrepasa la posicion objetivo
                self.x = self.target_x
        elif self.x > self.target_x:
            self.x -= self.speed # Mueve hacia la izquierda
            if self.x < self.target_x:
                self.x = self.target_x
        
        # Movimiento suave en el eje y
        if self.y < self.target_y:
            self.y += self.speed # Mueve hacia abajo
            if self.y > self.target_y:
                self.y = self.target_y
        elif self.y > self.target_y:
            self.y -= self.speed # Mueve hacia arriba
            if self.y < self.target_y:
                self.y = self.target_y
    
        # Verifica si el jugador ha llegado al objetivo osea la posicion exacta del cuadro
        if self.x == self.target_x and self.y == self.target_y:
            self.moving = False # Detiene el movimiento cuando llega a la posicion mas cercana
    
    # Definimos un metodo para alinear la posicion del jugador a la cuadricula mas cercana
    def enemy_snap_to_grid(self):
        if not self.moving:
            self.target_x = round(self.x / TILE_SIZE) * TILE_SIZE
            self.target_y = round(self.y / TILE_SIZE) * TILE_SIZE
            self.moving = True # Mueve el jugador a la casilla mas cercana

    def enemy_draw(self, surface):
        # Dibuja al jugasdor
        surface.blit(self.current_sprite, (self.x, self.y))


    