class Phone:
    def __init__(self,name,model,price):
        self.name = name
        self.model = model
        self.price = price
        
    def phone_name(self):
        return f"{self.name} {self.model}"
    
    def __str__(self):
        return f"Phone is {self.name} {self.model} and the price is {self.price}."
    
    def __repr__(self):
        return f"{self.name} {self.model} {self.price}"
    
    def __add__(self,other):
        return self.price + other.price
    # def __add__(self,next):
    #     return self.model + next.model
        
        
phone1 = Phone("Realme","5s",10000)
phone2 = Phone("Realme","5 pro",13000)
print(phone1.price)
print(phone1.__repr__())
print(str(phone1))

print(phone1 + phone2)

# polymorphism :- it simply means overwriting of same function in two different classes.

        