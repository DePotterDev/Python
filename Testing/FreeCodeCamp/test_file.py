import unittest
from unittest import result
from name_function import formatted_name


class NamesTestCase(unittest.TestCase):

    def test_first_last_name(self):
        # print("Hello")
        result = formatted_name("laurens", "de potter")
        self.assertEqual(result, "Laurens De Potter")

    def test_first_last_middle_name(self):
        result = formatted_name("raymond", "reddington", "red")
        self.assertEqual(result, "Raymond Red Reddington")

if __name__ == '__main__':
   unittest.main()