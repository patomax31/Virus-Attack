import pygame
import pygame.image
import sys
from settings import TILE_SIZE # Importa las configuraciones necesarias
from bubble import Bubble

# Clase Player para manejar al jugadorr
class Player:
    def __init__(self, x, y, character_index):
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
        self.direction = "DOWN"
        self.shoot_cooldown = 800 # Cooldonn wn milisegundoss
        self.last_shot_time = pygame.time.get_ticks() # Registra el ultimo tiempo de disparo
        self.health = 3 # Vida del jugador
        self.last_position = (self.x // TILE_SIZE, self.y // TILE_SIZE) # Posicion anterior del jugador
        self.is_dead = False
        
        self.walk_sound = pygame.mixer.Sound("assets/sounds/walk.mp3") # Carga el sonido de caminar
        
        self.character_index = character_index
        print(f"Character index: {character_index}")
        
        self.load_health_sprites()
        self.load_sprites(character_index)

        # Cargar las imágenes (sprites)
        self.image = self.sprite_down  # sprite inicial 
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

    # Cargamos los sprites dle jugador
    def load_sprites(self, character_index):
        print(f"Loading sprites for character index: {character_index}")
        if character_index == 0:
            self.sprite_up = pygame.image.load("assets/sprites/medicUp.png").convert_alpha()
            self.sprite_down = pygame.image.load("assets/sprites/medicDown.png").convert_alpha()
            self.sprite_left = pygame.image.load("assets/sprites/medicLeft.png").convert_alpha()
            self.sprite_right = pygame.image.load("assets/sprites/medicRight.png").convert_alpha()
        elif character_index == 1:
            self.sprite_up = pygame.image.load("assets\sprites\DOCTORACASTAÑAATRAS.png").convert_alpha()
            self.sprite_down = pygame.image.load("assets/sprites/DOCTORACASTAÑAFRENTE.png").convert_alpha()
            self.sprite_left = pygame.image.load("assets/sprites/DOCTORACASTAÑAIZQUIERDA.png").convert_alpha()
            self.sprite_right = pygame.image.load("assets/sprites/DOCTORACASTAÑADERECHA.png").convert_alpha()
        elif character_index == 2:
            self.sprite_up = pygame.image.load("assets\sprites\MEDICORUBIOATRAS.png").convert_alpha()
            self.sprite_down = pygame.image.load("assets/sprites/MEDICORUBIOFRENTE.png").convert_alpha()
            self.sprite_left = pygame.image.load("assets/sprites/MEDICORUBIOIZUQIERDA.png").convert_alpha()
            self.sprite_right = pygame.image.load("assets/sprites/MEDICORUBIODERECHA.png").convert_alpha()
        elif character_index == 3:
            self.sprite_up = pygame.image.load("assets\sprites\DOCTORAVISTAATRAS.png").convert_alpha()
            self.sprite_down = pygame.image.load("assets/sprites/DOCTORAVISTAFRENTE.png").convert_alpha()
            self.sprite_left = pygame.image.load("assets\sprites\DOCTORAIZQUIERDA.png").convert_alpha()
            self.sprite_right = pygame.image.load("assets/sprites/DOCTORADERECHA.png").convert_alpha()
        else:
            raise ValueError("Invalid character index: {character_index}")

        # Establecemos el sprite actual y el rectángulo de colisión
        self.image = self.sprite_down  # sprite inicial
        print(f"Successfully loaded sprites for character {character_index}") 
        self.sprite_up = pygame.transform.scale(self.sprite_up, (int(self.sprite_up.get_width() * 0.5), int(self.sprite_up.get_height() * 0.5)))
        self.sprite_down = pygame.transform.scale(self.sprite_down, (int(self.sprite_down.get_width() * 0.5), int(self.sprite_down.get_height() * 0.5)))
        self.sprite_left = pygame.transform.scale(self.sprite_left, (int(self.sprite_left.get_width() * 0.5), int(self.sprite_left.get_height() * 0.5)))
        self.sprite_right = pygame.transform.scale(self.sprite_right, (int(self.sprite_right.get_width() * 0.5), int(self.sprite_right.get_height() * 0.5)))

    def load_health_sprites(self):
        self.health_images = [
            pygame.image.load("assets/sprites/health_3.png").convert_alpha(),
            pygame.image.load("assets/sprites/health_2.png").convert_alpha(),
            pygame.image.load("assets/sprites/health_1.png").convert_alpha()
        ]

    def change_health(self, amount): # Metodo para cambiar la vida del jugador
        self.health += amount
        self.health = max(0, min(self.health, 3))
        self.update_health_sprite()
        if self.health < 1:
            self.is_dead = True

    def update_health_sprite(self): # Metodo para actualizar la imagen de la vida
        self.health_sprite = self.health_images[self.health - 1] # Selecciona la imagen correspondiente a la vida

    def move(self, direction, obstacles):
        # Esto mueve al jugador en la dirección especificada
        if not self.moving:  # Solo se mueve si no está ya en movimiento
            if direction == "UP":
                new_y = self.target_y - TILE_SIZE
                if not self.check_collision(self.target_x, new_y, obstacles):  # Verifica colisiones
                    self.target_y = new_y
                    self.image = self.sprite_up
                    self.direction = "UP"  # Actualiza la dirección
                    self.check_and_play_walk_sound()
            elif direction == "DOWN":
                new_y = self.target_y + TILE_SIZE
                if not self.check_collision(self.target_x, new_y, obstacles):  # Verifica colisiones
                    self.target_y = new_y
                    self.image = self.sprite_down
                    self.direction = "DOWN"
                    self.check_and_play_walk_sound()
            elif direction == "LEFT":
                new_x = self.target_x - TILE_SIZE
                if not self.check_collision(new_x, self.target_y, obstacles):  # Verifica colisiones
                    self.target_x = new_x
                    self.image = self.sprite_left
                    self.direction = "LEFT"
                    self.check_and_play_walk_sound()
            elif direction == "RIGHT":
                new_x = self.target_x + TILE_SIZE
                if not self.check_collision(new_x, self.target_y, obstacles):  # Verifica colisiones
                    self.target_x = new_x
                    self.image = self.sprite_right
                    self.direction = "RIGHT"
                    self.check_and_play_walk_sound()
            self.moving = True

    
    def check_collision(self, new_x, new_y, obstacles):
        # COmprueba si la nueva colision que se registre choca con algun obstaculo
        player_rect = pygame.Rect(new_x, new_y, TILE_SIZE, TILE_SIZE)
        for obstacle in obstacles:
            if player_rect.colliderect(obstacle):
                return True
        return False
    
    def check_and_play_walk_sound(self):
        current_position = (self.x // TILE_SIZE, self.y // TILE_SIZE)
        if current_position != self.last_position:
            self.walk_sound.play()
            self.last_position = current_position

    def update(self):
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

        # Actualizamos el rectángulo del jugador a la nueva posición
        self.rect.topleft = (self.x, self.y)
    
        # Verifica si el jugador ha llegado al objetivo osea la posicion exacta del cuadro
        if self.x == self.target_x and self.y == self.target_y:
            self.moving = False # Detiene el movimiento cuando llega a la posicion mas cercana
    
    # Definimos un metodo para alinear la posicion del jugador a la cuadricula mas cercana
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


    def shoot(self, all_bubbles, difficulty):
        current_time = pygame.time.get_ticks() # Con esto obtenemos el tiempo actual
        if current_time - self.last_shot_time >= self.shoot_cooldown: # Si ha pasado el cooldwon
            bubble = Bubble(self.rect.centerx, self.rect.centery, self.direction, difficulty) # Craemos una instancia de la burbuja  en la posicion actual del jugador (el centro de su sprite)
            all_bubbles.add (bubble) # Añade la burbuja recien creada al grupo de burbujas para que se actualice y se dibuje en pantalla
            self.last_shot_time = current_time # Reiniciamos el contadorr