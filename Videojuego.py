import pygame
#prueba de commit cris
pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
#en screen_width y height pude haber puesto directamente 800 y 600 pero es mejor tenerlo en variables
player= pygame.Rect((300, 250, 50, 50))


run = True
while run:
#otra vez, pude utilizar true en vez de run para el bucle    
    screen.fill((0, 0, 0,))

    pygame.draw.rect(screen, (255, 0, 0), player)
    
    key = pygame.key.get_pressed()
    if key[pygame.K_a] == True:
        player.move_ip(-1, 0)
    elif key[pygame.K_d] == True:
        player.move_ip(1, 0)    
    elif key[pygame.K_w] == True:
        player.move_ip(0, -1)    
    elif key[pygame.K_s] == True:
        player.move_ip(0, 1)    
        
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            run=False
#El bucle se mantiene siempre true hasta darle salir que se vuelve false
    pygame.display.update()
    #actualiza la pantalla
            
pygame.quit