import object
import text
import presets


codex = {"Europe" : "EUROPE:\\Out of all the regions, the culture and history of Europe\\have been the most affected by Christianity.\\Europe has also seen some of the greatest schisms\\in all of church history. As a result, the region\\is split between the protestant north,\\ catholic west, and orthodox east.\\Despite – or perhaps because of –\\Europe's long history with Christianity,\\the region is secularising quickly.\\Distract its inhabitants with things of the world,\\and Europe is ours.",
        "Ru" : "RUSSIA & UKRAINE:\\The Orthodox Church dominates the religious life\\of both countries. Russia should be easy to corrupt:\\most churches are illegal, the Orthodox one\\is a puppet of the government,\\and inhabitants are aware of this.\\Any strategy will work here.\\You could either use the inhabitants' distrust of the state\\church to sell them materialistic ideologies,\\or use the government to get rid of the smaller ones.\\Ukraine will be more problematic.\\Around 70% of inhabitants report being believers,\\church and state are separate,\\and neither is very useful individually.\\If only there was a way to get\\the Russian government here...",
        "Asia" :"EASTERN ASIA:\\Most East Asian countries are dominated by either\\Hinduism, Buddhism or Islam.\\Christianity is a minority religion,\\and while being christian is technically not a crime,\\it does not take much effort to make it punishable.\\Hindu nationalists and the Chinese government\\will be your best friends here." ,
        "Eafr" :"SOUTHERN AFRICA:\\The vast majority of Southern Africans are\\professing Christians of varying denominations,\\which makes this area somewhat tricky.\\Your best bet is to direct their devotion towards\\what is worldy and irrelevant.\\Prosperity preaching is already\\widespread in African megachurches,\\a fact you can certainly take advantage of.",
        "Islam" : "ISLAMIC REGION:\\While historically the very heart of the Christian world,\\these areas are now predominantly Islamic.\\What Christian churches still exist\\are mostly Oriental Orthodox.\\Many muslims would be more than happy\\to get rid of the local Christians.\\A great first project for the beginning demon.",
        "Pam" : "NORTH AMERICA:\\The USA is a melting pot of denominations,\\and the birthplace for dozens of them.\\Inhabitants are a religious lot, but they are\\also great at justifying their other beliefs with religion.\\As such, directing their devotion towards heresies\\and prosperity preaching should be quite easy.\\Canada's situation resembles Europe: Catholic\\ and Protestantchurches struggling with secularisation.\\You know what to do.",
        "Eam" : "SOUTH AMERICA:\\Latin America has a growing Christian population\\of more than 600 million.\\Most of them are Catholic, though Pentecostalism\\is quickly growing in popularity.\\Latin American Catholicism is prone to the\\formation of cults and local traditions,\\usually after being mixed with native religions.\\The mostly poor population is also quite\\susceptible to prosperity theology.",
        "Oce" : "AUSTRALIA & OCEANIA:\\Christianity is the dominant religion here,\\having all but replaced the animistic religions\\of the native Aboriginal and Maori people.\\Its popularity, however, has been on decline,\\as the people have abandoned\\their religion for secularity.\\If you can crush the growing\\ pentecostal churches of Australia,\\the whole region should soon\\rest safely in Mammon's embrace."}




def CreateCodexText(obj, region):
    
    Text = text.TextObject("Codex_text", codex[region], presets.main_font, (255,255,255), (0,0))
    obj.add_child(Text)
    Text.scale(0.013)
    Text.center()
    Text.move(-320,-150)
    
    
    
    