#!/usr/bin/python3
import unittest

from models.base import Base


class Test_almost_a_circle(unittest.TestCase):
    instance = Base()

    def test_id(self):
        self.assertEqual(isinstance.id, 1)
