import pygame
from settings import SCREEN_HEIGHT, SCREEN_WIDTH

#Creamos la clase para las burbujas 
class Bubble(pygame.sprite.Sprite): 
    def __init__(self, x, y , direction): 
        super().__init__() # Con esto llamamos al constructor de la clase base "pygame.sprite.Sprite"
        self.image = pygame.image.load("assets/sprites/bubble1.png").convert_alpha() # Cargamos la imagen
        self.rect = self .image.get_rect() # Con esto obtenemos el rectangulo que envuelve a la burbuja (para proximamente la colision y ademas su posicion)
        self.rect.center = (x, y) # Posicionas la burbuja en las cordenadas (x, y) que son la posicion inicial del disparo y ademas la posicion del personaje
        self.speed = 10 # Velocidad de la burbuja
        self.direction = direction # Con esto almacenamos la direccion en la que se movera la burbuja

    def update(self):
        # Movemos la burbuja segun su direccion
        if self.direction == "UP": # Si la direccion de lanzamiento es hacia arriba reducimos el valor de Y para mover la burbuja hacia arriba
            self.rect.y -= self.speed
        elif self.direction == "DOWN": # Si la direccion de lanzamiento es hacia abajo aumentamos el valor de Y para mover la burbuja hacia abajo
            self.rect.y += self.speed
        elif self.direction == "LEFT": # Si la direccion de lanzamiento es hacia la izquierda reducimos el valor de X para mover la burbuja hacia la izquierda
            self.rect.x -= self.speed
        elif self.direction == "RIGHT": # Si la direccion de lanzamiento es hacia la derecha aumentamos el valor de X para mover la burbuja hacia la derecha
            self.rect.x += self.speed
        
        # Elimina la burbuja si sale de la pantalla
        if self.rect.bottom < 0 or self.rect.top > SCREEN_HEIGHT or self.rect.right < 0 or self.rect.left > SCREEN_WIDTH:
            self.kill() #mango
            