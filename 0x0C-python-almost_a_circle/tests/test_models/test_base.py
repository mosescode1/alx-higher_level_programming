#!/usr/bin/python3
"""All test cases for the base class"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    b1 = Base()
    b2 = Base()
    b3 = Base(12)
    b4 = Base()
    dicts = {'name': "moses", 'age': 30}  # python dictionary
    json = '{"name": "moses", "age": 30}'  # json list

    def test_id(self):
        self.assertEqual(self.b1.id, 1)
        self.assertEqual(self.b2.id, 2)
        self.assertEqual(self.b3.id, 12)
        self.assertEqual(self.b4.id, 3)

    def test_to_json(self):
        self.assertEqual(self.b2.to_json_string(
            self.dicts), '{"name": "moses", "age": 30}')

    def test_to_dict(self):
        self.assertEqual(self.b1.from_json_string(self.json), self.dicts)
