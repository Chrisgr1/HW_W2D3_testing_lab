import unittest
from src.pub import Pub
from src.drink import Drink
from src.customer import Customer

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.drink = Drink("The Famous Grouse", 5.00, 6)
        self.pub = Pub("Not The Pet Shop", 100.00, [self.drink, 'The Famous Grouse', 'Grey Goose'])
        self.customer = Customer("Emma", 25.00, 30, 2)
    
    def test_customer_has_name(self):
        self.assertEqual("Emma", self.customer.name)

    def test_customer_has_cash(self):
        self.assertEqual(25.00, self.customer.wallet)

    def test_minus_c_wallet(self):
        self.customer.minus_c_wallet(self.drink)
        self.assertEqual(20.00,self.customer.wallet)
    
    def test_buy_drink(self):
        self.customer.buy_drink(self.drink, self.pub)
        self.assertEqual(8, self.customer.drunkenness)