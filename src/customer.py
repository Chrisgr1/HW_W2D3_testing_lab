# from src.drink import Drink 
# from src.pub import Pub

class Customer:
        
    def __init__(self, name, wallet, age, drunkenness):
        self.name = name
        self.wallet = wallet
        self.age = age
        self.drunkenness = drunkenness
    
    def buy_drink(self, drinks, pub): # method buy_drink in class customer becasue customer is the one who buy drink?
        pub.take_money(drinks.price)
        pub.remove_drink(drinks)
        self.minus_c_wallet(drinks)
        self.drunkenness += drinks.alcohol_level
    
    def minus_c_wallet(self, drink):
        self.wallet -= drink.price