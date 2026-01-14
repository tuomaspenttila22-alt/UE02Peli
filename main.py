import pygame
import renderer
import game

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Apostasy v.1.0")


#INITS
renderer.initRenderer(pygame)

clock = pygame.time.Clock()
running = True

while running:
    # 1. Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            print(event.key)
        
     

    # 2. Update game state
    game.updateGame()
    
    # 3. Draw
    renderer.renderScreen(screen, pygame)


    # 4. Timing
    clock.tick(60)

pygame.quit()