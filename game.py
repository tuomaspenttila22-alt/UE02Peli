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
import news
import codex

#PÄÄ PELI CLASSI
class Game():
    def __init__(
        self,
        game_state,
        playtime_in_mins = 5
    ):
        self.game_state = game_state
        self.mouse_free = True
        self.cliked_region = None
        
        self.playtime_in_mins = playtime_in_mins
        self.time_left = 365
        self.time_left_raw = playtime_in_mins * 60 * 1000  
        
        self.first_church = False
        self.church_region = None
        
        self.soul_count = 15000000
        self.game_time = 0
                
        self.regions = {"Europe" : region.Region("Europe", "W"),
                        "Ru" : region.Region("Ru", "W"),
                        "Asia" : region.Region("Asia", "SE"),
                        "Eafr" : region.Region("Eafr", "W"),
                        "Islam" : region.Region("Islam", "SE"),
                        "Pam" : region.Region("Pam", "W"),
                        "Eam" : region.Region("Eam", "W"),
                        "Oce" : region.Region("Oce", "W")}
        
        self.upgrades = {"Demon" : upgrades.Upgrade("Demon", 400),
                         "Internet" : upgrades.Upgrade("Internet", 400),
                         "Education" : upgrades.Upgrade("Education", 400),
                         "Persecution" : upgrades.Upgrade("Persecution", 400),}
        
        
    def getGlobalCorruption(self):
        total = 0
        for region in self.regions:
            total += self.regions[region].get_percent()
        return round(100 - total / len(self.regions),2)
    
    def getGlobalInfamy(self):
        total = 0
        for region in self.regions:
            total += self.regions[region].get_infamy()
        return round(total / len(self.regions))
    
    
    def reset_timer(self):
        self.time_left = 365
        self.time_left_raw = self.playtime_in_mins * 60 * 1000  
    
    def updateTime(self, dt):
        self.time_left_raw -= dt
        self.time_left = round(365*self.time_left_raw/1000/60/self.playtime_in_mins)
        self.game_time += dt


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
        
        pent = object.GameObject("Pent", assetLoader.images["allah"], (0,0))
        backg.add_child(pent)
        pent.scale(0.005)
        pent.center()
        pent.move(-50,260)
        
        codex.CreateCodexText(backg, obj.name)
        
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
    
def Time_Left_Update(obj, dt):
    obj.set_text(f"TIME LEFT: {game.time_left} d")
    obj.set_color((30,200+20*math.sin(0.002 * obj.time_alive),80))
    obj.set_opacity(180+10*math.sin(0.002 * obj.time_alive))

def Start_Pressed(obj):
    global game
    game = Game("game")
    game.reset_timer()
    object.objectManager.clearObjects()
    
    game.game_state = "game"
    
    Hotbar = object.GameObject("Hot", assetLoader.images["Hotbar"], (0,0), None)
    Hotbar.scale(0.95)
    Hotbar.center()
    Hotbar.move(-230,285)
    
    object.objectManager.add(Hotbar)
    
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
    Corruption_meter.move(-20,-350)
    

    Corruption_Text  = text.TextObject("Corruption_Text", "", presets.main_font, (255,10,0), (0,0))
    Corruption_Text.set_text(f"GLOBAL CORRUPTION: {game.getGlobalCorruption()}%")
    Corruption_Text.updateLoop = Global_Corruption_Text_Update
    
    
    Corruption_meter.add_child(Corruption_Text)
    
    Corruption_Text.scale(2.5)
    Corruption_Text.center()
    Corruption_Text.move(210,-5)
    
    object.objectManager.add(Corruption_meter)
    
    Time_meter = object.GameObject("Time_meter", assetLoader.images["time"], (200,0))
    Time_meter.scale(0.28)
    Time_meter.center()
    Time_meter.move(280,-350)
    
    Time_meter_text  = text.TextObject("Time_meter_text", "KAKAKA", presets.main_font, (255,10,0), (0,0))
    Time_meter_text.set_text(f"TIME LEFT: {game.time_left} d")
    Time_meter_text.updateLoop = Time_Left_Update
    
    
    Time_meter.add_child(Time_meter_text)
    
    Time_meter_text.scale(5.5)
    Time_meter_text.center()
    Time_meter_text.move(170,10)
    
    object.objectManager.add(Time_meter)
    
    
    
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
    if game.game_state == "game":
        if obj.time_alive >= 3000:
            obj.time_alive = 0
            my_region = game.regions[obj.name[15:]]
    
            if "Demonic" in obj.name:
                game.soul_count += my_region.reduce(1)
                my_region.add_infamy(1/2)
            else:
                game.soul_count += my_region.reduce(13)
                my_region.add_infamy(5)
            
            
           
    else:
        obj.time_alive -= dt
   
   
 
def Dem_Temple_Start(obj, dt):
    if "Demonic" in obj.name:
        obj.set_position(mouse_pos[0]-30, mouse_pos[1]-20)
    else:
        obj.set_position(mouse_pos[0]-60, mouse_pos[1]-40)
    
    if game.cliked_region != None:
        obj.name = f"{obj.name}_{game.cliked_region}"
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

    for church in object.objectManager.getObjectsListByName("BIGG_Church"):
        if obj.collides_with(church):
            church.destroy()

def Church_Update(obj, dt):
    if game.game_state == "game":
        if obj.time_alive >= 3000:
            obj.time_alive = 0
            my_region = game.regions[obj.name[11:]]

            if("BIGG" in obj.name):
                my_region.cure(5)
    else:
        obj.time_alive -= dt
        
def Upgrade_Click(obj):
    game.soul_count -= game.upgrades[obj.name].level_up(game.soul_count)
    
    cost = game.upgrades[obj.name].get_cost()
    lv = game.upgrades[obj.name].get_level()
    info = obj.getChildByName("INFO")
    
    info.set_text(f"Level {lv}\\{cost} souls")
    if game.upgrades[obj.name].level == 4:
        info.set_text("MAX LEVEL")
        
        if obj.name == "Demon":
            info.set_text("MAX LEVEL\\ \\BONUS:\\Bigger hellfire")
        


global tick_timer   
tick_timer = 100000000000000

global map_upd_timer
map_upd_timer = 10000000   
    
    

def startGame(pygame):
    global game
    game = Game("start_screen")
    
    global tick_timer   
    tick_timer = 100000000000000

    global map_upd_timer
    map_upd_timer = 10000000   
    
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
        if event.key == pygame.K_1 and game.mouse_free and game.soul_count >= 100:
            game.soul_count -= 100
            print("Added Tempke")
            game.mouse_free = False
            Temple = object.GameObject("Demonic_Temple", assetLoader.images["Demonic_Temple"], (0,0), Dem_Temple_Start)
            Temple.scale(1)
            Temple.set_position(mouse_pos[0]-30, mouse_pos[1]-20)
            
            object.objectManager.add(Temple)

        if event.key == pygame.K_2 and game.mouse_free and game.soul_count >= 1000:
            game.soul_count -= 1000
            print("Added Huge Temple")
            game.mouse_free = False
            Temple = object.GameObject("Hellish_Temple", assetLoader.images["Demonic_Temple"], (0,0), Dem_Temple_Start)
            Temple.scale(2)
            Temple.set_hue(100)
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
            Demonic.center()
            Demonic.move(-250,0)
            
            Demonic_info = text.TextObject("INFO", "Demonic Activity:\\Increases foulness\\globally", presets.main_font, (255,255,255))
            
            Demonic.add_child(Demonic_info)
            Demonic_info.scale(0.77)
            Demonic_info.center()
            Demonic_info.move(40,-180)
            
            Demonic_upg = button.Button("Demon", assetLoader.images["Play_Again"], (0,0), Upgrade_Click, 2.8, False, False)
            
            Demonic_upg.center()
            Demonic_upg.move(-245,200)
            
            cost = game.upgrades["Demon"].get_cost()
            lv = game.upgrades["Demon"].get_level()
            Demonic_upg_text = text.TextObject("INFO", f"Level {lv}\\{cost} souls", presets.main_font, (255,255,255))
            
            
            Demonic_upg.add_child(Demonic_upg_text)
            
            Demonic_upg_text.scale(0.18)
            Demonic_upg_text.center()
            Demonic_upg_text.move(0,0)
            if game.upgrades["Demon"].level == 4:
                Demonic_upg_text.set_text("MAX LEVEL\\ \\BONUS:\\Bigger hellfire")
            
            object.objectManager.add(Demonic_upg)
            
            
            Internet = object.GameObject("Internet_Upgrade", assetLoader.images["internet_a"], (0,0), None)
            Internet.scale(0.1)
            
            
            shop_backg.add_child(Internet)
            Internet.center()
            Internet.move(-100,0)
            
            Internet_info = text.TextObject("INFO", "Interner Acces:\\Increases effectivness\\globally", presets.main_font, (255,255,255))
            
            Internet.add_child(Internet_info)
            Internet_info.scale(0.77)
            Internet_info.center()
            Internet_info.move(60,-180)
            
            Internet_upg = button.Button("Internet", assetLoader.images["Play_Again"], (0,0), Upgrade_Click, 2.8, False, False)
            
            Internet_upg.center()
            Internet_upg.move(-100,200)
            
            cost = game.upgrades["Internet"].get_cost()
            lv = game.upgrades["Internet"].get_level()
            Internet_upg_text = text.TextObject("INFO", f"Level {lv}\\{cost} souls", presets.main_font, (255,255,255))
            if game.upgrades["Internet"].level == 4:
                Internet_upg_text.set_text("MAX LEVEL")
            
            Internet_upg.add_child(Internet_upg_text)
            
            Internet_upg_text.scale(0.18)
            Internet_upg_text.center()
            Internet_upg_text.move(0,0)
            
            object.objectManager.add(Internet_upg)
            
            Material = object.GameObject("Material_Upgrade", assetLoader.images["Material"], (0,0), None)
            Material.scale(0.1)
            
            
            shop_backg.add_child(Material)
            Material.center()
            Material.move(45,0)
            
            Material_info = text.TextObject("INFO", "Material teachings:\\Increases effectivness\\and foulness", presets.main_font, (255,255,255))
            
            Material.add_child(Material_info)
            Material_info.scale(0.77)
            Material_info.center()
            Material_info.move(60,-180)
            
            Material_upg = button.Button("Education", assetLoader.images["Play_Again"], (0,0), Upgrade_Click, 2.8, False, False)
            
            Material_upg.center()
            Material_upg.move(45,200)
            
            cost = game.upgrades["Education"].get_cost()
            lv = game.upgrades["Education"].get_level()
            Material_upg_text = text.TextObject("INFO", f"Level {lv}\\{cost} souls", presets.main_font, (255,255,255))
            if game.upgrades["Education"].level == 4:
                Material_upg_text.set_text("MAX LEVEL")
            
            Material_upg.add_child(Material_upg_text)
            
            Material_upg_text.scale(0.18)
            Material_upg_text.center()
            Material_upg_text.move(0,0)
            
            object.objectManager.add(Material_upg)
            
            Persp = object.GameObject("Persp_Upgrade", assetLoader.images["Persecution"], (0,0), None)
            Persp.scale(0.1)
            
            
            shop_backg.add_child(Persp)
            Persp.center()
            Persp.move(190,0)
            
            Persp_info = text.TextObject("INFO", "Persecution:\\Increases effectivness\\and foulness", presets.main_font, (255,255,255))
            
            Persp.add_child(Persp_info)
            Persp_info.scale(0.77)
            Persp_info.center()
            Persp_info.move(60,-180)
            
            Persp_upg = button.Button("Persecution", assetLoader.images["Play_Again"], (0,0), Upgrade_Click, 2.8, False, False)
            
            Persp_upg.center()
            Persp_upg.move(190,200)
            
            cost = game.upgrades["Persecution"].get_cost()
            lv = game.upgrades["Persecution"].get_level()
            Persp_upg_text = text.TextObject("INFO", f"Level {lv}\\{cost} souls", presets.main_font, (255,255,255))
            if game.upgrades["Persecution"].level == 4:
                Persp_upg_text.set_text("MAX LEVEL")
            
            Persp_upg.add_child(Persp_upg_text)
            
            Persp_upg_text.scale(0.18)
            Persp_upg_text.center()
            Persp_upg_text.move(0,0)
            
            object.objectManager.add(Persp_upg)
            
            
            
        if event.key == pygame.K_ESCAPE and game.game_state == "shop":
            game.game_state = "game"
            game.mouse_free = True
            
            shop = object.objectManager.getObjectByName("shop_backg")
            shop.destroy()
            
            demon = object.objectManager.getObjectByName("Demon")
            demon.destroy()
            
            inter =object.objectManager.getObjectByName("Internet")
            inter.destroy()
            
            mater =object.objectManager.getObjectByName("Education")
            mater.destroy()
            
            persp =object.objectManager.getObjectByName("Persecution")
            persp.destroy()
            
        if event.key == pygame.K_ESCAPE and game.game_state == "news":
            game.game_state = "game"
            game.mouse_free = True
            
            news = object.objectManager.getObjectByName("News")
            news.destroy()
            
    #Hellfire
        
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3 and game.soul_count >= 20 and game.mouse_free:
        game.soul_count -= 20
        hellfire = object.GameObject("Hellfire", assetLoader.images["hellfire"],(0,0),Hellfire_Update)
        hellfire.scale(1)
        hellfire.set_position(mouse_pos[0]-30,mouse_pos[1]-30)
        if game.upgrades["Demon"].get_level() == 4:
            hellfire.scale(2)
            hellfire.set_hue(200)
        
            hellfire.move(10,10)
        hellfire.set_opacity(0)
        object.objectManager.add(hellfire)
            
            



def updateGame(pygame, dt):
    global game
    global mouse_pos
    global tick_timer
    global map_upd_timer
    
    mouse_pos = presets.get_mouse_pos_virtual(pygame.display.get_surface())
    
    if game.game_state == "game":
        game.updateTime(dt)
    
    if(map_upd_timer >= 3/1 * 1000) and game.game_state != "LOSS" and game.game_state != "WIN":  #Map update 0.5 per sec
        map_update()
        map_upd_timer = 0
    else:
        map_upd_timer += dt
    
    object.objectManager.update(tick_timer)
    news.UpdateNewsCycle(game)
    
    if(tick_timer >= 1/10 * 1000):  #Game update 10 per sec
        if game.game_state != "LOSS" and game.game_state != "WIN":
            update_region_stats()
        tick_timer = 0
    else:
        tick_timer += dt
      
      
    #Win Check
    
    if game.getGlobalCorruption() >= 100 and game.game_state != "WIN" and game.game_state != "LOSS":
        game.mouse_free = False
        game.game_state = "WIN"
        object.objectManager.clearObjects()
        
        Satan = object.GameObject("SATAN",assetLoader.images["game_main_title_pic2"],(0,0))
        Satan.scale(0.3)
        Satan.center()
        
        WinText = text.TextObject("Win_TEXT", "You corrupted the world, YOU WIN", presets.main_font, (255,255,255))
        
        Satan.add_child(WinText)
        WinText.scale(12)
        WinText.center()
        WinText.move(680,-200)
        
        Play_Icon = button.Button("Play_Agin", assetLoader.images["Play_Again"], (0,0), Start_Pressed, base_scale=5)
        
        Play_Icon.center()
        Play_Icon.move(0,200)
        
        Play_Agian = text.TextObject("PlayAgain", "TRY AGAIN?", presets.main_font, (250,0,50))
        
        Play_Icon.add_child(Play_Agian)
        Play_Agian.scale(0.2)
        Play_Agian.center()
        Play_Agian.move(20,17)
   
        object.objectManager.add(Satan)
        object.objectManager.add(Play_Icon)
        
    #Loss check
    if game.time_left_raw <= 0 and game.game_state != "start_screen" and game.game_state != "LOSS" and game.game_state != "WIN":
        game.mouse_free = False
        game.game_state = "LOSS"
        object.objectManager.clearObjects()
        
        Jesus = object.GameObject("Jesus",assetLoader.images["Jesus"],(0,0))
        Jesus.scale(0.3)
        Jesus.center()
        
        LossText = text.TextObject("LOSS_TEXT", "Jesus returned, YOU LOSE", presets.main_font, (0,200,50))
        
        Jesus.add_child(LossText)
        LossText.scale(14)
        LossText.center()
        LossText.move(630,-200)
        
        
        Play_Icon = button.Button("Play_Agin", assetLoader.images["Play_Again"], (0,0), Start_Pressed, base_scale=5)
        
        Play_Icon.center()
        Play_Icon.move(0,200)
        
        Play_Agian = text.TextObject("PlayAgain", "TRY AGAIN?", presets.main_font, (250,0,50))
        
        Play_Icon.add_child(Play_Agian)
        Play_Agian.scale(0.2)
        Play_Agian.center()
        Play_Agian.move(20,17)
   
        object.objectManager.add(Jesus)
        object.objectManager.add(Play_Icon)
            
    

random.seed()

def update_region_stats():

    for region in game.regions:
        if game.regions[region].get_type() == "SE":           #Asia ja Islam
            game.regions[region].effectiveness = 1 + game.upgrades["Internet"].get_level()/6 + game.upgrades["Persecution"].get_level()/6
            game.regions[region].foulness = 1 + game.upgrades["Demon"].get_level()/6 + game.upgrades["Persecution"].get_level()/6
            
        elif game.regions[region].get_type() == "W":            #Europe, Ru, Eafr, Pam, Eam ja Oce
            game.regions[region].effectiveness = 1 + game.upgrades["Internet"].get_level()/6 + game.upgrades["Education"].get_level()/6
            game.regions[region].foulness = 1 + game.upgrades["Demon"].get_level()/6 + game.upgrades["Education"].get_level()/6
        else:                                   #Varalta ettei peli hajoa jos unohtu laittaa type
            game.regions[region].effectiveness =0
            game.regions[region].foulness = 0
        #Kirkko random spawn
        
        if game.regions[region].percent != 100 and game.game_state == "game":
            if random.random() >= 1-math.log(20*game.regions[region].infamy+1)/490:
                
                if game.first_church == False:
                    game.first_church = True
                game.church_region = region
                print("added church")
                if(game.getGlobalCorruption() >= 60):
                    church = object.GameObject(f"BIGG_Church{region}", assetLoader.images["Holy_Church"], (0,0), Church_Update)
                    church.set_scale(0.2)
                    church.set_hue(100)
                else:
                    church = object.GameObject(f"Holy_Church{region}", assetLoader.images["Holy_Church"], (0,0), Church_Update)
                    church.scale(0.1)
                
                region_obj = object.objectManager.getObjectByName(region)
                object.objectManager.add(church)
                
                
                church.center()
                church.move(random.randint(-400,400),random.randint(-400,400))
                while not church.collides_with_mask(region_obj):
                    church.center()
                    church.move(random.randint(-400,400),random.randint(-400,400))
                church.scale(10)
                    
            
        
    
    
    
    
    
    
    
