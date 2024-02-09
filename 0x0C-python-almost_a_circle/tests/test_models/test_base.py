import unittest

from models.base import Base


class Test_almost_a_circle(unittest.TestCase):
    def test_base(self):
        self.assertEqual(Base(), 1)