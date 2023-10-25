class Animals:
    def speaks(self):
        print("Animals Speak")

class Cat(Animals):
    def meows(self):
        print("Cat meows")
#initialize an object
paka=Cat()
paka.meows()
paka.speaks()
