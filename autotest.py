import unittest
from dumbcode import square, cube
class powertestcase(unittest.TestCase):
    def test_square(self):
        self.assertEqual(square(3), 9)
    def test_cube(self):    
        self.assertEqual(cube(3), 27)
if __name__ == "__main__":
    unittest.main()