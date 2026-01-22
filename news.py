import object
import assetLoader
import text
import presets

def slow_show(obj, dt):
    if obj.time_alive >= 100:
        obj.show()


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
        Title.updateLoop = slow_show
        obj.add_child(Title)
        
        Title.set_scale(0.8)
        Title.center()
        Title.move(-20,-70)
        Title.hide()
        
        Content = text.TextObject("Content", self.Content, presets.main_font, (200,200,200), (0,0))
        obj.add_child(Content)
        Content.updateLoop = slow_show
        Content.set_scale(0.29)
        Content.center()
        Content.move(-20,0)
        Content.hide()
        
        object.objectManager.add(obj)
        

class Up_News():
    def __init__(self, News, region, inf_cond, corrupt_cond, infamy_change = 0, corrupt_change = 0, soul_change = 0):
        self.News = News
        self.region = region
        self.corrupt_cond = corrupt_cond
        self.infamy_cond = inf_cond
        self.infamy_change  = infamy_change
        self.corrupt_change = corrupt_change
        self.soul_change = soul_change
    
        
        
   
        
        
global News_List     
News_List = [News("Satans calling", "Arise from thy slumber, my child. The reckoning is soon to be upon us,\\and you are hell's only hope. You shall lead\\the earthlings' away from their faith,\\to weaken the numbers gathered by the enemy.", "Satan"),
             News("Satans calling", "You shall gather their souls and use them \\to increase the power of our reign of terror.\\Now behold as I enlighten you of my teachings. ", "Satan"),
             News("Satans calling", "Effectiveness determines how quickly the corruption of our reign spreads.\\Foulness makes the harvested souls more sinful, therefore more valuable.\\Infamy, on the other hand, determines how aware governments\\and churches are of your havoc;\\beware, as they WILL fight back!", "Satan"),
             News("Satans calling", "But heed this, my child: the mortal world is vast,\\and the faith you seek to unravel is no single thread. It is a tapestry\\woven of countless beliefs, rituals and traditions.\\Some regions believe in otherworldly with immense resolve,\\others are swayed by doubt or temptation.\\You MUST learn the nature of the people of all regions,\\for their beliefs differ in parallel the lands they inhabit.", "Satan"),
             News("Satans calling", "You shall find your options and their respective\\strenghts and weaknesses in the Region Codex Library.\\Only through understanding the diversity of faith\\shall our corruption pry into every corner of Earth.", "Satan"),
             News("Satans calling", "You mustn't laze, for the time is running out!\\Christ returns in ONE YEAR.\\In this time you MUST corrupt every corner of the world...", "Satan"),]
    
global Upcoming_News
Upcoming_News = [Up_News(News("North America Corrupted", "The US along with Canada have been\\completely consumed by corruption.\\+1000 souls", "Satan"), "Pam", 0, 100, 0, 0, 1000), 
    Up_News(News("US President addres", "The President of the United States\\has issued a formal addres\\to announce a new nationwide\\campaign against satanic corruption.\\+10% infamy in North America.", "Kirk"), "Pam", 35, 0, 10, 0),
    Up_News(News("Chaos in USA","Heretics in the USA are yelling\\on the streets about the antichrist.\\The people however are not amused.", "Question"), "Pam", 5, 0, 0, 0),
    Up_News(News("Japan fights back","Japan starts a campaign to drive evil spirits through rituals.\\Faith in ritualistic areas is reforming.\\ +10% infamy in Asia", "Question"), "Asia", 15, 0, 10, 0),
    Up_News(News("The Orthodox Church Strikes","The Orthodox Church orders all denominations to be aware\\of the rising demonic activity.\\Churches will be more abundant.\\+5 infamy globally", "Kirk"), "World", 30, 0, 5, 0),
    Up_News(News("Churches join together","Investigations confirm demonic corruption within religious communities.\\Major churches begin sharing information\\and organizing countermeasures.\\ -10 % corruption globally", "Kirk"), "World", 55, 0, 0, -10),
    Up_News(News("Corruption under fire","Faith leaders worldwide acknowledge the threat publicly.\\Interdenominational alliances form,\\increasing resistance and slowing further spread.", "Kirk"), "World", 75, 0, 0, 0),
    Up_News(News("Global demonic crisis","Governments recognize the corruption as a global threat.\\Religious institutions receive protection and funding.\\The Public is fully aware.", "Question"), "World", 85, 0, 0, 0),
    Up_News(News("Corruption at large","The corruption is fully exposed.\\The rest of humanity is alert and unified.\\Churches are at their most powerful,\\making further influence extremely difficult.", "Kirk"), "World", 100, 0, 0, 0),
    Up_News(News("Corruption spotted globally","Corruption increases.\\Isolated believers report feelings of doubt and spiritual exhaustion.\\Confessions increase, but no clear cause is identified.", "Question"), "World", 0, 5, 0, 0),
    Up_News(News("Believers faith questioned","Small congregations begin losing members\\to unexplained apathy. Faith weakens.\\+100 souls", "Question"), "World", 0, 10, 0, 0, 100),
    Up_News(News("Corrupted Infuence at large","Influential preachers in the Americas\\begin spreading distorted interpretations of scripture.\\Corruption strengthens.\\+10% infamy in South America", "Kirk"), "Eam", 0, 25, 10, 0),
    Up_News(News("Asia corrupted","Asian communities start abandoning traditional worship.\\Faith-based protections weaken significantly.\\+150 souls", "Question"), "Asia", 0, 50, 0, 0, 150),
    Up_News(News("UN combats corruption","UN issues a mandate to use force in exorcising the wretched.\\Public worry is growing rapidly.\\+10% infamy globally", "Kirk"), "World", 0, 70, 10, 0),
    Up_News(News("The resistance is falling","The few faithful left feel watched.\\European, North American and Oceanian\\communities are crumbling.\\+500 souls", "Question"), "World", 0, 85, 0, 0, 500),
    Up_News(News("Global faith dead","Almost all faith has been corrupted.\\The faithful are in despair as their loved ones convert.", "Question"), "World", 0, 95, 0, 0),
    Up_News(News("Churches rebuild","As more and more churches have been destroyed,\\the unified faith have started building\\even stronger churches.", "Kirk"), "World", 0, 60, 0, 0),]


def AddNews():
    pass

global added_churh
added_churh = False

global added_tip_1
added_tip_1 = False


global added_tip_2
added_tip_2 = False

def UpdateNewsCycle(game):
    global News_List   
    global added_churh
    global Upcoming_News
    global added_tip_1
    global added_tip_2
    for Up in Upcoming_News:
        if Up.region == "World" and game.getGlobalCorruption() >= Up.corrupt_cond and game.getGlobalInfamy() >= Up.infamy_cond:
            News_List.append(Up.News)
            for region in game.regions:
                game.regions[region].infamy += Up.infamy_change
                game.regions[region].percent -= Up.corrupt_change
            game.soul_count += Up.soul_change
            Upcoming_News.remove(Up)
        if Up.region in game.regions:
            if 100-game.regions[Up.region].percent >= Up.corrupt_cond and game.regions[Up.region].infamy >= Up.infamy_cond:
                News_List.append(Up.News)
                game.regions[Up.region].infamy += Up.infamy_change
                game.regions[Up.region].percent -= Up.corrupt_change
                game.soul_count += Up.soul_change
                Upcoming_News.remove(Up)
    
    if game.first_church == True and added_churh == False:
        added_churh = True
        News_List.append(News("A new Chritian movement", "Due to the rise of demonic corruption globally,\\a new Christian movenment has built a place of worship\\to combat the spreading blasphemy.", "Charile"))
        News_List.append(News("DESTROY THEM", "The Enemy has began building churches to fight back.\\BURN THEM WITH MY HELLFIRE.\\Remember, hellfire will cost 20 souls for sacrifice.", "Satan"))
    
    if game.game_time >= 8000 and not added_tip_1:
        News_List.append(News("Tip", "The Region Codex Library is a helpful tool\\to determine the most effective strategy.\\Click on a region to open it.", "Question"))
        added_tip_1 = True
        
    if game.soul_count >= 200 and not added_tip_2:
        News_List.append(News("Tip", "You can enhance your reign of terror\\in the Demonic Upgrade Shop.\\Click Q to open it.", "Question"))
        added_tip_2 = True
    
    if len(News_List) >= 1 and game.game_state == "game" and game.mouse_free:
        News_List[0].MakeObj()

        News_List.pop(0)
        game.game_state = "news"
        game.mouse_free = False
        
