import pygame
import sys
from player import Player # Importamos la clase Player
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, WHITE, TILE_SIZE # Importamos configuraciones

# Inicializamos pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

# Creamos la instancia del jugador
player = Player(0, 0) # Posicion inicial del jugador en la cuadricula
player.load_sprites() # Cargamos los sprites despues de inicializar la pantalla

# Bucle principal del juego
running = True
keys_pressed = None
movement_cooldown = 0 # Temporizador para que el jugador no se mueva demasiado rapido

while running:
    for event in pygame.event.get(): # Revisa todos los enventos que ocurren en Pygame
        if event.type == pygame.QUIT: # Si se cierra la venta esto detiene el bucle
            running = False
        
    # Manejo de eventos
    keys = pygame.key.get_pressed() # Detecta si las teclas estan presionadas
    if movement_cooldown == 0:  # Solo permite el movimiento cuando cooldown es 0
        if keys[pygame.K_w]:
            player.move('UP')
            movement_cooldown = 0  # Pequeño retraso entre movimientos
        elif keys[pygame.K_s]:
            player.move('DOWN')
            movement_cooldown = 0
        elif keys[pygame.K_a]:
            player.move('LEFT')
            movement_cooldown = 0
        elif keys[pygame.K_d]:
            player.move('RIGHT')
            movement_cooldown = 0
        # Con esto validamos que si no se esta presionando alguna tecla nosotros vamos a ejecutar el metodo snap_to_grid
        elif not (keys[pygame.K_w] or keys[pygame.K_s] or keys[pygame.K_a] or keys[pygame.K_d]):
            player.snap_to_grid() # Alinea al jugador hacia la casilla de mas cercana

    
    # Actualizamos el jugador
    player.update()

    BG = pygame.image.load("background1.png") # Cargamos la imagen del fondo para el nivel 1 en una variable almacenada

    # Renederizamos la pantalla
    screen.fill(WHITE) # Limpia la pantalla llenandola de color blanco
    screen.blit(BG, (0, 0)) # Sobreponemos el fondo sobre el fondo blanco
    player.draw(screen) # Renderizamos al jugador
    pygame.display.flip()

    #Disminuye el cooldown
    if movement_cooldown > 0:
        movement_cooldown -= 1

    # Controlamos los FPS
    clock.tick(FPS)

# Finalizamos pygame chido
pygame.quit() # Cierra pygame de manera segura y finaliza el bucle
sys.exit() # Controla que el videojuego se cierre de manera correcta