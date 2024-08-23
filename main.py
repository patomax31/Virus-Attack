import pygame

#general setup
pygame.init
window_widht, window_height = 1200, 720
display_surface = pygame.display.set_mode((window_widht, window_height))
pygame.display.set_caption(title=("VIDEOJUEGO"))
running= True

#surface
surf = pygame.Surface((100, 200))
surf.fill("white")

while running:
    #event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False       
            
    #draw the game
    display_surface.fill("darkgray")
    display_surface.blit(surf,(100,200))
    pygame.display.update()
    
pygame.quit()