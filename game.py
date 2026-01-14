import object
import assetLoader
import presets


def startGame(pygame, ObjectManager):
    main_title = object.GameObject("Title", assetLoader.images["Apostasy_Logo"], (presets.VIRTUAL_HEIGHT/2,presets.VIRTUAL_WIDTH/2 ))
    main_title.scale(3)
    ObjectManager.add(main_title)
    
    


def updateGame(pygame, ObjectManager):
    ObjectManager.update(0)
    
    
    
