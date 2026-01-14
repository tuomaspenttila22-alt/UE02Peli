

def renderScreen(pygame, game_surface, screen,  ObjectManager):
    screen.fill((30, 30, 30))  # background

    ObjectManager.draw(game_surface)
        
    
    window_width, window_height = screen.get_size()

    scaled_surface = pygame.transform.scale(game_surface,(window_width, window_height))

    screen.blit(scaled_surface, (0, 0))
    pygame.display.flip()
   
    
   