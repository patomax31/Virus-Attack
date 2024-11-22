import pygame
import cv2

class Video:
    def __init__(self, state_manager):
        self.screen = pygame.display.set_mode((1280, 720))
        self.state_manager = state_manager
        self.clock = pygame.time.Clock()
        
        # Carga el video usando OpenCV
        self.video = cv2.VideoCapture("assets/VID/VIDEOVIRUSATTACK.mp4")
        self.playing = True
        self.start_time = pygame.time.get_ticks()
        self.music = pygame.mixer.music.load("assets/sounds/MUSICAVIRUSATTACK.mp3")
        pygame.mixer.music.play(-1)
    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.state_manager.quit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.playing = False
                self.state_manager.set_state("main_menu")
        
        if self.playing:
            ret, frame = self.video.read()
            if not ret:
                self.playing = False
                self.state_manager.set_state("main_menu")
                return
            
            frame = cv2.resize(frame, (1280, 720))
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = pygame.surfarray.make_surface(frame.swapaxes(0, 1))
            self.screen.blit(frame, (0, 0))
            pygame.display.flip()
            self.clock.tick(30)

    def draw(self, screen):
        pass

    def __del__(self):
        self.video.release()
        cv2.destroyAllWindows()