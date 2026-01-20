import object
import math
import game

def renderScreen(pygame, game_surface, screen, clock):
    game_surface.fill((10+game.game.getGlobalCorruption()*245/100, 0, 0))  # background

    object.objectManager.draw(game_surface)
        
    
    window_width, window_height = screen.get_size()

    scaled_surface = pygame.transform.scale(game_surface,(window_width, window_height))

    screen.blit(scaled_surface, (0, 0))
    pygame.display.flip()
   
    
   