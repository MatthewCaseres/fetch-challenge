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

def getGridFromOpposing(dims: Dimensions, topLeft: Point, bottomRight: Point) -> np.ndarray:
    """
    Take the topleft and bottomright corners and use numpy meshgrid api, reformat into the desired format.
    """
    nx, ny = dims
    (x1, y1), (x2, y2) = topLeft, bottomRight
    xgrid = np.linspace(x1, x2, nx)
    ygrid = np.linspace(y1, y2, ny)
    grid = np.meshgrid(xgrid, ygrid)
    grid = np.stack(grid, axis=2)
    return grid

def getGrid(dims: Dimensions, rect: Rectangle) -> np.ndarray:
    """
    get the opposing corners then use those to make the grid
    """
    topLeft, bottomRight = getOpposingCorners(rect)
    grid = getGridFromOpposing(dims, topLeft, bottomRight)
    return grid