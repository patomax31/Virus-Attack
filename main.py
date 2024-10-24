import pygame
import sys
from player import Player
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, WHITE, TILE_SIZE # Importamos configuraciones
from bubble import Bubble
from contador import tiempo
from pauseButton import PauseButton
from button import Button
from enemy import Enemy
# Inicializamos pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # Creamos la ventana con sus medidas
clock = pygame.time.Clock() # Creamos est amadre que es para controlar los FPS



# Creamos el mapa de obstáculos (1 = obstáculo, 0 = espacio libre)
map_data = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1], 
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

# Convertimos el mapa en una lista de rectángulos que representan las colisiones
obstacles = [] # Esta es la lista donde almacenamoslos obstaculos del mapa
for row_idx, row in enumerate(map_data): # Recorre cada fila del mapa y la indexa
    for col_idx, cell in enumerate(row): # Recorre cada columna de la fila
        if cell == 1: # Si la celda es igual a 1 (osea un obstaculo) crae un rectangulo
            obstacle_rect = pygame.Rect(col_idx * TILE_SIZE, row_idx * TILE_SIZE, TILE_SIZE, TILE_SIZE) # Crea el rectangulo para el obstaculo
            obstacles.append(obstacle_rect) # Con esto añadimos el rectangulo a la lista

# Creamos la instancia del jugador
player = Player(400, 400) # Posicion inicial del jugador en la cuadricula
player.load_sprites() # Cargamos los sprites despues de inicializar la pantalla

enemy = Enemy(1000, 500) # Posicion inicial del enemigo en la cuadricula

#Enemy
#enemy = Enemy(400, 500)
#enemy.enemy_load_sprites()

# Inicializamos el grupo de burbujas
all_bubbles = pygame.sprite.Group()

#FONDO
bg= pygame.image.load("assets/sprites/Fondo.jpeg")
#Fuentes de texto
def get_font(size): # Funcion para obtener la fuente de texto
    return pygame.font.Font("font.ttf", size) # Devuelve la fuente de texto con el tamaño especificado


def main_menu():
    #IMAGENES DE LOS BOTONES
    Play=pygame.image.load("assets/sprites/Play.png")
    Play = pygame.transform.scale(Play, (200, 200))

    Quit=pygame.image.load("assets/sprites/Quit.png")
    Quit = pygame.transform.scale(Quit, (200, 200))

    Options = pygame.image.load("assets/sprites/Options.png")
    Options = pygame.transform.scale(Options, (200, 200))
    
    title = pygame.image.load("assets/sprites/Title.png")
    title = pygame.transform.scale(title, (1300, 1000))
    while True:
        screen.fill((0, 0, 100,))


        MENU_MOUSE_POS = pygame.mouse.get_pos()

        #MENU_TEXT = get_font(60).render("VIRUS ATTACK", True, "#f57842")
        #MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=Play, pos=(640, 350), 
                            text_input=None, font=get_font(75), base_color="green", hovering_color="White")
       
        QUIT_BUTTON = Button(image=Quit, pos=(1000, 350), 
                            text_input=None, font=get_font(75), base_color="black", hovering_color="white")

        OPTIONS_BUTTON = Button(image=Options, pos=(250, 350), 
                                    text_input=None, font=get_font(75), base_color="black", hovering_color="white")
        #Muestra el fondo y el titulo del videojuego
        screen.blit(bg, (0, 0))
        screen.blit(title, (0, 0))
      #  screen.blit(MENU_TEXT, MENU_RECT)
        
        
        for button in [PLAY_BUTTON, QUIT_BUTTON, OPTIONS_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
       #     button.update(screen=pygame.image.load("Quit.png"))
            button.update(screen)

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    lv_selector()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()    
def lv_selector():
   while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        
        screen.fill("black")
        screen.blit(bg, (0, 0))

        PLAY_TEXT = get_font(45).render(" ", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
        screen.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(50), base_color="red", hovering_color="Green")
        Level = Button(image=None, pos=(250, 250), 
                            text_input="NIVEL", font=get_font(50), base_color="red", hovering_color="Green")
        Level_two = Button(image=None, pos=(600, 250), 
                            text_input="NIVEL", font=get_font(50), base_color="red", hovering_color="Green")
        Level_tres = Button(image=None, pos=(1000, 250), 
                            text_input="NIVEL", font=get_font(50), base_color="red", hovering_color="Green")    
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(screen)
        Level.changeColor(PLAY_MOUSE_POS)
        Level.update(screen)
        Level_two.changeColor(PLAY_MOUSE_POS)
        Level_two.update(screen)
        Level_tres.changeColor(PLAY_MOUSE_POS)
        Level_tres.update(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Level.checkForInput(PLAY_MOUSE_POS):
                    lv_1()    
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Level_two.checkForInput(PLAY_MOUSE_POS):
                    lv_1()         
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Level_tres.checkForInput(PLAY_MOUSE_POS):
                    lv_1()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
            

        pygame.display.update()    


def lv_1():
    running = True # Creamos esta variable que controla is el juego esta corriendo
    paused = False # Estado del juego (si esta pausado o no)
    pause_button = PauseButton() # Almacenamos la instancia del boton de pausa
    keys_pressed = None # Creamos esta variable que almacena las teclas precionadas en ella
    start_time = pygame.time.get_ticks() # Marca el tiempo al inicios
    font = pygame.font.Font("font.ttf", 35)
    fondo1_1= pygame.image.load("assets/sprites/fondo1_1.png")
    fondo1_1 = pygame.transform.scale(fondo1_1, (560, 600)) 
    # boton de reanudar
    botonR_1 = pygame.image.load("assets/sprites/botonR.png")
    botonR_1 = pygame.transform.scale(botonR_1, (300, 70)) 
    resume_button = Button(botonR_1,(642, 300), "Reanudar", get_font(25), "Black", "Green")
    #boton de salir 
    botonS_1 = pygame.image.load("assets/sprites/botonS.png")
    botonS_1 = pygame.transform.scale(botonS_1, (300, 70)) 
    go_out_button = Button(botonS_1,(642, 450), "Salir", get_font(25), "Black", "Green")
    #texto
    texto1 = font.render("pause", True, "white")
    texto1_rect = texto1.get_rect(center = (642, 130))

    while running:
        # Calculamos el tiempo transcurrido
        if not paused:
            elapsed_time = (pygame.time.get_ticks() - start_time) // 1000  # Hacemos la conversión a segundos
        else:
            start_time = pygame.time.get_ticks() - (elapsed_time * 1000)  # Ajustamos el tiempo cuando se reanuda
        time_left = max(0, 100 - elapsed_time)  # Tiempo restante en segundos

        for event in pygame.event.get():  # Revisa todos los eventos que ocurren en Pygame
            if event.type == pygame.QUIT or time_left == 0:  # Si se cierra la ventana esto detiene el bucle
                running = False  # Detiene la ejecución del juego

            if event.type == pygame.MOUSEBUTTONDOWN:
                if pause_button.is_clicked(event.pos):
                
                    paused = not paused  # Si le damos click al botón se cambia el estado de la pausa

            current_direction = "DOWN" # Direccion por default 

            if not paused:
                # Detectamos cuando se presiona la barra espaciadora para disparar
                if event.type == pygame.KEYDOWN:  # Detecta si se presiona una tecla
                    if event.key == pygame.K_w:
                        current_direction = "UP"  # Cambia la dirección cuando se presiona la tecla W
                    elif event.key == pygame.K_s:
                        current_direction = "DOWN"  # Cambia la dirección cuando se presiona la tecla S
                    elif event.key == pygame.K_a:
                        current_direction = "LEFT"  # Cambia la dirección cuando se presiona la tecla A
                    elif event.key == pygame.K_d:
                        current_direction = "RIGHT"  # Cambia la dirección cuando se presiona la tecla D

                    if event.key == pygame.K_j:  # Verifica si la tecla presionada es J
                        player.shoot(all_bubbles)  # Llamamos a la función shoot del archivo player y agregamos burbujas al grupo

                    if event.key == pygame.K_ESCAPE:
                        paused = not paused  # Cambiamos el estado de la pausa si presionamos escape

                    if event.key == pygame.K_z:
                        player.change_health()  # Cambiamos la vida del jugador si presionamos Z
            
        if not paused:
            # Manejo de eventos
            
            keys = pygame.key.get_pressed()  # Detecta si las teclas están presionadas
            if keys[pygame.K_w]:
                player.move('UP', obstacles)
            elif keys[pygame.K_s]:
                player.move('DOWN', obstacles)
            elif keys[pygame.K_a]:
                player.move('LEFT', obstacles)
            elif keys[pygame.K_d]:
                player.move('RIGHT', obstacles)
            else:
                player.snap_to_grid()  # Llamamos a la función snap_to_grid del archivo player para alinear al jugador hacia la casilla más cercana

        

            player.update() # ACtualizamos el estado del jugador
            all_bubbles.update() # Actualizamos el estado de todas las burbujas

        BG = pygame.image.load("background1.png") # Cargamos la imagen del fondo para el nivel 1 en una variable almacenada



        # Renederizamos la pantalla
        screen.blit(BG, (0, 0)) # Sobreponemos el fondo sobre el fondo blanco
        player.draw(screen) # Renderizamos al jugador
        enemy.enemy_draw(screen)
        all_bubbles.draw(screen) # Renderizamos a las burbujas del gruppo
        player.draw_health_bar(screen) # Renderizamos la barra de vida del jugador
        tiempo.draw_timer(screen, time_left) # Renderizamos el temporizadorr
        pause_button.draw(screen) # Renderizamos el btoin de pausea
        pygame.display.flip() # Esta madre actualiza la pantalla con nuevos graficoss

        if paused:  # si el estado de paused es verdadero
            # Dibujamos una pantalla semitransparente de mientras
            overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
            overlay.fill((0, 0, 0))  # pintamos color negro a la roña
            overlay.set_alpha(128)  # Le ponemos transparencia (la transparencia se mide del 0 al 255 donde el 0 es completamente transparente)  
            screen.blit(overlay, (0, 0))
            screen.blit(fondo1_1, (365, 50))
            resume_button.update(screen)
            go_out_button.update(screen)
            screen.blit(texto1, texto1_rect)
            pygame.display.flip()
            


            # Dibujamos el botón de pausa mientras el juego está en pausa
            pause_button.draw(screen)
            pygame.display.flip()  # actualizamos la pantalla
            while paused:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                        paused = False
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if pause_button.is_clicked(event.pos):
                         Reanudar = pygame.image.load("assets/sprites/Reanudar.png")
                         Salir = pygame.image.load("assets/sprites/Salir.png")
                        paused = not paused
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            paused = not paused
                        if event.key ==pygame.K_p:
                          lv_selector()
                            
                clock.tick(FPS)
            continue  # saltamos el resto del bucle para que nada más se mueva

        # Controlamos los FPS
        clock.tick(FPS)
        
    # Finalizamos pygame chido
    pygame.quit() # Cierra pygame de manera segura y finaliza el bucle
    sys.exit() # Controla que el videojuego se cierre de manera correcta
    #Tiren paro
main_menu()