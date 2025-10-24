class Cat:
    name = None
    age = None
    isHappy = None

    def aga(self,name,age,isHappy):
        self.name = name
        self.age = age
        self.isHappy = isHappy
    
    def get_data(self):
        print("Name:",self.name,"\nage:",self.age,"\nHappy:",self.isHappy)

Cat1 = Cat()
Cat1.aga("Спартак",13,True)
Cat1.get_data()