import unittest
from src.homework.j_classes.class_a import Die

class Test_Die(unittest.TestCase):

    def test_roll_range(self):
        my_die = Die()
        for _ in range(3):
            my_die.roll()
            rolled_value = my_die.get_rolled_value()
            self.assertTrue(1 <= rolled_value <= 6, f"Roll value {rolled_value} is out of range [1, 2]")
