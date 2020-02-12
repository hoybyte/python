#Object Oriented Programming

class PlayerCharacter:
    #Class Object Attribute
    #Only use Class Object Attributes when attribute does not change against all instances
    membership = True
    def __init__(self, name, age):
        if (PlayerCharacter.membership):
            self.name = name #attributes of the object
            self.age = age

    def shout(self):
        print(f'My name is {self.name}')
        
    def run(self):
        print('run')
        return 'done'
        
player1 = PlayerCharacter('Cindy', 21)

print(player1.name)