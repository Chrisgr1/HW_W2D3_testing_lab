import unittest

from src.food import Food

class TestFood(unittest.TestCase):

    def setUp(self):
        self.food = Food("Chips", 3.50, "high")

    def test_food_has_name(self):
        self.assertEqual("Chips", self.food.name)

    def test_food_has_price(self):
        self.assertEqual(3.50, self.food.price)

    def test_food_has_rejuvenation_level(self):
        self.assertEqual("high", self.food.rejuvenation_level)