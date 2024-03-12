"""
Create a function that validates mean,median and variance
based on following set of rules:
"""

import unittest
from calculate_stats import calculate_stats


class TestStats(unittest.TestCase):
    """
    Usecases for Unit Test
    """
    def test1(self):
        """checking if stats are correct"""
        self.assertEqual(calculate_stats([10, 12, 23, 23, 16, 23, 21, 16]),(18.0, 18.5, 4.898979485566356))

    def test2(self):
        """checking if stats are correct"""
        self.assertEqual(calculate_stats([40, 72, 93, 0, 16, 23, 21, 16]),(35.125, 22.0, 29.67506318443147))
        
    def test3(self):
        """checking if error is raised"""
        with self.assertRaises(ValueError):
            calculate_stats([40])
    def test4(self):
        """checking if error is raised"""
        with self.assertRaises(ValueError):
            calculate_stats([])
            
    def test5(self):
        """checking if error is raised"""
        with self.assertRaises(ValueError):
            calculate_stats(['H'])



if __name__ == "__main__":
    unittest.main()
