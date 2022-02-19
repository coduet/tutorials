class Player:
    #__inti_ is used to define constructor of a class
    #self is always added in parameter. Refers to the instance of class being initialised.
    def __init__(self,name,jersey,age):
        self.name = name
        self.jersey = jersey
        self.age = age

class Defender(Player):
    def __init__(self,name, jersey, age,tackles,physicality):
        self.tackles = tackles
        self.physicality = physicality
        Player.__init__(self, name, jersey, age) # call the constructor of base class 