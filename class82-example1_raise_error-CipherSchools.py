class Animal:
    def __init__(self,name):
        self.name = name 
    def sound(self):
        raise NotImplementedError("You to define this method in subclasses..")
    
    
class Dog(Animal):
    def __init__(self, name,breed):
        super().__init__(name)
        self.breed = breed
        
    def sound(self):
        return "hello how are you?"
        

class Elephant(Animal):
    def __init__(self, name,breed):
        super().__init__(name)
        self.breed = breed
        
dog1 = Dog("Tommy","Pomerian")
elephant1 = Elephant("Raja","White Elephant")

print(dog1.sound()) 
print(elephant1.sound())