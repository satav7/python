class fighter:
    def __init__(self, name):
        self.name = name
        self.damage = 10
        self.health = 100

    def attack(self, other_guy):                # Always use self when we use class .
        other_guy.health -= self.damage
        print('{} attacks {} !! Woooo'.format(self.name, other_guy.name))
        print('{} loses {} health points! '.format(other_guy.name, self.damage))
    
    def __str__(self):
        return "{}: {}".format(self.name, self.health)     # THIS IS THE POWER OF PYHTON
                                                        # A VERY IMPORTANT WAY TO STORE DATA

Rishab = fighter('rishab')
Praval = fighter('praval')




Rishab.attack(Praval)   # EVERY TIME FIGHTER WILL ATTACK ANOTHER FIGHTER, 10 health pts will be reduced
Praval.attack(Rishab)


print(Praval)                                            #THIS IS THE OUTPUT OF POWER OF PYHTON
print(Rishab)

