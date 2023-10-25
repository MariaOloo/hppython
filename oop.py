class Cars:
    #constructor
    def __init__(self, type, color, model):
        self.type=type
        self.color=color
        self.model=model

    #method
    def onyesha(self):
        print(f"I love {self.model} cars which is {self.type} being {self.color}")

#creating object
myobj=Cars("Saloon","Grey","Toyota")
myobj.onyesha()
myobj2=Cars("G-Wagon","Black","Isuzu")
myobj2.onyesha()

