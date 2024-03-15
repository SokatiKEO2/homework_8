import unittest
from exercise_5 import reverse_ascending

class TestReverseAscending(unittest.TestCase):
    
    def test_reverse_ascending(self):
        self.assertEqual(reverse_ascending([1, 2, 3, 4, 5]), ([5, 4, 3, 2, 1]))
        self.assertEqual(reverse_ascending([5, 7, 10, 4, 2, 7, 8, 1, 3]), [10, 7, 5, 4, 8, 7, 2, 3, 1])
        self.assertEqual(reverse_ascending([5, 4, 3, 2, 1]),  [5, 4, 3, 2, 1])
        self.assertEqual(reverse_ascending([1, 2, 1, 2, 1, 2, 1, 2]),  [2, 1, 2, 1, 2, 1, 2, 1])

        #edge cases
        # Empty list
        self.assertEqual(reverse_ascending([]),  [])
        # One element
        self.assertEqual(reverse_ascending([5]), [5])
        
        
if __name__ == '__main__':
    unittest.main()