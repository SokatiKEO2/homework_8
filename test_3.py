import unittest
from exercise_3 import remove_all_after

class TestRemoveAllAfter(unittest.TestCase):
    
    def test_remove_all_after(self):
        self.assertEqual(remove_all_after([1, 2, 3, 4, 5], 3), [1, 2, 3])
        self.assertEqual(remove_all_after([1, 1, 2, 2, 3, 3], 2), [1, 1, 2])

        #edge cases
        # If cutting element not found, list shouldn't change
        self.assertEqual(remove_all_after([1, 2, 3, 4, 5], 6), [1, 2, 3, 4, 5])
        # If list is empty, it should remain empty
        self.assertEqual(remove_all_after([], 3), [])
        
if __name__ == '__main__':
    unittest.main()