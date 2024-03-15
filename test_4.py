import unittest
from exercise_4 import chunking_by

class TestChunkingBy(unittest.TestCase):
    
    def test_chunking_by(self):
        self.assertEqual(chunking_by([5, 4, 7, 3, 4, 5, 4], 3), [[5, 4, 7], [3, 4, 5], [4]])
        self.assertEqual(chunking_by([3, 4, 5], 1), [[3], [4], [5]])
        self.assertEqual(chunking_by([1, 2, 3], 3), [[1, 2, 3]])
        self.assertEqual(chunking_by([5, 4, 7, 3, 4, 5, 4], 3), [[5, 4, 7], [3, 4, 5], [4]])

        #edge cases
        # Empty list
        self.assertEqual(chunking_by([], 2), [])
        
if __name__ == '__main__':
    unittest.main()