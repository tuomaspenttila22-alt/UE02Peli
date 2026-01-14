
import assetLoader


global images

def initRenderer(pygame):
    global images
    images = assetLoader.load_pngs("assets/images", pygame)
    print(len(images))
    


def renderScreen(screen, pygame):
    screen.fill((30, 30, 30))  # background
    
    pygame.draw.rect(screen, (255, 0, 0), (10, 10, 100, 200))
    
    pygame.display.flip()
    print(len(images))
    
   