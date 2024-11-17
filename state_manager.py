class StateManager:
    
    def __init__(self):
        self.states = {} # Diccionario de estados
        self.state = None # Estado actual none por defecto
        self.current_state = None
        self.selected_level = None
        self.selected_character = None
        self.difficulty = "Beginner"
        self.selected_character = 3
        
    def add_state(self, state_name, state):
        self.states[state_name] = state # Añade un estado al diccionario de estados
        
    def change_state(self, new_state):
        self.current_state = new_state    
        
    def set_state(self, state_name, level=None, character_index=None):
        self.current_state = self.states[state_name]
        if level:
            self.selected_level = level
        if character_index is not None:
            self.selected_character = character_index
        if hasattr(self.current_state, 'player'):
            self.current_state.player.character_index = self.selected_character

    def get_selected_level(self):
        return self.selected_level
    
    def get_selected_character(self):
        return self.selected_character
    
    def set_difficulty(self, difficulty):
        self.difficulty = difficulty
    
    def get_difficulty(self):
        return self.difficulty
    
    def set_selected_character(self, character_index):
        self.selected_character = character_index
        
    def update(self):
        if self.current_state:
            self.current_state.update()
            
    def draw(self, screen):
        if self.current_state:
            self.current_state.draw(screen)