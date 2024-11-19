import pygame
import time
from settings import SCREEN_WIDTH
class tiempo():
    def draw_timer(surface, time_left):
        font = pygame.font.Font("assets/fonts/SCREEN.TTF", 25)  # Use custom font GAME.TTF
        timer_text = font.render(f"{time_left // 60}:{time_left % 60:02d}", True, (255, 0, 0)) # Texto del temporizador
        surface.blit(timer_text,(1200, 25)) # Dibuja el temporizador


""" Traceback (most recent call last):
  File "/home/chris/VIdeojuego/main.py", line 6, in <module>
    from contador import tiempo
  File "/home/chris/VIdeojuego/contador.py", line 4, in <module>
    from main import *
  File "/home/chris/VIdeojuego/main.py", line 6, in <module>
    from contador import tiempo
ImportError: cannot import name 'tiempo' from partially initialized module 'contador' (most likely due to a circular import) (/home/chris/VIdeojuego/contador.py)"""
# No jala el contador :///