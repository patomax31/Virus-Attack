import pygame
import sys
from player import Player # Importamos la clase Player
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, WHITE, TILE_SIZE # Importamos configuraciones
from bubble import Bubble
from contador import tiempo
import time

# Inicializamos pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # Creamos la ventana con sus medidas
clock = pygame.time.Clock() # Creamos est amadre que es para controlar los FPS

# Creamos el mapa de obstáculos (1 = obstáculo, 0 = espacio libre)
map_data = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1], 
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

# Convertimos el mapa en una lista de rectángulos que representan las colisiones
obstacles = [] # Esta es la lista donde almacenamoslos obstaculos del mapa
for row_idx, row in enumerate(map_data): # Recorre cada fila del mapa y la indexa
    for col_idx, cell in enumerate(row): # Recorre cada columna de la fila
        if cell == 1: # Si la celda es igual a 1 (osea un obstaculo) crae un rectangulo
            obstacle_rect = pygame.Rect(col_idx * TILE_SIZE, row_idx * TILE_SIZE, TILE_SIZE, TILE_SIZE) # Crea el rectangulo para el obstaculo
            obstacles.append(obstacle_rect) # Con esto añadimos el rectangulo a la lista

# Creamos la instancia del jugador
player = Player(400, 400) # Posicion inicial del jugador en la cuadricula
player.load_sprites() # Cargamos los sprites despues de inicializar la pantalla

# Inicializamos el grupo de burbujas
all_bubbles = pygame.sprite.Group()

# Bucle principal del juego
running = True # Creamos esta variable que controla is el juego esta corriendo
keys_pressed = None # Creamos esta variable que almacena las teclas precionadas en ella
movement_cooldown = 0 # Temporizador para que el jugador no se mueva demasiado rapido

start_time = pygame.time.get_ticks() # Marca el tiempo al inicios

while running:
    # Calculamos el tiempo transcurrido
    elapsed_time = (pygame.time.get_ticks() - start_time) // 1000 # Hacemos la conversiona segundos
    time_left = max(0, 10 - elapsed_time) # Tiempo restante en segundoss
    for event in pygame.event.get(): # Revisa todos los enventos que ocurren en Pygame
        if event.type == pygame.QUIT or time_left == 0: # Si se cierra la venta esto detiene el bucle
            running = False # Detiene la ejecucion del juego

        current_direction = "DOWN" # Direccion por default 

        # Detectamos cuando se presiona la barra espaciadora para disparar
        if event.type == pygame.KEYDOWN: # Detecta si se presiona una tecla
            if event.key == pygame.K_w:
                current_direction = "UP" # Cambia la direccion cuando se presiona la telca W
            elif event.key == pygame.K_s:
                current_direction = "DOWN" # Cambia la direccion cuando se presiona la tecla S
            elif event.key == pygame.K_s:
                current_direction = "LEFT" # Cambia la didreccion cuando se presiona la tecla S
            elif event.key == pygame.K_s:
                current_direction = "RIGHT" # Cambia la direccion cuando se presiona la tecla S

            if event.key == pygame.K_j: # Verifica si la telca presionada es el espacio
                player.shoot(all_bubbles) # Llamamos a la funcion shoot del archivo player y agregamos burbujas al grupo
        
    # Manejo de eventos
    keys = pygame.key.get_pressed() # Detecta si las teclas estan presionadas
    if movement_cooldown == 0:  # Solo permite el movimiento cuando cooldown es 0
        if keys[pygame.K_w]:
            player.move('UP', obstacles)
            movement_cooldown = 0  # Pequeño retraso entre movimientos
        elif keys[pygame.K_s]:
            player.move('DOWN', obstacles)
            movement_cooldown = 0
        elif keys[pygame.K_a]:
            player.move('LEFT', obstacles)
            movement_cooldown = 0
        elif keys[pygame.K_d]:
            player.move('RIGHT', obstacles)
            movement_cooldown = 0
        # Con esto validamos que si no se esta presionando alguna tecla nosotros vamos a ejecutar el metodo snap_to_grid
        elif not (keys[pygame.K_w] or keys[pygame.K_s] or keys[pygame.K_a] or keys[pygame.K_d]):
            player.snap_to_grid() # LLamamos a la funcion snap_to_grid del archivo player para alinear al jugador hacia la casilla de mas cercana

    player.update() # ACtualizamos el estado del jugador
    all_bubbles.update() # Actualizamos el estado de todas las burbujas

    BG = pygame.image.load("background1.png") # Cargamos la imagen del fondo para el nivel 1 en una variable almacenada



    # Renederizamos la pantalla
    screen.fill(WHITE) # Limpia la pantalla llenandola de color blanco
    screen.blit(BG, (0, 0)) # Sobreponemos el fondo sobre el fondo blanco
    player.draw(screen) # Renderizamos al jugador
    all_bubbles.draw(screen) # Renderizamos a las burbujas del gruppo
    player.draw_health_bar(screen) # Renderizamos la barra de vida del jugador
    tiempo.draw_timer(screen, time_left)
    pygame.display.flip() # Esta madre actualiza la pantalla con nuevos graficoss

    #Disminuye el cooldown
    if movement_cooldown > 0: # Si el cooldown es mayor que 0:
        movement_cooldown -= 1 # Se disminuye el cooldown en 1

    # Controlamos los FPS
    clock.tick(FPS)

    

# Finalizamos pygame chido
pygame.quit() # Cierra pygame de manera segura y finaliza el bucle
sys.exit() # Controla que el videojuego se cierre de manera correcta
#Tiren paro