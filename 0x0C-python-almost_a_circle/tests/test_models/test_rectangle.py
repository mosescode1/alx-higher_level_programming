#!/usr/bin/python3
"""All test cases for the base class"""
import unittest
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    r1 = Rectangle(10, 30)
    r2 = Rectangle(12, "2")

    def test_all_case(self):
        self.assertEqual(self.r1.id, 1)

    def test_attributes(self):
        self.assertEqual(self.r1.height, 30)
        self.assertEqual(self.r1.width, 10)
        self.assertEqual(self.r1.x, 0)
        self.assertEqual(self.r1.y, 0)
