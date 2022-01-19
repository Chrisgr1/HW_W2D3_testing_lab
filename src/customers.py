# from src.drink import Drink 
# from src.pub import Pub

class Customers:
        
    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet
    
    def minus_c_wallet(self, wallet, drink):
        self.wallet -= drink