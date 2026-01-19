import object

def renderScreen(pygame, game_surface, screen):
    game_surface.fill((10, 10, 10))  # background

    object.objectManager.draw(game_surface)
        
    
    window_width, window_height = screen.get_size()

    scaled_surface = pygame.transform.scale(game_surface,(window_width, window_height))

    screen.blit(scaled_surface, (0, 0))
    pygame.display.flip()
   
    
   