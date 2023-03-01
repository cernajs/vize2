import argparse
from typing import Tuple
import numpy as np
import matplotlib.pyplot as plt
import lab02_help

parser = argparse.ArgumentParser()
# You may change the values of the arguments here (default) or in the commandline.
parser.add_argument("--seed", default=None, type=int, help="Seed for RNG.")
parser.add_argument("--f", default=1, type=float, help="Focal length of the camera in millimetres.")

def projection(f : float, xCoords : np.ndarray, yCoords : np.ndarray, zCoords : np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    # TODO: Implement the body of this function so that is computes the perspective
    # projection of a pin-hole camera onto an image plane. Matrices 'xCoords', 'yCoords'
    # and 'zCoords' contain the coordinates of points in 3D. Finally, 'f' is the focal
    # length (the distance from the image plane).
    
    xProjected = xCoords * f / zCoords
    yProjected = yCoords * f / zCoords
    return xProjected, yProjected

def main(args : argparse.Namespace):
    # NOTE: Create a scene consisitng of cubes with varying sizes and positions.
    # Project the scene using pin-hole camera (the function 'projection'). Create
    # the cubes in a cycle with random parameters using the following generator.
    generator = np.random.RandomState(args.seed)

    # NOTE: Use methods 'lab02help.createCube', 'lab02help.drawCube3D' and
    # 'lab02help.drawCube2D' to create and draw 3D and 2D cube objects.
    fig = plt.figure("Cubes", figsize=(10, 6))
    ax3d = fig.add_subplot(121, projection='3d')
    ax3d.set_title("3D scene")
    ax2d = fig.add_subplot(122, aspect="equal")
    ax2d.set_title("2D projection of the scene")
    colors = ["cyan", "red", "blue", "green", "magenta", "purple", "violet", "yellow", "azure", "tomato"]
    # TODO: Generate, draw 3D, project and draw 2D cubes accoridng to the following example ...
    # - Use for loop and 'generator.randint(a)' to create and draw 10 different cubes.
    
    for i in range(len(colors)):
        xc, yc, zc = generator.randint(40) - 10, generator.randint(40) - 20, -120
        side = generator.randint(25) + 1
        coords = lab02_help.createCube(xc, yc, zc, side)
        lab02_help.drawCube3D(ax3d, coords, colors[i])
        xp, yp = projection(args.f, coords[:, :, 0], coords[:, :, 1], coords[:, :, 2])
        lab02_help.drawCube2D(ax2d, xp, yp, colors[i])

    """
    xc, yc, zc = 0, 0, -120
    side = 10
    coords = lab02_help.createCube(xc, yc, zc, side)
    lab02_help.drawCube3D(ax3d, coords, colors[0])
    xp, yp = projection(args.f, coords[:, :, 0], coords[:, :, 1], coords[:, :, 2])
    lab02_help.drawCube2D(ax2d, xp, yp, colors[0])
    """
    # TODO: Set the 3D axes limits to minimum/maximum of your cubes.
    # - Set them to minimum/maximum numbers you can generate, e.g., ((generator.randint(10) - 3) * 5) has range [-15, 30]
    # - I wasn't able to force matplotlib to do this automatically.
    ax3d.set_xlim3d([-40, 40])
    ax3d.set_ylim3d([-40, 40])
    ax3d.set_zlim3d([-80, -160])
    fig.tight_layout()
    plt.show()

if __name__ == "__main__":
    args = parser.parse_args([] if "__file__" not in globals() else None)
    main(args)
