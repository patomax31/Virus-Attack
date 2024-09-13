import pygame
import sys

# Configuraciones basicas
SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720  # Dimensiones de la ventana del juego
TILE_SIZE = 32  # Tamaño de cada cuadro en la cuadrícula del juego
player_pos = [5, 5]  # Posición inicial del jugador en la cuadrícula (x, y)

# Inicialización de Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # Crea la ventana del juego con el tamaño especificado
clock = pygame.time.Clock()  # Reloj para controlar la tasa de actualización del juego

# Funcion para mover al jugador según la dirección dada
def move_player(direction):
    """A partir de aqui esti mueve al jugador en la dirección especificada."""
    if direction == 'UP':       # Movimiento hacia arriba
        player_pos[1] -= 1
    elif direction == 'DOWN':   # Movimiento hacia abajo
        player_pos[1] += 1
    elif direction == 'LEFT':   # Movimiento hacia la izquierda
        player_pos[0] -= 1
    elif direction == 'RIGHT':  # Movimiento hacia la derecha
        player_pos[0] += 1

# Bucle principal del juego
running = True
while running:
    for event in pygame.event.get():  # Revisa todos los eventos que ocurren en Pygame
        if event.type == pygame.QUIT:  # Si se cierra la ventana esto detiene el bucle
            running = False
        elif event.type == pygame.KEYDOWN:  # Detecta si se presiona una tecla
            # Aqui se asignan los controles de movimiento con las teclas WASD
            if event.key == pygame.K_w:      # Tecla W para moverse hacia arriba
                move_player('UP')
            elif event.key == pygame.K_s:    # Tecla S para moverse hacia abajo
                move_player('DOWN')
            elif event.key == pygame.K_a:    # Tecla A para moverse hacia la izquierda
                move_player('LEFT')
            elif event.key == pygame.K_d:    # Tecla D para moverse hacia la derecha
                move_player('RIGHT')

    # Renderizado de la pantalla y jugador
    screen.fill((0, 0, 0))  # Limpia la pantalla llenandola de color negro
    # Dibuja al jugador como un rectángulo rojo en la posición actual multiplicada por el tamaño de los cuadros
    pygame.draw.rect(screen, (255, 0, 0), (player_pos[0] * TILE_SIZE, player_pos[1] * TILE_SIZE, TILE_SIZE, TILE_SIZE))
    pygame.display.flip()  # Actualiza la pantalla para mostrar los cambios
    clock.tick(60)  # Mantiene el juego corriendo a 60 fotogramas por segundo (FPS)

pygame.quit()  # Cierra Pygame de manera segura cuando el bucle principal termina
sys.exit()  #Controla que el videojuego se cierre de manera correcta 