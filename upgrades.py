class Upgrade:

    def __init__(self, name, base_cost):
        self.name = name                    # Upgraden nimi
        self.level = 0                      # Upgraden leveli
        self.base_cost = base_cost          # Mitä päivittäminen levelille 1 maksaa. Myöhemmille kerrotaan numerolla

    # Päivittää upgraden ja palauttaa käytettyjen sielujen määrän, jos sielut riittää ja leveli on maksimissaan 4. 
    # Muuten palauttaa 0.
    def level_up(self, soul):
        if soul >= (self.level+1)*self.base_cost and self.level < 4:
            self.level += 1
            return self.level*self.base_cost
        else:
            return 0

    def get_name(self):
        return self.name
    
    def get_level(self):
        return self.level

    def get_cost(self):
        return (self.level+1)*self.base_cost

