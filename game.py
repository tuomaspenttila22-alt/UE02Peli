import object
import button
import assetLoader
import presets

def ButtonPress():
    print("Button Clicked")

def startGame(pygame, ObjectManager):


    start_button = button.Button(
    name="start",
    surface=assetLoader.images["Apostasy_Logo"],
    position=(presets.VIRTUAL_HEIGHT/2,presets.VIRTUAL_WIDTH/2 ),
    on_click=ButtonPress,
    base_scale=4
    )

    ObjectManager.add(start_button)
    



def updateGame(pygame, ObjectManager, dt):
    ObjectManager.update(dt)
    
    
    
    
    
    
