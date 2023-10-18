#!/usr/bin/python3
"""Defines Unittest module that tests all Cases"""
import unittest
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class TestAllClasses(unittest.TestCase):
    def test_state_attributes(self):
        state = State()
        self.assertEqual(state.name, "")

    def test_city_attributes(self):
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    def test_amenity_attributes(self):
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

    def test_place_attributes(self):
        place = Place()
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        # Add more tests for other attributes

    def test_review_attributes(self):
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")


if __name__ == '__main__':
    unittest.main()
