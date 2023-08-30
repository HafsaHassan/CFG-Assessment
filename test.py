import unittest
from concept import check_isogram


class TestingIsogram(unittest.TestCase):
    def test_isogram(self):
        # Test case where string is isogram
        self.assertTrue(check_isogram("isogram"))

    def test_non_isogram(self):
        # Test case where string is not isogram
        self.assertFalse(check_isogram("hafsa"))

    def test_edge_case(self):
        # Edge cases
        self.assertTrue(check_isogram(""))
        self.assertFalse(check_isogram("Aa"))


if __name__ == '__main__':
    unittest.main()
