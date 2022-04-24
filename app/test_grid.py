from .grid import getGridFromOpposing, getOpposingCorners, getGrid
import numpy as np

def test_getOpposingCorners():
    # attempt at random ordering
    rect = ((0,1), (0,0), (1,0), (1,1))
    topLeft, bottomRight = getOpposingCorners(rect)
    assert topLeft == (0,1)
    assert bottomRight == (1,0)
    # ensure that orientation relative to origin is not an issue
    rect = ((0,0), (-1,0), (-1,-1), (0,-1))
    topLeft, bottomRight = getOpposingCorners(rect)
    assert topLeft == (-1, 0)
    assert bottomRight == (0, -1)

def test_getGridFromOpposing():
    grid = getGridFromOpposing((3,3), (-1, 1), (1, -1))
    expected_grid = np.array([
        [[-1, 1], [0, 1], [1, 1]],
        [[-1, 0], [0, 0], [1, 0]],
        [[-1, -1], [0, -1], [1, -1]]
    ])
    np.testing.assert_allclose(grid, expected_grid)

def test_getGrid():
    rect = ((1,1), (-1,-1), (1,-1), (-1,1))
    dims = (3,3)
    grid = getGrid(dims, rect)
    expected_grid = np.array([
        [[-1, 1], [0, 1], [1, 1]],
        [[-1, 0], [0, 0], [1, 0]],
        [[-1, -1], [0, -1], [1, -1]]
    ])
    np.testing.assert_allclose(grid, expected_grid)