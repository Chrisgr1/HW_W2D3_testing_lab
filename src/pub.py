from src.drink import Drink
from src.customer import Customer

class Pub:
    def __init__(self, name, till, drinks):
        self.name = name
        self.till = till
        self.drinks = drinks
    
    def take_money(self, drinks):
        self.till += drinks

    def remove_drink(self, drinks):
        self.drinks.remove(drinks)

    def buy_drink(self, drinks):
        self.take_money(drinks)
        self.remove_drink(drinks)
        self.customer1.minus_c_wallet(drinks)

    def check_age(self, customer):
        if customer.age < 18:
            return False
        return True

