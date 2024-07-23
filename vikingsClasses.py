import random

# Soldier
class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    
    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.health -= damage
    

# Viking
class Viking(Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health, strength)
        self.name = name

    def battleCry(self):
        return "Odin Owns You All!"

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"

# Saxon
class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)
    
    def receiveDamage(self, damage):
        self.health -= damage
        if (self.health > 0):
            return f"A Saxon has received {damage} points of damage"
        else:
            return f"A Saxon has died in combat"

# Davicente
class War():
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, viking):
        self.vikingArmy.append(viking)
    
    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)
    
    def vikingAttack(self):
        vi = self.vikingArmy[random.randint(0,len(self.vikingArmy)-1)]
        sa = self.saxonArmy[random.randint(0,len(self.saxonArmy)-1)]

        r = sa.receiveDamage(vi.strength)
        x = 0
        for s in self.saxonArmy:
            if s.health <= 0:
                self.saxonArmy.pop(x)   
            x +=1
        return r
    
    def saxonAttack(self):
        vi = self.vikingArmy[random.randint(0,len(self.vikingArmy)-1)]
        sa = self.saxonArmy[random.randint(0,len(self.saxonArmy)-1)]

        r = vi.receiveDamage(sa.strength)
        x = 0
        for v in self.vikingArmy:
            if v.health <= 0:
                self.vikingArmy.pop(x)   
            x +=1
        return r

    def showStatus(self):
        if len(self.saxonArmy) == 0:
            r = "Vikings have won the war of the century!"
        if len(self.vikingArmy) == 0:
            r = "Saxons have fought for their lives and survive another day..."
        if len(self.saxonArmy) >= 1 and len(self.vikingArmy) >= 1:
            r = "Vikings and Saxons are still in the thick of battle."
        return r

#yop
# class War2:

#     def __init__(self):
#         # your code here

#     def addViking(self, Viking):
#         # your code here
    
#     def addSaxon(self, Saxon):
#         # your code here
    
#     def vikingAttack(self):
#         # your code here

#     def saxonAttack(self):
#         # your code here

#     def showStatus(self):
#         # your code here

#     pass


