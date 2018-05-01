import unittest
from radio.radio import check_interval

class TestCheckInterval(unittest.TestCase):

    def test_within_limits(self):
        # Is within a 3% tolerance
        self.assertTrue(check_interval(1670, 1680))
        self.assertTrue(check_interval(3419, 3420))
        self.assertTrue(check_interval(7020, 7020))
        pass

    def test_exceeds_limits(self):
        # Exceeds in more than 3% from the requested duration
        self.assertFalse(check_interval(1740, 1680))
        self.assertFalse(check_interval(5000, 3420))
        self.assertFalse(check_interval(10000, 7020))
        pass

    def test_beneath_limits(self):
        # Is beneath in more than 3% from the requested duration
        self.assertFalse(check_interval(1000, 1680))
        self.assertFalse(check_interval(2500, 3420))
        self.assertFalse(check_interval(4000, 7020))
        pass

if __name__ == '__main__':
    unittest.main()
