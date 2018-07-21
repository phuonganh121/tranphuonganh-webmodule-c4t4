class Ninja:
    # ham tao (constructor)
    def __init__(self, n, s, d):
        self.name = n
        self.strength = s
        self.defense = d
        self.hp = 10
     
    def print(self):
        print (self.name)
        print (self.strength)
        print (self.defense)
        print (self.hp)

    def attack(self, other):
        # self:  attacker 
        # other: defender 
        # str(attacker) - def(defender) / 2 => HP_Loss 
        # tru mau cho defender 
        hp_loss = self.strength - (other.defense / 2)
        other.hp -= hp_loss

ninja1 = Ninja("Kakashi", 7, 9) #n = object

ninja2 = Ninja("Itachi", 6, 10) 

ninja1.print()

print ("* "*10)

ninja2.print()

print ("* "*10)

print("Kakashi is attacking Itachi")
ninja1.attack(ninja2)
ninja2.print()
