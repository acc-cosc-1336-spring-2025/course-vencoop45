import unittest
from src.homework.i_dictionaries_sets.dictionary import add_inventory, remove_inventory_widget

class Test_Config(unittest.TestCase):

    def test_add_inventory(self):
        inventory_dictionary = {}

        add_inventory(inventory_dictionary, "Widget1", 10)
        self.assertEqual(inventory_dictionary["Widget1"], 10)

        add_inventory(inventory_dictionary, "Widget1", 25)
        self.assertEqual(inventory_dictionary["Widget1"], 35)

        add_inventory(inventory_dictionary, "Widget1", -10)
        self.assertEqual(inventory_dictionary["Widget1"], 25)

    def test_remove_inventory_widget(self):
        inventory_dictionary = {"Widget1": 50, "Widget2": 20}
        result = remove_inventory_widget(inventory_dictionary, "Widget1")

        self.assertEqual(result, "Record deleted")
        self.assertNotIn("Widget1", inventory_dictionary)
        self.assertIn("Widget2", inventory_dictionary)