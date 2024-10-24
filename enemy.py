import pygame
import random
from settings import TILE_SIZE # Importa las configuraciones necesarias
class Enemy:
    def __init__(self, x, y):
        # Inicializa las posiciones iniciales del jugador y la posicion que desea alcanzar
        self.x = x # Posicion actual del jugador en el eje x
        self.y = y # Posicion acutal edl jugador en el eje y
        self.target_x = self.x # Posicion objetivo en el eje x
        self.target_y = self.y # Posicion objetivo en el eje y
        self.speed = 2 # velocida de movimiento
        self.moving = False # Maraca para verificar si el jugador se esta moviento
        self.width = TILE_SIZE
        self.height = TILE_SIZE
        self.direction = random.choice(["UP", "DOWN", "LEFT", "RIGHT"])
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
        self.image = self.sprite
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
    
    #Movimiento random del enemigo
    def enemy_move_automatically(self, obstacles):
        if not self.moving:
            self.direction = random.choice(["UP", "DOWN", "LEFT", "RIGHT"])
            self.enemy_move(self.direction, obstacles)

    def enemy_move(self, direction, obstacles):
     #Esto de aqui mueve al jugador en la direccion especificadaa 
        if not self.moving: # Esto de aqui evita inicar un nuevo movimiento si ya esta en uno
            if direction == "UP":
                new_y = self.y - TILE_SIZE
                if not self.enemy_check_collision(self.x, new_y, obstacles): # Verifica colisiones
                    self.target_y = new_y
                    self.current_sprite = self.sprite_up
            elif direction == "DOWN":
                new_y = self.y + TILE_SIZE
                if not self.enemy_check_collision(self.x, new_y, obstacles): # Verifica colisiones
                    self.target_y = new_y
                    self.current_sprite = self.sprite_down
            elif direction == "LEFT":
                new_x = self.x - TILE_SIZE
                if not self.enemy_check_collision(new_x, self.y, obstacles): # Verifica colisiones
                    self.target_x = new_x
                    self.current_sprite = self.sprite_left
            elif direction == "RIGHT":
                new_x = self.x + TILE_SIZE
                if not self.enemy_check_collision(new_x, self.y, obstacles): # Verifica colisiones
                    self.target_x = new_x
                    self.current_sprite = self.sprite_right
            self.moving = True
    #COLISION DE ENEMIGOS
    def enemy_check_collision(self, new_x, new_y, obstacles): #player
        # COmprueba si la nueva colision que se registre choca con algun obstaculo
        enemy_rect = pygame.Rect(new_x, new_y, TILE_SIZE, TILE_SIZE)
        for obstacle in obstacles:
            if enemy_rect.colliderect(obstacle): #player
                return True
        return False 
    
    def enemy_update(self, obstacles):
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
            
        self.rect.topleft = (self.x, self.y)

    # Definimos un metodo para alinear la posicion del jugador a la cuadricula mas cercana
   
        if not self.moving:
         self.enemy_move_automatically(obstacles)  
    

    def enemy_draw(self, surface,):
        # Dibuja al jugasdor
        if self.sprite:
            surface.blit(self.sprite, (self.x, self.y))  # Dibuja el sprite si existe
        else:
            pygame.draw.rect(surface, (255, 0, 0), (self.x, self.y, TILE_SIZE, TILE_SIZE))


    