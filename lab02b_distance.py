
import argparse
import numpy as np
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser()
# You may change the values of the arguments here (default) or in the commandline.
parser.add_argument("--f", default=30, type=float, help="Focal length of the camera in millimetres.")
parser.add_argument("--height", default=100, type=float, help="Height of an object in millimetres.")

def ccdDistance(f : float, objDistance : float) -> float:
    # TODO: Implement the body of this function so that it computes
    # the distance of the image plane, such that the image of
    # an object at distance 'objDistance' would be sharp
    # (without blur). Use the equation for a thin lens (from slides).
    return 1/((1/f) - (1/objDistance))

def main(args : argparse.Namespace):
    # TODO: Implement the function 'ccdDistance'.
    # Then, use this function to compute the ideal position of a sensor for an object
    # at distances: 45mm, 60mm, 10cm, 1m and 5m from the lens.
    # - The focal length of the camera is 30mm ('args.f').
    distances = np.array([45, 60, 100, 1000, 5000])
    ccdDistances = ccdDistance(args.f, distances)

    for i in range(len(distances)):
        print("Ideal CCD distance for object at {}mm is {:.6f}mm".format(distances[i], ccdDistances[i]))

    # TODO: What is the size of an object's image providing the object is
    # 10cm tall ('args.height') and placed at the individual positions investigated above.
    heightProjected = args.height * ccdDistances / distances
    
    # TODO: Plot a graph showing the dependency of image distance on object
    # distance.
    fig, ax = plt.subplots(1, 1, figsize=(6, 7))
    ax.plot(distances, ccdDistances)
    ax.set_xlabel("Object distance")
    ax.set_ylabel("Image distance")
    fig.tight_layout()
    plt.show()

if __name__ == "__main__":
    args = parser.parse_args([] if "__file__" not in globals() else None)
    main(args)
