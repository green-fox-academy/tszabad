from pirate import Pirate
import random

class Ship:
    def __init__(self, name):
        self.name = name
        self.crew = []
        self.captain = None
        self.alive_crew = 0
        

    def fillShip(self, captain, pirate):
        self.captain = captain
        for i in range(random.randint(1, len(pirate))):
            self.crew.append(pirate[i])
            if pirate[i].alive == True:
                self.alive_crew +=1

        return self.captain, self.crew

    def __str__(self):
        return 'Captain(name='+ captain.name+', rum drinked='+str(captain.count)+'captain is alive'
        + str(captain.alive) + 'alive pirates in the crew' + str(self.alive_crew) + ')'

    def battle(self, other_ship):
        ship1_score = self.alive_crew - self.captain.count
        ship2_score = other_ship.alive_crew - other_ship.captain.count
        if ship1_score > ship2_score:
            for i in range(random.randint(1, len(self.crew))):
                self.crew[i].drinkSomeRum()
            
            for i in range(random.randint(1, len(other_ship.crew))):
                other_ship.crew[i].die()
            print(self.name + " won the battle")
            return True
            
        else:
            for i in range(random.randint(1, len(other_ship.crew))):
                other_ship.crew[i].drinkSomeRum()
            for i in range(random.randint(1, len(self.crew))):
                self.crew[i].die()
            print(other_ship.name + " won the battle")
            return False


        



        
    
