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

def Region_Update(obj):
    if obj.is_hovered:
        pass


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
    
    Europe_Icon = button.Button(name="Europe",
    surface=assetLoader.images["eur"],
    position=(presets.VIRTUAL_WIDTH/2-100,presets.VIRTUAL_HEIGHT/2 ),
    on_click=None,
    base_scale=0.8,
    accurate_hit=True,
    hover_anim=False)
    
    Europe_Icon.updateLoop = Region_Update
    Europe_Icon.center()
    
    Ru_Icon = button.Button(name="Ru",
    surface=assetLoader.images["ru"],
    position=(presets.VIRTUAL_WIDTH/2-100,presets.VIRTUAL_HEIGHT/2 ),
    on_click=None,
    base_scale=0.8,
    accurate_hit=True,
    hover_anim=False)
    
    Ru_Icon.center()
    
    Asia_Icon = button.Button(name="Asia",
    surface=assetLoader.images["asia"],
    position=(presets.VIRTUAL_WIDTH/2-100,presets.VIRTUAL_HEIGHT/2 ),
    on_click=None,
    base_scale=0.8,
    accurate_hit=True,
    hover_anim=False)
    
    Asia_Icon.center()
    
    Islam_Icon = button.Button(name="Islam",
    surface=assetLoader.images["islam"],
    position=(presets.VIRTUAL_WIDTH/2-100,presets.VIRTUAL_HEIGHT/2 ),
    on_click=None,
    base_scale=0.8,
    accurate_hit=True,
    hover_anim=False)
    
    Islam_Icon.center()
    
    Oce_Icon = button.Button(name="Oce",
    surface=assetLoader.images["oce"],
    position=(presets.VIRTUAL_WIDTH/2-100,presets.VIRTUAL_HEIGHT/2 ),
    on_click=None,
    base_scale=0.8,
    accurate_hit=True,
    hover_anim=False)
    
    Oce_Icon.center()
    
    Eam_Icon = button.Button(name="Eam",
    surface=assetLoader.images["eam"],
    position=(presets.VIRTUAL_WIDTH/2-100,presets.VIRTUAL_HEIGHT/2 ),
    on_click=None,
    base_scale=0.8,
    accurate_hit=True,
    hover_anim=False)
    
    Eam_Icon.center()
   
    Eafr_Icon = button.Button(name="Eafr",
    surface=assetLoader.images["eafr"],
    position=(presets.VIRTUAL_WIDTH/2-100,presets.VIRTUAL_HEIGHT/2 ),
    on_click=None,
    base_scale=0.8,
    accurate_hit=True,
    hover_anim=False)
    
    Eafr_Icon.center()
    
    Pam_Icon = button.Button(name="Pam",
    surface=assetLoader.images["pam"],
    position=(presets.VIRTUAL_WIDTH/2-100,presets.VIRTUAL_HEIGHT/2 ),
    on_click=None,
    base_scale=0.8,
    accurate_hit=True,
    hover_anim=False)
    
    Pam_Icon.center()
    
    
    object.objectManager.add(Europe_Icon)
    object.objectManager.add(Ru_Icon)
    object.objectManager.add(Asia_Icon)
    object.objectManager.add(Islam_Icon)
    #object.objectManager.add(Oce_Icon)
    #object.objectManager.add(Eam_Icon)
    #object.objectManager.add(Eafr_Icon)
    #object.objectManager.add(Pam_Icon)
    
    
    
    
    

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
    object.objectManager.add(start_button)
    object.objectManager.add(start_button)
    object.objectManager.add(start_button)
    
    
    

def updateGame(pygame, dt):
    global game
    object.objectManager.update(dt)
    
    
    
    
    
    
    
