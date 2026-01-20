import object
import button
import text
import assetLoader
import presets
import pygame
import math
import region
import upgrades
import random

#PÄÄ PELI CLASSI
class Game():
    def __init__(
        self,
        game_state
    ):
        self.game_state = game_state
        self.mouse_free = True
        self.cliked_region = None
        
        self.soul_count = 100
                
        self.regions = {"Europe" : region.Region("Europe", "W"),
                        "Ru" : region.Region("Ru", "W"),
                        "Asia" : region.Region("Asia", "SE"),
                        "Eafr" : region.Region("Eafr", "W"),
                        "Islam" : region.Region("Islam", "SE"),
                        "Pam" : region.Region("Pam", "W"),
                        "Eam" : region.Region("Eam", "W"),
                        "Oce" : region.Region("Oce", "W"),}
        
        self.upgrades = {"Demon" : upgrades.Upgrade("Demon", 400),
                         "Internet" : upgrades.Upgrade("Internet", 400),
                         "Education" : upgrades.Upgrade("Education", 400),
                         "Persecution" : upgrades.Upgrade("Persecution", 400),}
        
        
    def getGlobalCorruption(self):
        total = 0
        for region in self.regions:
            total += self.regions[region].get_percent()
        return round(100 - total / len(self.regions),2)


global game    
global mouse_pos
        
def Soul_Count_Update(obj, dt):
    obj.set_text(f"SOULS: {game.soul_count}")
    obj.set_color((0,40 + 40*math.sin(0.002 * obj.time_alive),255))
    obj.set_opacity(180+80*math.sin(0.002 * obj.time_alive))
    
    

def Region_Click(obj):
    if game.mouse_free == False:
        game.cliked_region = obj.name
    else:
        game.game_state = f"REGION_INFO_STATE: {obj.name}"
        game.mouse_free = False
        backg = object.GameObject("Codex", assetLoader.images["CODEX_BACKG"], (0,0), None)
        backg.center()
        backg.scale(8)
        
        object.objectManager.add(backg)

def Region_Update(obj, dt):
    
    if obj.is_hovered:
        obj.set_scale(3 + min(obj.hover_time/4000,0.01))
        if obj.hover_time/1000 >= 0.5 and game.mouse_free:
            if not object.objectManager.hasObjectByName(f"{obj.name}info_square"):
                Square_Icon = object.GameObject(name=f"{obj.name}info_square", surface=assetLoader.images["Square"], position =(0,0))
                Square_Icon.hide()
                Square_Icon.scale(2)
                Square_Icon.set_opacity(100)
                
                if obj.name == "Europe":
                    content = "EUROPE"
                elif obj.name == "Asia":
                    content = "ASIA"
                elif obj.name == "Ru":
                    content = "RUSSIA"
                elif obj.name == "Islam":
                    content = "ISLAMIC REGION"
                elif obj.name == "Oce":
                    content = "OCEANIA"
                elif obj.name == "Eam":
                    content = "S AMERICA"
                elif obj.name == "Eafr":
                    content = "AFRICA"
                elif obj.name == "Pam":
                    content = "N AMERICA"
                    
                
                Text = text.TextObject("info_text", content, presets.main_font, (255,255,255), (0,0), False)
                Text.scale(0.50)
                
                Text_Data = text.TextObject("data_text", f"CORRUPTION", presets.main_font, (255,0,20), (0,0), False)
                Square_Icon.add_child(Text_Data)
                Text_Data.scale(0.13)
                Text_Data.center()
                Text_Data.move(-45,-30)
                
                Text_Infamy = text.TextObject("infamy_text", f"INFAMY", presets.main_font, (214, 214, 34), (0,0), False)
                Square_Icon.add_child(Text_Infamy)
                Text_Infamy.scale(0.13)
                Text_Infamy.center()
                Text_Infamy.move(-45,5)
                
                Pent_Icon = object.GameObject("Pentagram", assetLoader.images["allah"], (0,0), None)
                Square_Icon.add_child(Pent_Icon)
                Pent_Icon.scale(0.02)
                Pent_Icon.center()
                Pent_Icon.move(-91,-32)
                
                Square_Icon.add_child(Text)
                Text.center()
                Text.move(0,-60)
                object.objectManager.add(Square_Icon)
            else:
                info_obj = object.objectManager.getObjectByName(f"{obj.name}info_square")
                info_obj.set_position(mouse_pos[0]-55, mouse_pos[1]-10)
                info_obj.show()

                Data_text = info_obj.getChildByName("data_text")
                Data_text.set_text(f"CORRUPTION {round(100-game.regions[obj.name].get_percent())} %")
                
                Data_text = info_obj.getChildByName("infamy_text")
                Data_text.set_text(f"INFAMY {round(game.regions[obj.name].get_infamy())} %")
        
    else:
        obj.base_scale = 3
        if obj.hover_quit:
            obj.set_scale(3)
            
            if object.objectManager.hasObjectByName(f"{obj.name}info_square"):
                info_obj = object.objectManager.getObjectByName(f"{obj.name}info_square")
                info_obj.destroy()
 
def Global_Corruption_Text_Update(obj, dt):
    obj.set_text(f"GLOBAL CORRUPTION: {game.getGlobalCorruption()}%")
    obj.set_color((100 + 20*math.sin(0.002 * obj.time_alive),10,40))
    obj.set_opacity(180+10*math.sin(0.002 * obj.time_alive))
    


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
    
    Corruption_meter = object.GameObject("Corruption_Meter", assetLoader.images["corruption"], (200,0))
    Corruption_meter.scale(0.5)
    Corruption_meter.center()
    Corruption_meter.move(0,-350)
    
    Corruption_Text  = text.TextObject("Corruption_Text", "", presets.main_font, (255,10,0), (0,0))
    Corruption_Text.set_text(f"GLOBAL CORRUPTION: {game.getGlobalCorruption()}%")
    Corruption_Text.updateLoop = Global_Corruption_Text_Update
    
    
    Corruption_meter.add_child(Corruption_Text)
    
    Corruption_Text.scale(2.5)
    Corruption_Text.center()
    Corruption_Text.move(210,-5)
    
    object.objectManager.add(Corruption_meter)
    
    
    Europe_Icon = button.Button(name="Europe",
    surface=assetLoader.images["EUR2"],
    position=(presets.VIRTUAL_WIDTH/2-100,presets.VIRTUAL_HEIGHT/2 ),
    on_click=Region_Click,
    base_scale=0.8,
    accurate_hit=True,
    hover_anim=False)
    
    Europe_Icon.updateLoop = Region_Update
    Europe_Icon.center()
    
    Ru_Icon = button.Button(name="Ru",
    surface=assetLoader.images["RU2"],
    position=(presets.VIRTUAL_WIDTH/2-100,presets.VIRTUAL_HEIGHT/2 ),
    on_click=Region_Click,
    base_scale=0.8,
    accurate_hit=True,
    hover_anim=False)
    
    Ru_Icon.center()
    Ru_Icon.updateLoop = Region_Update
    
    Asia_Icon = button.Button(name="Asia",
    surface=assetLoader.images["ASIA2"],
    position=(presets.VIRTUAL_WIDTH/2-100,presets.VIRTUAL_HEIGHT/2 ),
    on_click=Region_Click,
    base_scale=0.8,
    accurate_hit=True,
    hover_anim=False)
    
    Asia_Icon.center()
    Asia_Icon.updateLoop = Region_Update
    
    Islam_Icon = button.Button(name="Islam",
    surface=assetLoader.images["ISLAM2"],
    position=(presets.VIRTUAL_WIDTH/2-100,presets.VIRTUAL_HEIGHT/2 ),
    on_click=Region_Click,
    base_scale=0.8,
    accurate_hit=True,
    hover_anim=False)
    
    Islam_Icon.center()
    Islam_Icon.updateLoop = Region_Update
    
    Oce_Icon = button.Button(name="Oce",
    surface=assetLoader.images["OCE2"],
    position=(presets.VIRTUAL_WIDTH/2-100,presets.VIRTUAL_HEIGHT/2 ),
    on_click=Region_Click,
    base_scale=0.8,
    accurate_hit=True,
    hover_anim=False)
    
    Oce_Icon.center()
    Oce_Icon.updateLoop = Region_Update
    
    Eam_Icon = button.Button(name="Eam",
    surface=assetLoader.images["EAM2"],
    position=(presets.VIRTUAL_WIDTH/2-100,presets.VIRTUAL_HEIGHT/2 ),
    on_click=Region_Click,
    base_scale=0.8,
    accurate_hit=True,
    hover_anim=False)
    
    Eam_Icon.center()
    Eam_Icon.updateLoop = Region_Update
    
    Eafr_Icon = button.Button(name="Eafr",
    surface=assetLoader.images["AFR2"],
    position=(presets.VIRTUAL_WIDTH/2-100,presets.VIRTUAL_HEIGHT/2 ),
    on_click=Region_Click,
    base_scale=0.8,
    accurate_hit=True,
    hover_anim=False)
    
    Eafr_Icon.center()
    Eafr_Icon.updateLoop = Region_Update
    
    Pam_Icon = button.Button(name="Pam",
    surface=assetLoader.images["PAM2"],
    position=(presets.VIRTUAL_WIDTH/2-100,presets.VIRTUAL_HEIGHT/2 ),
    on_click=Region_Click,
    base_scale=0.8,
    accurate_hit=True,
    hover_anim=False)
    
    Pam_Icon.center()
    Pam_Icon.updateLoop = Region_Update
    
    
    object.objectManager.add(Europe_Icon)
    object.objectManager.add(Ru_Icon)
    object.objectManager.add(Asia_Icon)
    object.objectManager.add(Islam_Icon)
    object.objectManager.add(Oce_Icon)
    object.objectManager.add(Eam_Icon)
    object.objectManager.add(Eafr_Icon)
    object.objectManager.add(Pam_Icon)
   
def Dem_Temple_Update(obj, dt):
    
    if obj.time_alive >= 3000:
        obj.time_alive = 0
        my_region = game.regions[obj.name[15:]]
    
        game.soul_count += my_region.reduce() 
        my_region.add_infamy(1/6)
   
   
 
def Dem_Temple_Start(obj, dt):
    obj.set_position(mouse_pos[0]-30, mouse_pos[1]-20)
    
    if game.cliked_region != None:
        obj.name = f"Demonic_Temple_{game.cliked_region}"
        print(f"Created temple in {game.cliked_region}")
        game.cliked_region = None
        game.mouse_free = True
        obj.updateLoop = Dem_Temple_Update
    

def Hellfire_Update(obj, dt):
    obj.set_opacity(max(0,-0.7*(obj.time_alive/10)**2+obj.time_alive*3))
    
    if(obj.opacity == 0):
        obj.destroy()
        
    for church in object.objectManager.getObjectsListByName("Holy_Church"):
        if obj.collides_with(church):
            church.destroy()

def Church_Update(obj, dt):
    if obj.time_alive >= 3000:
        obj.time_alive = 0
        my_region = game.regions[obj.name[11:]]
    
        my_region.cure()
        
    
    
    

def startGame(pygame):
    global game
    game = Game("start_screen")
    
    start_button = button.Button(name="start",
    surface=assetLoader.images["Apostasy_Logo"],
    position=(presets.VIRTUAL_WIDTH/2-100,presets.VIRTUAL_HEIGHT/2 ),
    on_click=Start_Pressed,
    base_scale=4)
    start_button.center()
    
    Jesus_art = object.GameObject("JesusArt",surface=assetLoader.images["game_main_title_pic2"],position=(0,0 ) )
    Jesus_art.set_scale(0.465)
    Jesus_art.center()
    Jesus_art.move(0,-40)
    
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
    
def map_update():
    for region in game.regions:
            if game.regions[region].changed_percent:
                game.regions[region].changed_percent = False
                obj = object.objectManager.getObjectByName(region)
                
                obj.set_hue(150-1.5*game.regions[region].get_percent())

    


def inputEvent(event):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_e and game.mouse_free and game.soul_count >= 100:
            game.soul_count -= 100
            print("Added Tempke")
            game.mouse_free = False
            Temple = object.GameObject("Demonic_Temple", assetLoader.images["Demonic_Temple"], (0,0), Dem_Temple_Start)
            Temple.scale(1)
            Temple.set_position(mouse_pos[0]-30, mouse_pos[1]-20)
            
            object.objectManager.add(Temple)
            
        if event.key == pygame.K_ESCAPE and "REGION_INFO_STATE:" in game.game_state:
            game.game_state = "game"
            game.mouse_free = True
            
            codex = object.objectManager.getObjectByName("Codex")
            codex.destroy()
            
        if event.key == pygame.K_q and game.mouse_free:
            game.game_state = "shop"
            game.mouse_free = False
            
            shop_backg = object.GameObject("shop_backg", assetLoader.images["shop_backg"], (0,0))
            shop_backg.scale(6.7)
            shop_backg.center()
            
            object.objectManager.add(shop_backg)
            
            Demonic = object.GameObject("Demonic_Upgrade", assetLoader.images["demonic_p"], (0,0), None)
            Demonic.scale(0.1)
            
            shop_backg.add_child(Demonic)
            
            
            
        if event.key == pygame.K_ESCAPE and game.game_state == "shop":
            game.game_state = "game"
            game.mouse_free = True
            
            shop = object.objectManager.getObjectByName("shop_backg")
            shop.destroy()
            
    #Hellfire
        
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3 and game.soul_count >= 20:
        game.soul_count -= 20
        hellfire = object.GameObject("Hellfire", assetLoader.images["hellfire"],(0,0),Hellfire_Update)
        hellfire.scale(1)
        hellfire.set_position(mouse_pos[0]-30,mouse_pos[1]-30)
        hellfire.set_opacity(0)
        object.objectManager.add(hellfire)
            
            

global tick_timer   
tick_timer = 100000000000000

global map_upd_timer
map_upd_timer = 10000000

def updateGame(pygame, dt):
    global game
    global mouse_pos
    global tick_timer
    global map_upd_timer
    
    mouse_pos = presets.get_mouse_pos_virtual(pygame.display.get_surface())
    
    if(map_upd_timer >= 1/1 * 1000):  #Map update 1 per sec
        map_update()
        map_upd_timer = 0
    else:
        map_upd_timer += dt
    
    
    if(tick_timer >= 1/10 * 1000):  #Game update 10 per sec
        object.objectManager.update(tick_timer)
        update_region_stats()
        tick_timer = 0
    else:
        tick_timer += dt

random.seed()

def update_region_stats():

    for region in game.regions:
        if game.regions[region].get_type() == "SE":           #Asia ja Islam
            game.regions[region].effectiveness = 1 + game.upgrades["Internet"].get_level() + game.upgrades["Persecution"].get_level()
            game.regions[region].foulness = 1 + game.upgrades["Demon"].get_level() + game.upgrades["Persecution"].get_level()
            
        elif game.regions[region].get_type == "W":            #Europe, Ru, Eafr, Pam, Eam ja Oce
            game.regions[region].effectiveness = 1 + game.upgrades["Internet"].get_level() + game.upgrades["Education"].get_level()
            game.regions[region].foulness = 1 + game.upgrades["Demon"].get_level() + game.upgrades["Education"].get_level()
        else:                                   #Varalta ettei peli hajoa jos unohtu laittaa type
            game.regions[region].effectiveness = 1 + game.upgrades["Internet"].get_level()
            game.regions[region].foulness = 1 + game.upgrades["Demon"].get_level()
        #Kirkko random spawn
        
        if game.regions[region].percent != 100:
            if random.random() >= 1-math.log(20*game.regions[region].infamy+1)/600:
                print("added church")
                church = object.GameObject(f"Holy_Church{region}", assetLoader.images["Holy_Church"], (0,0), Church_Update)
                
                region_obj = object.objectManager.getObjectByName(region)
                object.objectManager.add(church)
                
                church.scale(0.1)
                church.center()
                church.move(random.randint(-400,400),random.randint(-400,400))
                while not church.collides_with_mask(region_obj):
                    church.center()
                    church.move(random.randint(-400,400),random.randint(-400,400))
                church.scale(10)
                    
            
        
    
    
    
    
    
    
    
