import numpy as np

Dimensions = tuple[int, int]
Point = tuple[float, float]
Rectangle = tuple[Point, Point, Point, Point]

def getOpposingCorners(rect: Rectangle) -> tuple[Point, Point]:
    """
    Take in unordered points of a rectangle and return a pair of opposing corners.
    The opposing corners will be ordered (topleft, bottomright)
    """
    return min(rect, key=lambda x: (x[0], -x[1])), max(rect, key=lambda x: (x[0], -x[1]))

def getGrid(dims: Dimensions, topLeft: Point, bottomRight: Point) -> np.ndarray:
    """
    Use the meshgrid api to make the grid, reformat into the desired format.
    """
    nx, ny = dims
    (x1, y1), (x2, y2) = topLeft, bottomRight
    xgrid = np.linspace(x1, x2, nx)
    ygrid = np.linspace(y1, y2, ny)
    grid = np.meshgrid(xgrid, ygrid)
    grid = np.stack(grid, axis=2)
    return grid