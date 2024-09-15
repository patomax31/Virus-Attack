import pygame

# Configuraciones básicas
SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720
TILE_SIZE = 32
FPS = 60

# Colores
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Inicialización de Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.target_x = x
        self.target_y = y
        self.speed = 5  # Velocidad del movimiento

    def move(self, direction):
        # Establece la posición objetivo basada en la dirección del movimiento
        if direction == 'UP':
            self.target_y -= TILE_SIZE
        elif direction == 'DOWN':
            self.target_y += TILE_SIZE
        elif direction == 'LEFT':
            self.target_x -= TILE_SIZE
        elif direction == 'RIGHT':
            self.target_x += TILE_SIZE

    def update(self):
        # Movimiento suave hacia la posición objetivo
        if self.x < self.target_x:
            self.x += self.speed
            if self.x > self.target_x:  # Corrige el desplazamiento sobrepasado
                self.x = self.target_x
        elif self.x > self.target_x:
            self.x -= self.speed
            if self.x < self.target_x:
                self.x = self.target_x

        if self.y < self.target_y:
            self.y += self.speed
            if self.y > self.target_y:
                self.y = self.target_y
        elif self.y > self.target_y:
            self.y -= self.speed
            if self.y < self.target_y:
                self.y = self.target_y

    def draw(self, surface):
        # Dibuja el jugador como un rectángulo rojo (puedes reemplazar con sprites)
        pygame.draw.rect(surface, RED, (self.x, self.y, TILE_SIZE, TILE_SIZE))

# Crear una instancia del jugador
player = Player(5 * TILE_SIZE, 5 * TILE_SIZE)  # Posición inicial

# Bucle principal del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.move('UP')
            elif event.key == pygame.K_DOWN:
                player.move('DOWN')
            elif event.key == pygame.K_LEFT:
                player.move('LEFT')
            elif event.key == pygame.K_RIGHT:
                player.move('RIGHT')

    # Actualiza el jugador
    player.update()

    # Renderiza la pantalla y el jugador
    screen.fill(BLACK)  # Limpia la pantalla
    player.draw(screen)  # Dibuja el jugador
    pygame.display.flip()
    clock.tick(FPS)  # Controla los FPS

pygame.quit()
