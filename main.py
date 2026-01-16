import presets
import pygame
import assetLoader
import object
import renderer
import game


#Init 
pygame.init()

presets.init_font()

screen = pygame.display.set_mode(presets.VIRTUAL_SCREEN_RECT, pygame.RESIZABLE)
game_surface = pygame.Surface(presets.VIRTUAL_SCREEN_RECT)

pygame.display.set_caption("Apostasy v.1.0")

assetLoader.load_pngs("assets/images", pygame)

game.startGame(pygame)

clock = pygame.time.Clock()
running = True

def handle_window_event(event):
    global screen
    global running

    if event.type == pygame.VIDEORESIZE:
        screen = pygame.display.set_mode(
            event.size,
            pygame.RESIZABLE
        )

    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_F11:
            screen = pygame.display.set_mode(
                screen.get_size(),
                pygame.FULLSCREEN
            )
            
    if event.type == pygame.QUIT:
            running = False
    
    for obj in object.objectManager.objects:
        if hasattr(obj, "handle_event"):
            obj.handle_event(event)




#Main loop
while running:
    # 1. Events
    for event in pygame.event.get():
        handle_window_event(event)

    # 2. Update game state
    game.updateGame(pygame, clock.get_time())
    
    # 3. Draw
    renderer.renderScreen(pygame, game_surface, screen )

    # 4. Timing
    clock.tick(60)
    
    
    
 

pygame.quit()