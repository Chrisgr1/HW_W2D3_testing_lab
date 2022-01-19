# from src.drink import Drink 
# from src.pub import Pub

class Customer:
        
    def __init__(self, name, wallet, age, drunkenness):
        self.name = name
        self.wallet = wallet
        self.age = age
        self.drunkenness = drunkenness
    
    def minus_c_wallet(self, wallet, drink):
        self.wallet -= drink