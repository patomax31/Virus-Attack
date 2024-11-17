import pygame
import sys
from player import Player
from enemy import Enemy
from button import Button
from contador import tiempo
from objects import soap


class Tutorial:
    def __init__(self, state_manager):
        # Datos de pantalla
        font_game = pygame.font.Font("assets/fonts/GAME.TTF", 50)
        font_screen_title = pygame.font.Font("assets/fonts/SCREEN.TTF", 40)
        self.state_manager = state_manager
        character_index = self.state_manager.get_selected_character()
        print(f"Selected character index: {character_index}")
        self.player = Player(400, 400, character_index)
        self.screen = pygame.display.set_mode((1280, 720))  # Creamos la ventana con sus medidas
        self.clock = pygame.time.Clock() # Reloj para controlar los FPS
        self.TILE_SIZE = 32
        self.enemy = Enemy(960, 400)
        self.soap = soap(500, 400)
        self.paused = False
        self.keys_pressed = None
        self.timer = tiempo()
        self.start_time = pygame.time.get_ticks()
        self.time_left = 1000
        self.all_bubbles = pygame.sprite.Group()
        self.all_enemies = pygame.sprite.Group()
        self.all_enemies.add(self.enemy)
        
        
        self.difficulty = self.state_manager.get_difficulty()
        
        # Creamos el mapa de obstáculos (1 = obstáculo, 0 = espacio libre)
        self.map_data = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
            [1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
            [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1], 
            [1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1],
            [1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        ]
        
        # Convertimos el mapa en una lista de rectángulos que representan las colisiones
        self.obstacles = [] # Esta es la lista donde almacenamoslos obstaculos del mapa
        for row_idx, row in enumerate(self.map_data): # Recorre cada fila del mapa y la indexa
            for col_idx, cell in enumerate(row): # Recorre cada columna de la fila
                if cell == 1: # Si la celda es igual a 1 (osea un obstaculo) crae un rectangulo
                    obstacle_rect = pygame.Rect(col_idx * self.TILE_SIZE, row_idx * self.TILE_SIZE, self.TILE_SIZE, self.TILE_SIZE) # Crea el rectangulo para el obstaculo
                    self.obstacles.append(obstacle_rect) # Con esto añadimos el rectangulo a la lista

        # Carga de sonidos
        self.walk_sound = pygame.mixer.Sound("assets/sounds/walk.mp3")

        # Carga de recursos
        self.background = pygame.image.load("assets/sprites/tutorial_bg.png")
        self.pause_image = pygame.image.load("assets/sprites/pauseButton.png")
        self.w = pygame.image.load("assets/sprites/tecla_w.png")
        self.a = pygame.image.load("assets/sprites/tecla_a.png")
        self.s = pygame.image.load("assets/sprites/tecla_s.png")
        self.d = pygame.image.load("assets/sprites/tecla_d.png")
        self.space = pygame.image.load("assets/sprites/tecla_space.png")
        
        # Escalar los recursos
        self.difficulty = font_screen_title.render("Press to move", True, (78, 248, 71))
        
        
        # Crear botones
        self.pause_button = Button(self.pause_image, (self.screen.get_width()//2, 50), "", self.get_font(15), "Black", "Green")
        
    def get_font(self, size):
        return pygame.font.Font("font.ttf", size)
    
    def draw_overlay(self):
        overlay = pygame.Surface((1280, 720))
        overlay.fill((0, 0, 0))
        overlay.set_alpha(128)
        self.screen.blit(overlay, (0, 0))
        self.pause_button.update(self.screen)
        pygame.display.flip()
        #BUCLE
    def update(self, difficulty):
        if not self.paused:
            elapsed_time = (pygame.time.get_ticks() - self.start_time) // 1000
            self.time_left = max(0, 1000 - elapsed_time)



            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.pause_button.checkForInput(pygame.mouse.get_pos()):
                        self.paused = True
                        self.pause_start_time = pygame.time.get_ticks()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.paused = True
                        self.pause_start_time = pygame.time.get_ticks()
                    elif event.key == pygame.K_w:
                        self.player.move('UP', self.obstacles)
                    elif event.key == pygame.K_s:
                        self.player.move('DOWN', self.obstacles)
                    elif event.key == pygame.K_a:
                        self.player.move('LEFT', self.obstacles)
                    elif event.key == pygame.K_d:
                        self.player.move('RIGHT', self.obstacles)
                    elif event.key == pygame.K_z:
                        self.player.change_health()
                    elif event.key == pygame.K_j:
                        self.player.shoot(self.all_bubbles, self.difficulty)

            keys = pygame.key.get_pressed()
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
            self.check_collision()
            self.soap.check_object_collision(self.obstacles, self.player.rect)
            
            self.all_enemies.update(self.player.rect, self.obstacles)
            self.all_bubbles.update(self.obstacles, self.all_enemies)
                        
            pygame.display.flip()

            
            
        #Moverse al jabon
        
        #Disparar al enemigo
        
        #Salir del mapa
        #PAUSA
        if self.paused:
            self.draw_overlay()
            pygame.display.flip()
            while self.paused:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        if self.pause_button.checkForInput(pygame.mouse.get_pos()):
                            self.paused = False
                            self.start_time += pygame.time.get_ticks() - self.pause_start_time
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            self.paused = False
                            self.start_time += pygame.time.get_ticks() - self.pause_start_time
                        elif event.key == pygame.K_p:
                            self.paused = False
                            self.reset_game_state()
                            self.state_manager.set_state("levels")
                            
                self.clock.tick(60)

        pygame.display.flip()
        self.clock.tick(60)
        #end bucle
    def reset_game_state(self):
        self.player = Player(400, 400)
        self.paused = False
        self.keys_pressed = None
        self.timer = tiempo()
        self.start_time = pygame.time.get_ticks()
        self.time_left = 100
        self.all_bubbles.empty()
        self.screen.fill((0, 0, 0))  # Limpiar la pantalla al resetear el estado
        pygame.display.flip()
        
    def check_collision(self):
        for bubble in self.all_bubbles:
            enemy_hit_list = pygame.sprite.spritecollide(bubble, self.all_enemies, True)
            if enemy_hit_list:
                bubble.kill()
                for enemy in enemy_hit_list:
                    self.all_enemies.remove(enemy)
                    self.screen.blit(self.background, enemy.rect, enemy.rect)
     #   for soap in object:
     #       soap= pygame.sprite.spritecollide(self.player.rect)
     #       if soap:
     #           soap.kill()
    def draw(self, screen):
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.w, (100, 200))
        self.screen.blit(self.a, (50, 250))
        self.screen.blit(self.s, (100, 250))
        self.screen.blit(self.d, (150, 250))
        self.screen.blit(self.space, (100, 300))
        self.screen.blit(self.difficulty, self.difficulty.get_rect(center=(120, 160)))      

        self.soap.draw(screen)        
        self.player.draw(screen)  
       # self.enemy.draw(screen)
        self.all_bubbles.draw(screen)
   
               # tiempo.draw_timer(screen, self.time_left)
        self.pause_button.update(screen)
 
