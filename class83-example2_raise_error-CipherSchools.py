class Mobiles:
    def __init__(self,name):
        self.name = name

class MobileStore:
    def __init__(self):
        self.mobiles = []

    def add_mob(self,new_mobile):
        if isinstance(new_mobile,Mobiles):
            self.mobiles.append(new_mobile)
        else:
            raise TypeError("new mobile should be of object class...")

oneplus = Mobiles('one plus 6t')
realme = 'realme X'
mobostore = MobileStore()
mobostore.add_mob(oneplus)
mob = mobostore.mobiles
print(mob[0])