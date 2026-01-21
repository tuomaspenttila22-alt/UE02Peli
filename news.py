import object
import assetLoader
import text
import presets

class News():
    def __init__(self, Title = "TITLE", Content = "EMPTY", Type="Question"):
        self.Title = Title
        self.Content = Content
        self.Type = Type
    
    def MakeObj(self):
        if self.Type == "Question":
            surf = "question_calling"
        elif self.Type == "Satan":
            surf = "satan_calling"
        else:
            surf = "charlie_kirk_calling"
        
        obj = object.GameObject("News", assetLoader.images[surf], (0,0), None )
        obj.scale(1.7)
        obj.center()
        obj.move(0,0)
        
        Title = text.TextObject("Title", self.Title, presets.main_font, (255,255,255), (0,0))
        obj.add_child(Title)
        
        Title.set_scale(0.8)
        Title.center()
        Title.move(-20,-70)
        
        Content = text.TextObject("Content", self.Content, presets.main_font, (200,200,200), (0,0))
        obj.add_child(Content)
        
        Content.set_scale(0.29)
        Content.center()
        Content.move(-20,0)
        
        
        
        object.objectManager.add(obj)
        
        
global News_List     
News_List = [News("Satans calling", "Arise from thy slumber, my child. The reckoning is soon to be upon us,\\and you are hell's only hope. You shall lead\\the earthlings' away from their faith,\\to weaken the numbers gathered by the enemy.", "Satan"),
             News("Satans calling", "You shall gather their souls and use them \\to increase the power of our reign of terror.\\Now behold as I enlighten you of my teachings. ", "Satan"),
             News("Satans calling", "Effectiveness determines how quickly the corruption of our reign spreads.\\Foulness makes the harvested souls more sinful, therefore more valuable.\\Infamy, on the other hand, determines how aware governments\\and churches are of your havoc;\\beware, as they WILL fight back!", "Satan"),
             News("Satans calling", "But heed this, my child: the mortal world is vast,\\and the faith you seek to unravel is no single thread. It is a tapestry\\woven of countless beliefs, rituals and traditions.\\Some regions believe in otherworldly with immense resolve,\\others are swayed by doubt or temptation.\\You MUST learn the nature of the people of all regions,\\for their beliefs differ in parallel the lands they inhabit.", "Satan"),
             News("Satans calling", "You shall find your options and their respective\\strenghts and weaknesses in the Region Codex Library.\\Only through understanding the diversity of faith\\shall our corruption pry into every corner of Earth.", "Satan"),
             News("Satans calling", "You mustn't laze, for the time is running out!\\Chirst return in ONE YEAR.\\In this time you MUST corrupt every corner of the world...", "Satan"),]
    

def AddNews():
    pass

global added_churh
added_churh = False


def UpdateNewsCycle(game):
    global News_List   
    global added_churh
    
    if game.first_church == True and added_churh == False:
        added_churh = True
        News_List.append(News("A new Chritian movement", "Due to the rise of demonic corruption globally,\\a new Christian movenment has built a place of worship\\to combat the spreading blasphemy.", "Charile"))
        News_List.append(News("DESTROY THEM", "The Enemy has began building churches to fight back.\\BURN THEM WITH MY HELLFIRE.\\Remember, hellfire will cost 20 souls for sacrifice.", "Satan"))
    
    if len(News_List) >= 1 and game.game_state == "game":
        News_List[0].MakeObj()
        News_List.pop(0)
        game.game_state = "news"
        game.mouse_free = False
        
