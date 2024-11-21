import pygame
import sys
from player import Player
from enemy import Enemy
from button import Button
from contador import tiempo
import random
from progress import set_current_level
from Localization_manager import localization
class Level1:
    def __init__(self, state_manager):
        # Datos de pantalla
        self.screen = pygame.display.set_mode((1280, 720))  # Creamos la ventana con sus medidas
        self.clock = pygame.time.Clock() # Reloj para controlar los FPS
        self.TILE_SIZE = 32
        self.state_manager = state_manager
        self.character_index = self.state_manager.get_selected_character()
        if self.character_index is None:
            print("Error: No character selected")
            self.character_index = 0
        else:
            print(f"Selected character index: {self.character_index}")
        
         # Obtener la dificultad del state_manager
        self.difficulty = self.state_manager.get_difficulty()
        print(f"Level1 initialized with difficulty: {self.difficulty}")  # Añade esta línea para depurar
        
        self.player = Player(400, 400, self.character_index, self.difficulty)
        self.paused = False
        self.keys_pressed = None
        self.timer = tiempo()
        self.start_time = pygame.time.get_ticks()
        self.time_left = 100
        self.all_bubbles = pygame.sprite.Group()
        self.all_enemies = pygame.sprite.Group()
        self.score = 0
        # Carga de sonidos
        self.lose_sound = pygame.mixer.Sound("assets/sounds/perder.mp3")
        self.select_sound = pygame.mixer.Sound("assets/sounds/select.mp3")
        self.enemy_hurt_sound = pygame.mixer.Sound("assets/sounds/enemy_hurt.mp3")
        self.win_sound = pygame.mixer.Sound("assets/sounds/victoria.mp3")
        self.enemy_sound = pygame.mixer.Sound("assets/sounds/hit_hurt-3.mp3")
        self.music = pygame.mixer.music.load("assets/sounds/musiclevel1y2.mp3")
        pygame.mixer.music.play(-1)
         # Obtener la dificultad del state_manager
        self.difficulty = self.state_manager.get_difficulty()
        print(f"Level1 initialized with difficulty: {self.difficulty}")  # Añade esta línea para depurar

        # Ajustar puntos por enemigo según la dificultad
        if self.difficulty == "Beginner":
            self.points_per_enemy = 5
        elif self.difficulty == "Advanced":
            self.points_per_enemy = 15

        # Posiciones iniciales de los enemigos
        self.enemy_positions = [
            (900, 400),
            (960, 400),
            (1060, 400),
            (1160, 400)
        ]
        self.create_enemies()
        self.enemy_count = len(self.all_enemies)
        
        # Creamos el mapa de obstáculos (1 = obstáculo, 0 = espacio libre)
        self.map_data = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
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
        self.font = pygame.font.Font("font.ttf", 35)
        self.font2 = pygame.font.Font("assets/fonts/SCREEN.TTF", 25)
        self.fondo1_1= pygame.image.load("assets/sprites/PANTALLASELECCIONPERSONAJE1.png")
        self.botonR_1 = pygame.image.load("assets/sprites/boton_crditos1.png")
        self.botonS_1 = pygame.image.load("assets/sprites/boton_crditos1.png")
        self.reloj = pygame.image.load("assets/sprites/reloj.png")
        self.viruscount = pygame.image.load("assets/sprites/virus-count.png")
        self.score_image = pygame.image.load("assets/sprites/score.png")

        # Escalar los recursos
        self.fondo1_1 = pygame.transform.scale(self.fondo1_1, (1280, 720 ))
        self.botonR_1 = pygame.transform.scale(self.botonR_1, (370, 250)) 
        self.botonS_1 = pygame.transform.scale(self.botonS_1, (370, 250))
        self.viruscount = pygame.transform.scale(self.viruscount, (154, 54)) 
        self.reloj = pygame.transform.scale(self.reloj, (154, 54))
        self.score_image = pygame.transform.scale(self.score_image, (154, 54))

        # Crear botones
        self.pause_button = Button(self.pause_image, (640, 40), "", self.get_font(25), "black", "Green")
        self.resume_button = Button(
            self.botonR_1, (642, 250), localization.get_text("resume"),
            self.get_font(25), "White", "Green", text_offset=(0, 0)  # Texto desplazado hacia arriba
        )
        
        self.go_out_button = Button(
            self.botonS_1, (642, 400), localization.get_text("go out"),
            self.get_font(25), "White", "Green", text_offset=(0, 0)  # Texto desplazado hacia arriba
        )

        # Texto
        self.texto1 = self.font.render("pause", True, "black")
        self.texto1_rect = self.texto1.get_rect(center = (642, 130))
        
        self.resume_button_rect = self.botonR_1.get_rect(topleft=(642,250))  # Ajusta la posición
        self.go_out_button_rect = self.botonS_1.get_rect(topleft=(642,370))  # Ajusta la posición
        

    def create_enemies(self):
        self.all_enemies.empty()  # Vacía el grupo de enemigos
        for pos in self.enemy_positions:
            enemy = Enemy(pos[0], pos[1])
            self.all_enemies.add(enemy)
        self.enemy_count = len(self.all_enemies)
        self.all_enemies.add(enemy)    
        
    def get_font(self, size):
        return pygame.font.Font("assets/fonts/GAME.TTF", size)
    
    def draw_overlay(self):
        overlay = pygame.Surface((1280, 720))
        overlay.fill((0, 0, 0))
        overlay.set_alpha(128)
        self.screen.blit(overlay, (0, 0))
        self.screen.blit(self.fondo1_1, (0, 0))
        self.resume_button.update(self.screen)
        self.go_out_button.update(self.screen)
     
        pygame.display.flip()
    
    def update_text(self):
        self.texto1 = self.get_font(40).render(localization.get_text("pause"), True,"black")
       

    def update(self):
        
        self.check_collision()        
        if not self.paused:
            elapsed_time = (pygame.time.get_ticks() - self.start_time) // 1000
            self.time_left = max(0, 100 - elapsed_time)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.pause_button.checkForInput(pygame.mouse.get_pos()):
                        self.paused = True
                        self.pause_start_time = pygame.time.get_ticks()
                        self.select_sound.play()
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
                    elif event.key == pygame.K_l:
                        print(f"character_index: {self.player.character_index}")
                self.update_text()

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
            self.check_player_enemy_collision()

            for enemy in self.all_enemies:
                enemy.update(self.player.rect, self.obstacles)
            self.all_bubbles.update(self.obstacles, self.all_enemies, self)
        
            pygame.display.flip()
            
        if self.time_left == 0 or self.player.is_dead:
            self.state_manager.set_state("lose_menu")
            self.lose_sound.play()
            pygame.mixer.music.pause()

        if len(self.all_enemies) == 0:
            self.state_manager.set_state("win_menu")
            self.win_sound.play()
            pygame.mixer.music.pause()

            set_current_level(2)

        if self.paused:
            pygame.mixer.music.pause() #Pausa la musica
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
                            self.select_sound.play()
                            pygame.mixer.music.unpause()

                        elif self.resume_button.checkForInput(pygame.mouse.get_pos()):
                            self.paused = False
                            self.start_time += pygame.time.get_ticks() - self.pause_start_time
                            self.select_sound.play()
                            pygame.mixer.music.unpause()
                            
                        elif self.go_out_button.checkForInput(pygame.mouse.get_pos()):
                            self.paused = False
                            self.reset_game_state()
                            self.state_manager.set_state("levels")    
                            self.select_sound.play()
                            pygame.mixer.music.unpause()
                            
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            self.paused = False
                            self.start_time += pygame.time.get_ticks() - self.pause_start_time
                            pygame.mixer.music.unpause()

                self.clock.tick(60)

        pygame.display.flip()
        self.clock.tick(60)
        
    def check_player_enemy_collision(self):
        for enemy in self.all_enemies:
            if self.player.rect.colliderect(enemy.rect):
                self.player.change_health(-1)
                self.move_enemy_away(enemy)
                self.enemy_sound.play()
                
    def move_enemy_away(self, enemy):
        max_attempts = 100  # Número máximo de intentos para encontrar una posición válida
        attempts = 0
        while attempts < max_attempts:
            new_x = random.randint(0, self.screen.get_width() - enemy.rect.width)
            new_y = random.randint(0, self.screen.get_height() - enemy.rect.height)
            new_rect = pygame.Rect(new_x, new_y, enemy.rect.width, enemy.rect.height)
            if not self.player.rect.colliderect(new_rect) and not any(obstacle.colliderect(new_rect) for obstacle in self.obstacles):
                enemy.rect.topleft = (new_x, new_y)
                enemy.get_random_direction()  # Asignar un nuevo rumbo aleatorio
                break
            attempts += 1
        else:
            # Si no se encuentra una posición válida, mantener al enemigo en su posición actual
            print("No se encontró una posición válida para alejar al enemigo.")
        
    def reset_game_state(self):
        self.player = Player(400, 400, self.character_index, self.difficulty)
        self.paused = False
        self.keys_pressed = None
        self.timer = tiempo()
        self.start_time = pygame.time.get_ticks()
        self.time_left = 100
        self.all_bubbles.empty()
        self.create_enemies()
        self.screen.fill((0, 0, 0))  # Limpiar la pantalla al resetear el estado
        pygame.display.flip()
        
    def check_collision(self):
        for bubble in self.all_bubbles:
            enemy_hit_list = pygame.sprite.spritecollide(bubble, self.all_enemies, True)
            if enemy_hit_list:
                bubble.kill()
                self.enemy_hurt_sound.play()
                for enemy in enemy_hit_list:
                    self.enemy_count -= 1
                    self.score += self.points_per_enemy
                    self.all_enemies.remove(enemy)
                    self.screen.blit(self.background, enemy.rect, enemy.rect)
            
    def draw(self, screen):
        self.screen.blit(self.background, (0, 0))
        self.player.draw(screen)
        self.all_enemies.draw(screen)
        self.all_bubbles.draw(screen)

        self.pause_button.update(screen)
        
        self.screen.blit(self.reloj, (1120, 10))
        self.screen.blit(self.viruscount, (1120, 64))
        self.screen.blit(self.score_image, (1120, 118))
        
        tiempo.draw_timer(screen, self.time_left)
        
        self.enemy_count_text = self.font2.render(f"{self.enemy_count}", True, "black")
        self.screen.blit(self.enemy_count_text, (1210, 80))
        
        self.score_text = self.font2.render(f"{self.score}", True, "black")
        self.screen.blit(self.score_text, (1210, 135))
        
        #tiren paro