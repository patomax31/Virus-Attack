import pygame
import sys

def grid(window, size, rows):
    # Iniciar nuestra cuadricula
    # Distancia entre filas o tamaño de nuestro cubo
    distanceBtwRows = size // rows
    x = 0
    y = 0
    for i in range(rows):
        # Incrementa x y y en base a la distancia entre filas
        x += distanceBtwRows
        y += distanceBtwRows
        # Dibuja nuestra cuadricula, color negro
        # Dibuja la línea vertical
        pygame.draw.line(window, (0, 0, 0), (x, 0), (x, size))
        # Dibuja la línea horizontal
        pygame.draw.line(window, (0, 0, 0), (0, y), (size, y))

def redraw(window, size, rows):
    # Rellenar la pantalla con color blanco
    window.fill((255, 255, 255))
    # Dibujar la cuadricula
    grid(window, size, rows)
    # Actualizar display
    pygame.display.update()

def main():
    pygame.init()
    size = 500
    rows = 20
    # Crear la ventana
    window = pygame.display.set_mode((size, size))
    pygame.display.set_caption("Ejemplo de cuadricula pal proyecto")

    # Loop principal
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Redibujar la ventana
        redraw(window, size, rows)

main()