from src.drink import Drink
from src.customer import Customer

class Pub:
    def __init__(self, name, till, drinks):
        self.name = name
        self.till = till
        self.drinks = drinks
    
    def take_money(self, drinks):
        self.till += drinks

    def remove_drink(self, drink):
        self.drinks.remove(drink)

    def check_age(self, customer):
        if customer.age < 18:
            return False
        return True

