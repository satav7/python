'''Understanding the Object n variable
 '''

class Robots:
     


    population = 0

    def __init__(self, name):

        self.name = name
    
        print(' Initialising {}'.format(self.name))

         # When this person is created it adds to the population

        Robots.population += 1
    
    def die(self):

        print('Dying {}'.format(self.name))

        Robots.population -= 1

        if Robots.population == 0:
            print(' I was the last one left!')
        
        else:
            print('{:d}  robots are still working!'.format(Robots.population))


    def say_hi(self):

        print('Hey! We would love to be your friends. My name is {}'.format(self.name))

    
    def __str__(self):
        return "{}".format(self.name)
    
    @classmethod                                     #tis made sure that the below method comes under 'Class'
    def how_many(cls):
        print('we have {:d} robots left'.format(cls.population))
     

Watson = Robots('Watson')
Rose = Robots('Rose')


Watson.say_hi()             #This is inside the def method
Robots.how_many()           # This is inside 'Class'



# Lets say watson dies !!

Watson.die()



Robots.how_many()

