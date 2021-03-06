from utils import flavors_terminal as fla

class Item():
    def __init__(self, name, description, value,  specialRoom = None):
        self.value = value
        self.name = name
        self.description = description
        self.specialRoom = specialRoom
    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description, self.value)
    def modifyPlayer(self, player):
        return NotImplementedError()

class Credits(Item):
    def __init__(self, amount, specialRoom):
        self.amount = amount
        self.specialRoom = specialRoom
        Item.__init__(self, specialRoom = specialRoom , name = "Credits", description="Booty!!", value = self.amount)
    def modifyPlayer(self, player):
        return fla.con_gray("My precious...")

class Screwdriver(Item):
    def __init__(self, specialRoom):
        Item.__init__(self, specialRoom = specialRoom, name="Screwdriver", description="It's Kaylee's tools...", value = 0)
    def modifyPlayer(self, player):
        if self.specialRoom == player.room().__class__.__name__:
            print fla.con_gray("Well, I guess I could try fixing it with this... No luck")
class Weapon(Item):
    def __init__(self,  specialRoom, name, description, value, damage):
        self.damage = damage
        Item.__init__(self, name, description, value, specialRoom = specialRoom)
    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nDamage: {}".format(self.name, self.description, self.value, self.damage)

class Rock(Weapon):
    def __init__(self, specialRoom):
        self.specialRoom = specialRoom
        Weapon.__init__(self, specialRoom = specialRoom , name = "Rock", description = "... It's a rock", value=0, damage = 5)
class Gun(Weapon):
    def __init__(self, specialRoom):
        Weapon.__init__(self, specialRoom = specialRoom,  name = "Gun", description = "... It's a gun", value=0, damage = 30)
        def modifyPlayer(self, player):
            if room_exists(player.locationX,player.locationY).__class__.__name__ == 'CargoBay' and player.runTime['EXCHANGE']:
                player.runTime['GUN'] = True

class Toy(Item):
    def __init__(self, specialRoom):
        Item.__init__(self, specialRoom = specialRoom , name = "Dinosaurs", description="WAAARRRGGH", value = 1000)

class Cake(Item): #TODO
    def __init__(self, specialRoom):
        self.specialRoom = specialRoom
        Item.__init__(self, specialRoom = specialRoom , name = "Cake", description="It's a lie...", value = 5)

class Adrenaline(Item):
    def __init__(self, specialRoom):
        self.specialRoom = specialRoom
        Item.__init__(self, specialRoom = specialRoom , name = "Adrenaline shot", description="A syringe with a big damn adrenaline dosis", value = 10)
    def modifyPlayer(self, player):
        if player.health<80: player.health = player.health +20
        elif player.health<100: player.health = 100

class Catalyzer(Item):
    def __init__(self):
        Item.__init__(self, specialRoom = "EngineRoom", name="Screwdriver", description="It's Kaylee's tools...", value = 0)
    def modifyPlayer(self, player):
        if self.specialRoom == player.room().__class__.__name__:
            player.runTime["USER_CATALYZER"] = True
            print fla.con_gray("Finally, it is fixed! Hooray!")


#print Credits( 20)
#print Gun()
