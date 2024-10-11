class StateManager:
    
    def __init__(self):
        self.states = {} # Diccionario de estados
        self.state = None # Estado actual none por defecto
        
    def add_state(self, state_name, state):
        self.states[state_name] = state # Añade un estado al diccionario de estados
        
    def set_state(self, state_name):
        self.current_state = self.states.get(state_name) # Establece el estado actual a partir del nombre del estado
        
    def update(self):
        if self.current_state:
            self.current_state.update()
            
    def draw(self, screen):
        if self.current_state:
            self.current_state.draw(screen)