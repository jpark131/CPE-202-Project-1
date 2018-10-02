import unittest
from bears import *

class TestAssign1(unittest.TestCase):
    def test_bear_true_values(self):
        self.assertTrue(bears(250))
        self.assertTrue(bears(42))
        self.assertTrue(bears(84))


    def test_bear_false_values(self):
        self.assertFalse(bears(53))
        self.assertFalse(bears(41))
        self.assertFalse(bears(12))
        self.assertFalse(bears(126))

    def test_bear_large_true_values(self):
        self.assertTrue(bears(1260))
        self.assertTrue(bears(420))
        self.assertTrue(bears(2520))

    def test_bear_large_false_values(self):
        self.assertFalse(bears(9000))
        self.assertFalse(bears(1314))
        self.assertFalse(bears(900))
        self.assertFalse(bears(6300))


if __name__ == "__main__":
    unittest.main()
