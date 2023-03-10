
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d as mpl3
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

def createCube(xCenter : float, yCenter : float, zCenter: float, side : float) -> np.ndarray:
    """
    Generates coordinates of a cube positioned at '(xCenter, yCenter, zCenter)' with
    sides of length 'side'. The cube is centered on the specified position.

    The returned value has the shape (6, 4, 3) representing 6 faces X 4 vertices X 3 coordinates.
    Each side of the cube is separate object, no vertex reuse.

    Arguments:
    - 'xCenter' - X coordinate of the cube's centre.
    - 'yCenter' - Y coordinate of the cube's centre.
    - 'zCenter' - Z coordinate of the cube's centre.
    - 'side' - The length of the cube's side.

    Return:
    - Corner coordinates of the generated cube: (6 faces x 4 vertices x 3 coordinates).
    """
    coords = [
        [
            [0, 0, 0],
            [1, 0, 0],
            [1, 0, 1],
            [0, 0, 1]
        ],
        [
            [0, 0, 0],
            [0, 1, 0],
            [0, 1, 1],
            [0, 0, 1]
        ],
        [
            [0, 0, 1],
            [1, 0, 1],
            [1, 1, 1],
            [0, 1, 1]
        ],
        [
            [0, 0, 0],
            [1, 0, 0],
            [1, 1, 0],
            [0, 1, 0]
        ],
        [
            [0, 1, 0],
            [1, 1, 0],
            [1, 1, 1],
            [0, 1, 1]
        ],
        [
            [1, 0, 0],
            [1, 1, 0],
            [1, 1, 1],
            [1, 0, 1]
        ]
    ]
    coords = np.asarray(coords) - 0.5
    coords[:, :, 0] = side * coords[:, :, 0] + xCenter
    coords[:, :, 1] = side * coords[:, :, 1] + yCenter
    coords[:, :, 2] = side * coords[:, :, 2] + zCenter

    return coords

def drawCube3D(ax : mpl3.Axes3D, coords : np.ndarray, color : str, alpha : float = 0.8) -> None:
    """
    Draws a cube described by the given coordinates (in the form generated by 'createCube').
    Requires axes object 'ax' with active 3D projection. 'color' speicifes the colour of the cube.

    Arguments:
    - 'ax' - Axes3D object where the cube should be drawn.
    - 'coords' - Coordinates of the 3D polygons (N faces x K vertices x 3 coordinates).
    - 'color' - String name of the cube colour recognised by MatPlotLib.
    - 'alpha' - Opaqueness of the cube (lower value means more transparent).
    """
    face = Poly3DCollection(coords)
    face.set_facecolor(color)
    face.set_edgecolor('black')
    face.set_alpha(alpha)
    ax.add_collection3d(face)

def drawCube2D(ax : plt.Axes, xProjected : np.ndarray, yProjected : np.ndarray, color : str, alpha : float = 0.8) -> None:
    """
    Draws cube projection described by x and y coordiantes of the projected points 'xProjected', 'yProjected',
    The cube is drawn with the specified colour 'color' and transparency 'alpha'.

    Arguments:
    - 'ax' - Axes object where the 2D cube should be drawn.
    - 'xProjected' - X coordinates of the projected vertices of all faces.
    - 'yProjected' - Y coordinates of the projected vertices of all faces.
    - 'color' - Colour of the cube.
    - 'alpha' - Opaqueness of the cube (lower value means more transparent).
    """
    for j in range(6):
        ax.fill(xProjected[j, :], yProjected[j, :], color, edgecolor="black", alpha=alpha)
