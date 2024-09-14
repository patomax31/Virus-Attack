import pygame
import sys

# Configuraciones basicas
SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720  # Dimensiones de la ventana del juego
TILE_SIZE = 30  # Tamaño de cada cuadro en la cuadrícula del juego
player_pos = [5, 5]  # Posición inicial del jugador en la cuadrícula (x, y)
move_cooldown = 200 # Tiempo que se tarda en hacer un movimiento en milisegundoss
bg = pygame.image.load("background1.png")

# Inicializacion de Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # Crea la ventana del juego con el tamaño especificado
clock = pygame.time.Clock()  # Reloj para controlar la tasa de actualización del juego
last_move_time = 0 # Controla el tiempo del ultimo movimiento

# Inicializacion de las variables que controlan las direcciones del movimiento
move_up = move_down = move_left = move_right = False

# Funcion para mover al jugador según la dirección dada
def move_player():
    global last_move_time
    current_time = pygame.time.get_ticks()  # Tiempo actual en milisegundos
    # Aqui se determina si ha pasado suficiente tiempó desde el ultimo movimiento
    if current_time - last_move_time > move_cooldown:
        # determina la direccion en que se mueve el jugador
        if move_up:
            player_pos[1] -= 1
            last_move_time = current_time
        if move_down:
            player_pos[1] += 1
            last_move_time = current_time
        if move_left:
            player_pos[0] -= 1
            last_move_time = current_time
        if move_right:
            player_pos[0] += 1
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
    screen.fill((255, 255, 255))  # Limpia la pantalla llenandola de color blanco
    screen.blit(bg, (0, 0))  # Sobrepone sobre el fondo blanco la imagen del fondo
    # Dibuja al jugador como un rectángulo rojo en la posición actual multiplicada por el tamaño de los cuadros
    pygame.draw.rect(screen, (255, 0, 0), (player_pos[0] * TILE_SIZE, player_pos[1] * TILE_SIZE, TILE_SIZE, TILE_SIZE))
    pygame.display.flip()  # Actualiza la pantalla para mostrar los cambios
    clock.tick(60)  # Mantiene el juego corriendo a 60 fotogramas por segundo (FPS)

pygame.quit()  # Cierra Pygame de manera segura cuando el bucle principal termina
sys.exit()  #Controla que el videojuego se cierre de manera correcta 