
class Region:

    def __init__(self, name):

        self.name = name
        self.percent = 100
        
        self.effectiveness = 10
        self.foulness= 1
        self.infamy = 1
        
        #On totta jos äskettäin vaihdettiin prosentti
        self.changed_percent = False

    def reduce(self):
        self.changed_percent = True
        self.percent -= self.effectiveness
        return self.effectiveness*self.foulness

    def get_name(self):
        return self.name
    
    def get_percent(self):
        return self.percent
    
    def get_effectiveness(self):
        return self.effectiveness
    
    def get_foulness(self):
        return self.foulness
    
    def get_infamy(self):
        return self.infamy