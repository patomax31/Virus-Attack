import sys
import pygame
from player import Player # Importamos la clase Player
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, TILE_SIZE # Importamos configuraciones
from bubble import Bubble
from contador import tiempo
from pauseButton import PauseButton

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
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
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
paused = False # Estado del juego (si esta pausado o no)
pause_button = PauseButton() # Almacenamos la instancia del boton de pausa
keys_pressed = None # Creamos esta variable que almacena las teclas precionadas en ella
start_time = pygame.time.get_ticks() # Marca el tiempo al inicios

while running:
    # Calculamos el tiempo transcurrido
    if not paused:
        elapsed_time = (pygame.time.get_ticks() - start_time) // 1000  # Hacemos la conversión a segundos
    else:
        start_time = pygame.time.get_ticks() - (elapsed_time * 1000)  # Ajustamos el tiempo cuando se reanuda
    time_left = max(0, 100 - elapsed_time)  # Tiempo restante en segundos

    for event in pygame.event.get():  # Revisa todos los eventos que ocurren en Pygame
        if event.type == pygame.QUIT or time_left == 0:  # Si se cierra la ventana esto detiene el bucle
            running = False  # Detiene la ejecución del juego

        if event.type == pygame.MOUSEBUTTONDOWN:
            if pause_button.is_clicked(event.pos):
                paused = not paused  # Si le damos click al botón se cambia el estado de la pausa

        current_direction = "DOWN" # Direccion por default 

        if not paused:
            # Detectamos cuando se presiona la barra espaciadora para disparar
            if event.type == pygame.KEYDOWN:  # Detecta si se presiona una tecla
                if event.key == pygame.K_w:
                    current_direction = "UP"  # Cambia la dirección cuando se presiona la tecla W
                elif event.key == pygame.K_s:
                    current_direction = "DOWN"  # Cambia la dirección cuando se presiona la tecla S
                elif event.key == pygame.K_a:
                    current_direction = "LEFT"  # Cambia la dirección cuando se presiona la tecla A
                elif event.key == pygame.K_d:
                    current_direction = "RIGHT"  # Cambia la dirección cuando se presiona la tecla D

                if event.key == pygame.K_j:  # Verifica si la tecla presionada es J
                    player.shoot(all_bubbles)  # Llamamos a la función shoot del archivo player y agregamos burbujas al grupo

                if event.key == pygame.K_ESCAPE:
                    paused = not paused  # Cambiamos el estado de la pausa si presionamos escape

                if event.key == pygame.K_z:
                    player.change_health()  # Cambiamos la vida del jugador si presionamos Z
        
    if not paused:
        # Manejo de eventos
        keys = pygame.key.get_pressed()  # Detecta si las teclas están presionadas
        if keys[pygame.K_w]:
            player.move('UP', obstacles)
        elif keys[pygame.K_s]:
            player.move('DOWN', obstacles)
        elif keys[pygame.K_a]:
            player.move('LEFT', obstacles)
        elif keys[pygame.K_d]:
            player.move('RIGHT', obstacles)
        else:
            player.snap_to_grid()  # Llamamos a la función snap_to_grid del archivo player para alinear al jugador hacia la casilla más cercana

    

        player.update() # ACtualizamos el estado del jugador
        all_bubbles.update() # Actualizamos el estado de todas las burbujas

    BG = pygame.image.load("background1.png") # Cargamos la imagen del fondo para el nivel 1 en una variable almacenada



    # Renederizamos la pantalla
    screen.blit(BG, (0, 0)) # Sobreponemos el fondo sobre el fondo blanco
    player.draw(screen) # Renderizamos al jugador
    all_bubbles.draw(screen) # Renderizamos a las burbujas del gruppo
    player.draw_health_bar(screen) # Renderizamos la barra de vida del jugador
    tiempo.draw_timer(screen, time_left) # Renderizamos el temporizadorr
    pause_button.draw(screen) # Renderizamos el btoin de pausea
    pygame.display.flip() # Esta madre actualiza la pantalla con nuevos graficoss

    if paused:  # si el estado de paused es verdadero
        # Dibujamos una pantalla semitransparente de mientras
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        overlay.fill((0, 0, 0))  # pintamos color negro a la roña
        overlay.set_alpha(128)  # Le ponemos transparencia (la transparencia se mide del 0 al 255 donde el 0 es completamente transparente)
        screen.blit(overlay, (0, 0))

        # Dibujamos el botón de pausa mientras el juego está en pausa
        pause_button.draw(screen)
        pygame.display.flip()  # actualizamos la pantalla
        while paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    paused = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pause_button.is_clicked(event.pos):
                        paused = not paused
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        paused = not paused
            clock.tick(FPS)
        continue  # saltamos el resto del bucle para que nada más se mueva

    # Controlamos los FPS
    clock.tick(FPS)
     
# Finalizamos pygame chido
pygame.quit() # Cierra pygame de manera segura y finaliza el bucle
sys.exit() # Controla que el videojuego se cierre de manera correcta
#Tiren paro