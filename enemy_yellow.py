import pygame
import random
from settings import TILE_SIZE
from player import Player
class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.target_x = self.x
        self.target_y = self.y
        self.speed = 4  # Asegúrate de que la velocidad sea un divisor exacto de TILE_SIZE
        self.moving = False
        self.direction = self.get_random_direction()
        
        self.enemy_load_sprites()

        self.image = self.current_sprite
        self.rect = self.image.get_rect(center=(self.x, self.y))
        
    def get_random_direction(self):
        directions = ["UP", "DOWN", "LEFT", "RIGHT"]
        return random.choice(directions)

    def enemy_load_sprites(self):
        self.current_sprite = pygame.image.load("assets/sprites/enemy_2.png").convert_alpha()
        self.current_sprite = pygame.transform.scale(self.current_sprite, (int(self.current_sprite.get_width() * 0.5), int(self.current_sprite.get_height() * 0.5)))

    def draw(self, surface):
        surface.blit(self.current_sprite, self.rect)
    
    def update(self, player_rect, obstacles):
        
        if self.direction == "UP":
            new_y = self.rect.y - self.speed
            if not self.check_collision(self.rect.x, new_y, obstacles):
                self.rect.y = new_y
            else:
                self.direction = self.get_random_direction()
        elif self.direction == "DOWN":
            new_y = self.rect.y + self.speed
            if not self.check_collision(self.rect.x, new_y, obstacles):
                self.rect.y = new_y
            else:
                self.direction = self.get_random_direction()
        elif self.direction == "LEFT":
            new_x = self.rect.x - self.speed
            if not self.check_collision(new_x, self.rect.y, obstacles):
                self.rect.x = new_x
            else:
                self.direction = self.get_random_direction()
        elif self.direction == "RIGHT":
            new_x = self.rect.x + self.speed
            if not self.check_collision(new_x, self.rect.y, obstacles):
                self.rect.x = new_x
            else:
                self.direction = self.get_random_direction()
        
    def move_random(self, obstacles, Player):
        directions = [(0, -TILE_SIZE), (0, TILE_SIZE), (-TILE_SIZE, 0), (TILE_SIZE, 0)]
        random.shuffle(directions)  # Mezcla las direcciones para intentar en orden aleatorio
        for dx, dy in directions:
            new_x = self.target_x + dx
            new_y = self.target_y + dy

            if not self.check_collision(new_x, new_y, obstacles):
                self.target_x = new_x
                self.target_y = new_y
                self.dx, self.dy = dx, dy
                self.moving = False
                break  # Sale del bucle una vez que encuentra una dirección válida

    
    def move(self):
        if self.moving:
            if self.rect.x < self.target_x:
                self.rect.x += self.speed
                if self.rect.x > self.target_x:
                    self.rect.x = self.target_x
            elif self.rect.x > self.target_x:
                self.rect.x -= self.speed
                if self.rect.x < self.target_x:
                    self.rect.x = self.target_x

            if self.rect.y < self.target_y:
                self.rect.y += self.speed
                if self.rect.y > self.target_y:
                    self.rect.y = self.target_y
            elif self.rect.y > self.target_y:
                self.rect.y -= self.speed
                if self.rect.y < self.target_y:
                    self.rect.y = self.target_y

            if self.rect.x == self.target_x and self.rect.y == self.target_y:
                self.moving = False

    def handle_collisions(self, player_rect, obstacles):
        if self.rect.colliderect(player_rect):
            self.rect.x = self.dx
            self.rect.y = self.dy
        for obstacle in obstacles:
            if self.rect.colliderect(obstacle):
                self.rect.x -= self.dx
                self.rect.y -= self.dy

    def check_collision(self, new_x, new_y, obstacles):
        enemy_rect = pygame.Rect(new_x, new_y, self.rect.width, self.rect.height)
        for obstacle in obstacles:
            if enemy_rect.colliderect(obstacle):
                return True
        return False