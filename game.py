import object
import button
import text
import assetLoader
import presets
import pygame
import math

class Game():
    def __init__(
        self,
        game_state
    ):
        self.game_state = game_state
        self.soul_count = 100
        

global game    
        
def Soul_Count_Update(obj):
    obj.set_text(f"SOULS: {game.soul_count}")
    obj.set_color((0,40 + 40*math.sin(0.002 * obj.time_alive),255))
    obj.set_opacity(180+80*math.sin(0.002 * obj.time_alive))
    
    game.soul_count += 1



def Start_Pressed(obj):
    
    object.objectManager.clearObjects()
    
    game.game_state = "game"
    
    Soul_Count = object.GameObject(name="soul_count", surface=assetLoader.images["soul_better"], position=(0,0))
    Soul_Count.scale(0.25)
    Soul_Count.to_top_left()
    Soul_Count.move(-40,-30)
    
    
    
    Soul_Count_text = text.TextObject(
        name="soul_count_score",
        text="0",
        font=presets.main_font,
        color=(0, 10, 255),
        position=(0,0))
    
    
    Soul_Count_text.set_text(f"SOULS: {game.soul_count}")
    Soul_Count_text.updateLoop = Soul_Count_Update
    
    Soul_Count.add_child(Soul_Count_text, (0,0))
    Soul_Count_text.set_scale(2.3)
    Soul_Count_text.set_opacity(180)
    Soul_Count_text.move(105,63.5)
    
    object.objectManager.add(Soul_Count)
    
    

def startGame(pygame):
    global game
    game = Game("start_screen")
    
    start_button = button.Button(name="start",
    surface=assetLoader.images["Apostasy_Logo"],
    position=(presets.VIRTUAL_WIDTH/2-100,presets.VIRTUAL_HEIGHT/2 ),
    on_click=Start_Pressed,
    base_scale=4)
    start_button.center()
    
    Jesus_art = object.GameObject("JesusArt",surface=assetLoader.images["Jesus"],position=(0,0 ) )
    Jesus_art.set_scale(0.25)
    Jesus_art.center()
    
    score_text = text.TextObject(
        name="score",
        text="Score: 0",
        font=presets.main_font,
        color=(255, 255, 255),
        position=(presets.VIRTUAL_WIDTH/2-100, 50))

    score_text.set_text("Welcome to play")
    score_text.set_color((255, 200, 50))
    score_text.set_scale(0.3)
    score_text.set_opacity(180)
    
    start_button.add_child(score_text, (-50,-70))
    score_text.center()
    score_text.move(0,-50)
    
    object.objectManager.add(Jesus_art)
    object.objectManager.add(start_button)
    
    
    

def updateGame(pygame, dt):
    global game
    object.objectManager.update(dt)
    
    
    
    
    
    
    
