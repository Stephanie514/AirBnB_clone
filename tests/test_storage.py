#!/usr/bin/python3
"""Defines Unittest module to test Storage"""
import unittest
from models.place import Place
from models.engine.file_storage import FileStorage


class TestStorage(unittest.TestCase):
    def setUp(self):
        self.storage = FileStorage()
        self.storage.reload()

    def tearDown(self):
        self.storage._FileStorage__objects = {}
        self.storage.save()

    def test_save_place(self):

        place = Place()
        place.name = "My Place"
        self.storage.new(place)
        self.storage.save()

        loaded_place = self.storage.all(Place).values()
        self.assertTrue(loaded_place)


if __name__ == '__main__':
    unittest.main()
