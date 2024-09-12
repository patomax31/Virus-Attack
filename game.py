import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
def get_font(size):
    return pygame.font.Font("font.ttf", size)

#Sprites/Surfaces
#player=pygame.image.load("player.png").convert_alpha()

enemy_surf = pygame.image.load("enemigo.gif").convert_alpha()
enemy_rect = enemy_surf.get_rect(topleft = (750,350))

player_surf = pygame.image.load("player.png").convert_alpha()
player_rect = player_surf.get_rect(topleft = (350,350))


#texto= get_font(80).render("My game", False, "Red")
MENU_TEXT = get_font(30).render("Test", True, "#b68f40")
MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

#loop
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("gray")

  #sprites
    screen.blit(MENU_TEXT,MENU_RECT)
    
    #player_x_pos+=1
    #screen.blit(player, (player_x_pos,player_y_pos))
    
    enemy_rect.left-= 0
    screen.blit(enemy_surf,enemy_rect)
    #surf player


    player_rect.left +=0
    screen.blit(player_surf,player_rect)
    pygame.display.flip()

    clock.tick(60)
pygame.quit()