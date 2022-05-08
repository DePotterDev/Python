import unittest
from city_function import city_country


class TestCities(unittest.TestCase):
    def test_city_country(self):
        """Testing if city and countries can go in same sentence."""
        formatted_version = city_country('brugge', 'belgium')
        self.assertEqual(formatted_version, 'Brugge, Belgium')

    def test_city_country_pop(self):
        """Testing if city and countries can go in same sentence."""
        formatted_version = city_country('brugge', 'belgium', '300000')
        self.assertEqual(formatted_version, 'Brugge, Belgium - 300000')
