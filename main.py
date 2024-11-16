import pygame
from state_manager import StateManager
from main_menu import MainMenu
from lv_selector import LevelSelector
from lv_1 import Level1
from tutorial import Tutorial
from settings_menu import SettingsMenu
from player_selector import PlayerSelector
from lose_menu import LoseMenu
from win_menu import WinMenu
from lv_2 import Level2
from lv_3 import Level3
from credits import CreditsScreen

def main():
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    
    state_manager = StateManager()
    state_manager.add_state("Tutorial", Tutorial(state_manager)) #Agrege el tutorial al state manager
    state_manager.add_state("main_menu", MainMenu(state_manager))
    state_manager.add_state("player_selector", PlayerSelector(state_manager))
    state_manager.add_state("levels", LevelSelector(state_manager))
    state_manager.add_state("settings", SettingsMenu(state_manager))
    state_manager.add_state("lose_menu", LoseMenu(state_manager))
    state_manager.add_state("win_menu", WinMenu(state_manager))
    state_manager.add_state("credits", CreditsScreen(state_manager))
    
    # Cargar niveles según la dificultad
    difficulty = state_manager.get_difficulty()
    if difficulty == "Beginner":
        from lv_1 import Level1
        from lv_2 import Level2
        from lv_3 import Level3
    elif difficulty == "Advanced":
        from lv_1_advanced import Level1
        from lv_2_advanced import Level2
        from lv_3_advanced import Level3
    
    state_manager.add_state("level1", Level1(state_manager))
    state_manager.add_state("level2", Level2(state_manager))
    state_manager.add_state("Tutorial", Tutorial(state_manager))
    
    state_manager.set_state("main_menu")
  
    while True:
        state_manager.update()
        state_manager.draw(screen)
        pygame.display.flip()
        clock.tick(60)
        
if __name__ == "__main__":
    main()