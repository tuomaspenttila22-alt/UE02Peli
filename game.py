import object
import button
import assetLoader
import presets


def startGame(pygame, ObjectManager):
   # main_title = object.GameObject("Main_Title", assetLoader.images["Apostasy_Logo"], (presets.VIRTUAL_HEIGHT/2,presets.VIRTUAL_WIDTH/2 ))
    #main_title.scale(3)
    
    
    #ObjectManager.add(main_title)
    
    start_button = button.Button(
    name="start",
    surface=assetLoader.images["Apostasy_Logo"],
    position=(presets.VIRTUAL_HEIGHT/2,presets.VIRTUAL_WIDTH/2 ),
    on_click=start_game
)
    


def updateGame(pygame, ObjectManager, dt):
    ObjectManager.update(dt)
    
    
    
    
    
    
