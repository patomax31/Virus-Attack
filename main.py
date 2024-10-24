import pygame
import sys
from state_manager import StateManager
from main_menu import MainMenu
from lv_selector import LevelSelector
from lv_1 import Level1

def main():
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    
    state_manager = StateManager()
    state_manager.add_state("main_menu", MainMenu(state_manager))
    state_manager.add_state("levels", LevelSelector(state_manager))
    state_manager.add_state("level1", Level1(state_manager))
    state_manager.set_state("main_menu")
    
    while True:
        state_manager.update()
        state_manager.draw(screen)
        pygame.display.flip()
        clock.tick(60)
        
if __name__ == "__main__":
    main()