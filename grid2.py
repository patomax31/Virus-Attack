import pygame
import sys

# ayudaAAAAAAAS

# Configuraciones basicas
SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720  # Dimensiones de la ventana del juego
TILE_SIZE = 32  # Tamaño de cada cuadro en la cuadrícula del juego
player_pos = [4, 9]  # Posición inicial del jugador en la cuadrícula (x, y)
move_cooldown = 200 # Tiempo que se tarda en hacer un movimiento en milisegundoss
bg = pygame.image.load("background1.png") # Cargamos la imagen del fondo para el nivel 1 en una variable almacenada
# Almacenamos en variables los valores de los colores para no tener que repetir tantas veces los numeros
white = 255, 255, 255
black = 0, 0, 0
red = 255, 0, 0

# Inicializacion de Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # Crea la ventana del juego con el tamaño especificado
clock = pygame.time.Clock()  # Reloj para controlar la tasa de actualización del juego
last_move_time = 0 # Controla el tiempo del ultimo movimiento

# Cargamos los sprites en variables y almacenamos los archivos
sprite_up = pygame.image.load("assets/sprites/medicUp.png").convert_alpha()
sprite_down = pygame.image.load("assets/sprites/medicDown.png").convert_alpha()
sprite_left = pygame.image.load("assets/sprites/medicLeft.png").convert_alpha()
sprite_right = pygame.image.load("assets/sprites/medicRight.png").convert_alpha()

# Inicializacion de las variables que controlan las direcciones del movimiento
move_up = move_down = move_left = move_right = False
current_sprite = sprite_down # Controlamos el sprite inicial que se supone debe estar mirando hacia abajo

# Funcion para mover al jugador según la dirección dada
def move_player():
    global last_move_time, current_sprite
    current_time = pygame.time.get_ticks()  # Tiempo actual en milisegundos
    # Aqui se determina si ha pasado suficiente tiempó desde el ultimo movimiento
    if current_time - last_move_time > move_cooldown:
        # determina la direccion en que se mueve el jugador
        if move_up:
            player_pos[1] -= 1
            current_sprite = sprite_up # Cambia el sprite
            last_move_time = current_time
        if move_down:
            player_pos[1] += 1
            current_sprite = sprite_down # Cambia el sprite
            last_move_time = current_time
        if move_left:
            player_pos[0] -= 1
            current_sprite = sprite_left # Cambia el sprite
            last_move_time = current_time
        if move_right:
            player_pos[0] += 1
            current_sprite = sprite_right # Cambia el sprite
            last_move_time = current_time

# Bucle principal del juego
running = True
while running:
    for event in pygame.event.get():  # Revisa todos los eventos que ocurren en Pygame
        if event.type == pygame.QUIT:  # Si se cierra la ventana esto detiene el bucle
            running = False
        elif event.type == pygame.KEYDOWN:  # Detecta si se presiona una tecla
            # Aqui se asignan los controles de movimiento con las teclas WASD y el estado de la tecla
            if event.key == pygame.K_w:      # Tecla W para moverse hacia arriba
                move_up = True
            elif event.key == pygame.K_s:    # Tecla S para moverse hacia abajo
                move_down = True
            elif event.key == pygame.K_a:    # Tecla A para moverse hacia la izquierda
                move_left = True
            elif event.key == pygame.K_d:    # Tecla D para moverse hacia la derecha
                move_right = True
        
        elif event.type == pygame.KEYUP:  # Detecta si se deja de presionar una tecla
            # Aqui se asignan los controles de movimiento con las teclas WASD y el estado de la tecla
            if event.key == pygame.K_w:      # Tecla W para moverse hacia arriba
                move_up = False
            elif event.key == pygame.K_s:    # Tecla S para moverse hacia abajo
                move_down = False
            elif event.key == pygame.K_a:    # Tecla A para moverse hacia la izquierda
                move_left = False
            elif event.key == pygame.K_d:    # Tecla D para moverse hacia la derecha
                move_right = False

    # Llamamos a la funcion que mueve al jugador segun la tecla que se presione
    move_player()

    # Renderizado de la pantalla y jugador
    screen.fill(white)  # Limpia la pantalla llenandola de color blanco
    screen.blit(bg, (0, 0))  # Sobrepone sobre el fondo blanco la imagen del fondo
    # Dibuja al jugador como un rectángulo rojo en la posición actual multiplicada por el tamaño de los cuadros
    screen.blit(current_sprite, (player_pos[0] * TILE_SIZE, player_pos[1] * TILE_SIZE, TILE_SIZE, TILE_SIZE))
    pygame.display.flip()  # Actualiza la pantalla para mostrar los cambios
    clock.tick(60)  # Mantiene el juego corriendo a 60 fotogramas por segundo (FPS)

pygame.quit()  # Cierra Pygame de manera segura cuando el bucle principal termina
sys.exit()  #Controla que el videojuego se cierre de manera correcta 