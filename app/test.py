import unittest
from grid import getOpposingCorners, getGrid
import numpy as np

class TestSum(unittest.TestCase):

    def test_getOpposingCorners(self):
        # attempt at random ordering
        rect = ((0,1), (0,0), (1,0), (1,1))
        topLeft, bottomRight = getOpposingCorners(rect)
        self.assertEqual(topLeft, (0,1))
        self.assertEqual(bottomRight, (1,0))
        # ensure that orientation relative to origin is not an issue
        rect = ((0,0), (-1,0), (-1,-1), (0,-1))
        topLeft, bottomRight = getOpposingCorners(rect)
        self.assertEqual(topLeft, (-1, 0))
        self.assertEqual(bottomRight, (0, -1))
    
    def test_getGrid(self):
        grid = getGrid((3,3), (-1, 1), (1, -1))
        expected_grid = np.array([
            [[-1, 1], [0, 1], [1, 1]],
            [[-1, 0], [0, 0], [1, 0]],
            [[-1, -1], [0, -1], [1, -1]]
        ])
        np.testing.assert_allclose(grid, expected_grid)

        grid = getGrid((3,3), (-1, 1), (1, -1))
        expected_grid = np.array([
            [[-1, 1], [0, 1], [1, 1]],
            [[-1, 0], [0, 0], [1, 0]],
            [[-1, -1], [0, -1], [1, -1]]
        ])

    def test_integration(self):
        rect = ((1,1), (-1,-1), (1,-1), (-1,1))
        dims = (3,3)
        topLeft, bottomRight = getOpposingCorners(rect)
        grid = getGrid(dims, topLeft, bottomRight)
        expected_grid = np.array([
            [[-1, 1], [0, 1], [1, 1]],
            [[-1, 0], [0, 0], [1, 0]],
            [[-1, -1], [0, -1], [1, -1]]
        ])
        np.testing.assert_allclose(grid, expected_grid)

if __name__ == '__main__':
    unittest.main()