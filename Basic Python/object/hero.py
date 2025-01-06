class hero:
    def __init__(self, name, health, power, armor):
        self.name = name
        self.health = health
        self.power = power
        self.armor = armor

    def attack (self, opponent):
        print (self.name, "attack", opponent.name, "with", self.power, "dmg")
        opponent.attacked(self, self.power)

    def attacked (self, opponent, opponentPower):
        self.health = self.health - (opponentPower / self.armor)
        print (self.name, "attacked by", opponent.name, "health dicrease to", self.health)

sniper = hero("sniper", 100, 20, 3) 
knight = hero ("knight", 100, 15, 4)

sniper.attack (knight)

print ()

knight.attack (sniper)


     