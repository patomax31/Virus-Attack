import pygame
import sys
from player import Player
from button import Button
from contador import tiempo

class Level1:
    def __init__(self, state_manager):
        # Datos de pantalla
        self.state_manager = state_manager
        self.screen = pygame.display.set_mode((1280, 720))  # Creamos la ventana con sus medidas
        self.clock = pygame.time.Clock() # Reloj para controlar los FPS
        self.TILE_SIZE = 32
        self.player = Player(400, 400)
        self.paused = False
        self.keys_pressed = None
        self.timer = tiempo()  # Initialize timer
        self.start_time = pygame.time.get_ticks()
        self.time_left = 100
        self.all_bubbles = pygame.sprite.Group()  # Define all_bubbles as a sprite group
        
        # Creamos el mapa de obstáculos (1 = obstáculo, 0 = espacio libre)
        self.map_data = [
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
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        ]
        
        # Convertimos el mapa en una lista de rectángulos que representan las colisiones
        self.obstacles = [] # Esta es la lista donde almacenamoslos obstaculos del mapa
        for row_idx, row in enumerate(self.map_data): # Recorre cada fila del mapa y la indexa
            for col_idx, cell in enumerate(row): # Recorre cada columna de la fila
                if cell == 1: # Si la celda es igual a 1 (osea un obstaculo) crae un rectangulo
                    obstacle_rect = pygame.Rect(col_idx * self.TILE_SIZE, row_idx * self.TILE_SIZE, self.TILE_SIZE, self.TILE_SIZE) # Crea el rectangulo para el obstaculo
                    self.obstacles.append(obstacle_rect) # Con esto añadimos el rectangulo a la lista

        # Carga de recursos
        self.background = pygame.image.load("assets/sprites/level1.png")
        self.pause_image = pygame.image.load("assets/sprites/pauseButton.png")
        
        # Escalar los recursos
        
        # Crear botones
        self.pause_button = Button(self.pause_image, (self.screen.get_width()//2, 50), "", self.get_font(25), "Black", "Green")
        
    def get_font(self, size):
        return pygame.font.Font("font.ttf", size)
    
    def draw_overlay(self):
        overlay = pygame.Surface((1280, 720))
        overlay.fill((0, 0, 0))
        overlay.set_alpha(128)
        self.screen.blit(overlay, (0, 0))
    
    def update(self):
        if not self.paused:
            elapsed_time = (pygame.time.get_ticks() - self.start_time) // 1000
        
        else:
            self.start_time = pygame.time.get_ticks() - (elapsed_time * 1000)
        self.time_left = max(0, 100 - elapsed_time)


        for event in pygame.event.get():
            if event.type == pygame.QUIT or self.time_left == 0:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.pause_button.checkForInput(pygame.mouse.get_pos()):
                    self.paused = not self.paused
                    if self.paused:
                        self.draw_overlay()

            elif event.type == pygame.KEYDOWN:
                if not self.paused:
                    if event.key == pygame.K_w:
                        self.player.move('UP', self.obstacles)
                    elif event.key == pygame.K_s:
                        self.player.move('DOWN', self.obstacles)
                    elif event.key == pygame.K_a:
                        self.player.move('LEFT', self.obstacles)
                    elif event.key == pygame.K_d:
                        self.player.move('RIGHT', self.obstacles)
                    elif event.key == pygame.K_z:
                        self.player.change_health()
                        
                    if event.key == pygame.K_j:
                        self.player.shoot(self.all_bubbles)

                if event.key == pygame.K_ESCAPE:
                    self.paused = not self.paused
                    if self.paused:
                        self.draw_overlay()
                        
                if event.key == pygame.K_p and self.paused:
                    self.state_manager.set_state("levels")
                    self.reset_game_state()

        keys = pygame.key.get_pressed()
        if not self.paused:
            if keys[pygame.K_w]:
                self.player.move('UP', self.obstacles)
            if keys[pygame.K_s]:
                self.player.move('DOWN', self.obstacles)
            if keys[pygame.K_a]:
                self.player.move('LEFT', self.obstacles)
            if keys[pygame.K_d]:
                self.player.move('RIGHT', self.obstacles)
            else:
                self.player.snap_to_grid()

            self.player.update()
            self.all_bubbles.update()

        if self.paused:
            self.draw_overlay()
            pygame.display.flip()
            while self.paused:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.running = False
                        self.paused = False
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        if self.pause_button.checkForInput(pygame.mouse.get_pos()):
                            self.paused = not self.paused
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            self.paused = not self.paused
                        elif event.key == pygame.K_p:
                            self.paused = not self.paused
                            self.reset_game_state()
                            self.state_manager.set_state("levels")
                self.clock.tick(60)
                continue
        
        pygame.display.flip()
        self.clock.tick(60)
        
    def reset_game_state(self):
        self.player = Player(400, 400)
        self.paused = False
        self.keys_pressed = None
        self.timer = tiempo()
        self.start_time = pygame.time.get_ticks()
        self.time_left = 100
        self.all_bubbles.empty()
            
    def draw(self, screen):
        self.screen.blit(self.background, (0, 0))
        self.player.draw(screen)
        self.all_bubbles.draw(screen)
        tiempo.draw_timer(screen, self.time_left)
        self.pause_button.update(screen)