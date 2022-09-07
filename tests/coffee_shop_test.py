import unittest
from src.coffee_shop import CoffeeShop

class TestCoffeeShop(unittest.TestCase):
    
    def setUp(self):
        self.stock = [
                    {   "type": "drink",
                        "name" : "Latte",
                        "price": 2.50,
                        "energy": 5
                        },
                    {   "type": "drink",
                        "name" : "Mocha",
                        "price": 3.50,
                        "energy": 10
                        },
                    {   "type": "food",
                        "name" : "Burger",
                        "price": 8.00,
                        "energy": 50
                        }
                ]

        self.coffee_shop = CoffeeShop("The Prancing Pony", 100.00, self.stock)

    def test_coffee_shop_has_name(self):
        self.assertEqual("The Prancing Pony", self.coffee_shop.name)

    def test_increase_till(self):
        self.coffee_shop.increase_till(2.50)
        self.assertEqual(102.50 , self.coffee_shop.till)

    def test_get_total_stock_value(self):
        total_stock_value= self.coffee_shop.get_total_stock_value()
        self.assertEqual(14, total_stock_value)
