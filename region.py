
class Region:

    def __init__(self, name, type):

        self.name = name
        self.type = type
        self.percent = 100
        
        self.effectiveness = 1
        self.foulness= 1
        self.infamy = 0
        
        #On totta jos äskettäin vaihdettiin prosentti
        self.changed_percent = False

    def reduce(self):
        
        
        self.percent -= self.effectiveness * 0.2 * 100
        if self.percent <= 0:
            self.percent = 0
        else:
            self.changed_percent = True
        return round(self.effectiveness*self.foulness*1.5*100)

    def cure(self):
        
        self.percent += 0.2
        if self.percent >= 100:
            self.percent = 100
        else:
            self.changed_percent = True

    def add_infamy(self, factor):
        self.infamy += factor * self.foulness
        
        if self.infamy >= 100:
            self.infamy = 100
    
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
    
    def get_type(self):
        return self.type