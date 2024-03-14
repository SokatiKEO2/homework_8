import unittest
from exercise_2 import index_power

class TestIndexPower(unittest.TestCase):
    
    def test_index_power(self):
        self.assertEqual(index_power([1, 2, 3, 4], 2), 9)
        self.assertEqual(index_power([1, 3, 10, 100], 3), 1000000)
        self.assertEqual(index_power([0, 1], 0), 1)
        
        #edge case
        #return -1 when N is outside array
        self.assertEqual(index_power([1, 2], 3), -1)
        self.assertEqual(index_power([1, 2, 3], 3), -1)
        self.assertEqual(index_power([1, 2, 3], 5), -1)
        
if __name__ == '__main__':
    unittest.main()