class AdarshConstruction:
    website = 'https://adarsh-construction.business.site'    # INSTANT VARIABLE --> part of class variable
    def __init__(self, name):
        self.name = name

object = AdarshConstruction('paaji')

print(object.name)                          #Storing variable in object(in it method)
print(AdarshConstruction.website)           #Storing info in class variable 
