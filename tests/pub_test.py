import unittest
from src.pub import Pub
from src.drink import Drink
from src.customer import Customer

class TestPub(unittest.TestCase):
    def setUp(self):
        self.pub = Pub("Not The Pet Shop", 100.00, ['The Famous Grouse', 'Grey Goose'])
        self.drink = Drink("The Famous Grouse", 5.00, 7)
        self.customer1 = Customer("Emma", 25.00, 30, "low")
        self.customer2 = Customer("Jon", 25.00, 14, "low")

    def test_pub_has_name(self):
        self.assertEqual("Not The Pet Shop", self.pub.name)

    def test_has_till(self):
        self.assertEqual(100.00, self.pub.till)

    def test_has_drink(self):
        self.assertEqual(['The Famous Grouse', 'Grey Goose'], self.pub.drinks)
        
    def test_take_money(self):
        self.pub.take_money(5.00)
        self.assertEqual(105.00, self.pub.till)
        
    def test_remove_drink(self):
        self.pub.remove_drink('Grey Goose')
        self.assertEqual(['The Famous Grouse'], self.pub.drinks)

    def test_buy_drink(self):
         self.pub.remove_drink('Grey Goose')
         self.assertEqual(['The Famous Grouse'], self.pub.drinks)
         self.pub.take_money(5.00)
         self.assertEqual(105.00, self.pub.till)
         self.customer1.minus_c_wallet(self.customer1.wallet, self.drink.price)
         self.assertEqual(20.00,self.customer1.wallet)
    
    def test_check_age_true(self):
        result = self.pub.check_age(self.customer1)
        self.assertEqual(True, result)
