import object
import button
import text
import assetLoader
import presets

def ButtonPress(obj):
    ask = input("WRITE: ")
    obj.getChildByName("score").set_text(ask)
    obj.move(0,25)
    

def startGame(pygame):


    start_button = button.Button(
    name="start",
    surface=assetLoader.images["Apostasy_Logo"],
    position=(presets.VIRTUAL_WIDTH/2-100,presets.VIRTUAL_HEIGHT/2 ),
    on_click=ButtonPress,
    base_scale=4
    )

    font = pygame.font.Font(None, 48)

    score_text = text.TextObject(
        name="score",
        text="Score: 0",
        font=font,
        color=(255, 255, 255),
        position=(presets.VIRTUAL_WIDTH/2-100, 50)
    )

    score_text.set_text("Welcome to play")
    score_text.set_color((255, 200, 50))
    score_text.set_scale(0.3)
    score_text.set_opacity(180)
    
    start_button.add_child(score_text, (-100,-50))
    
    object.objectManager.add(start_button)
    
    

def updateGame(pygame, dt):
    object.objectManager.update(dt)
    
    
    
    
    
    
