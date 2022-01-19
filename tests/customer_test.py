import unittest
from src.pub import Pub
from src.drink import Drink
from src.customer import Customer

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.pub = Pub("Not The Pet Shop", 100.00, ['The Famous Grouse', 'Grey Goose'])
        self.drink = Drink("The Famous Grouse", 5.00, 6)
        self.customer = Customer("Emma", 25.00, 30, 2)
    
    def test_customer_has_name(self):
        self.assertEqual("Emma", self.customer.name)

    def test_customer_has_cash(self):
        self.assertEqual(25.00, self.customer.wallet)

    def test_minus_c_wallet(self):
        self.customer.minus_c_wallet(self.customer.wallet, self.drink.price)
        self.assertEqual(20.00,self.customer.wallet)