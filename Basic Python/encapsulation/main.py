class hero:

    def __init__(self, name, health, attackPower):
        self.__name = name
        self.__health = health
        self.__attackPower = attackPower
    
    # getter
    def getName(self):
        return self.__name
    
    def getHealth(self):
        return self.__health
    
    def getAttackPower(self):
        return self.__attackPower
    
    # setter
    def setName(self, name):
        self.__name = name
    
    def setHealth(self, health):
        self.__health = health
    
    def setAttackPower(self, attackPower):
        self.__attackPower = attackPower 
    
    def attacked(self, attackPower):
        self.__health -= attackPower
        print(f"{self.__name}'s health decreased to {self.__health}")
    
    def attack(self, otherHero):
        print(f"{self.__name} attacked {otherHero.getName()}")
        otherHero.attacked(self.__attackPower)
        
# Creating hero instances
knight = hero("knight", 100, 10)
sniper = hero("sniper", 50, 20)

# Example of using the attack method
knight.attack(sniper)
sniper.attack(knight)
