
import argparse
import lab02b_distance

parser = argparse.ArgumentParser()
# You may change the values of the arguments here (default) or in the commandline.
parser.add_argument("--height", default=1.8, type=float, help="Height of Gregor in meters.")
parser.add_argument("--distance", default=5, type=float, help="Gregor's distance from the camera.")
parser.add_argument("--f", default=1.7, type=float, help="Focal length in millimetres.")

def main(args : argparse.Namespace):
    # TODO: Consider the following parameters (some of which are in the arguments).
    # It is Gregor's name day and he had a photo of him taken. He is 1.8m tall
    # (args.height), he stands 5m from the camera (args.distance). The camera has
    # focal length 1.7mm (args.f). The camera sensor is 1/2'' (size 6.4x4.8mm)
    # and the resolution of the camera is 2048x1536 pixels (3Mpx).
    #
    # Answer the following questions:
    # 1) What is the distance between the lens and the sharp image of Gregor?
    # 2) What is the size of Gregor's image in mm?
    # 3) What is the size of one pixel in mm?
    # 4) What is the size of Gregor's image in pixels?
    # 5) How far does Gregor need to stand so that his image (height) has 500px?


    sharpDistance = 1/((1/args.f) - (1/(args.distance * 1000)))
    heighProj = args.height * sharpDistance / args.distance
    pixelSize = 6.4 / 2048
    heighPixel = heighProj / pixelSize


    #y ->|   a       a'
    #    ---------O-----
    #                  | <- y'

    # a' = f * (y'/y) + f
    
    # y'/y = a'/a
    # y' = y * a'/a
    # 5_000 = y * a'/a
    # a = y * a'/5_000
    # 1960.100000 = y * a'/5_000
    # 1960.100000 = 1_800 * a'/5_000 --> 5444,72222...

    #f * (y'/y) + f = a' --- y'= 500
    temp = args.f * (500 / args.height) + args.f # <-- a' pro vysku 500px
    targetDistance = args.height * temp / 500

    # 500 * pixelSize = args.height * sharpDistance / args.distance
    # args.distance * 500 * pixelSize = args.height * sharpDistance
    # args.distance = (args.height * sharpDistance) / (500 * pixelSize)

    # should be 1960.100000mm
    # 1960.1 = 1/((1/args.f) - (1/(args.distance * 1000)))

    # y'/y = a'/a
    # a'= a * y'/y
    # a = a' / y' * y

    # a' = f * (y'/y) + f
    aaHelper = args.f * (500 * pixelSize /args.height * 1000) + args.f
    print("{:.6f}mm".format(aaHelper))

    aa = aaHelper / (500 * pixelSize) * args.height
    print("{:.6f}mm".format(aa))

    # newSharp = 1.702
    # args.distance = (args.height * sharpDistance) / (500 * pixelSize)
    x = (args.height * 1000 * sharpDistance) / (500 * pixelSize)
    #print("{:.6f}mm".format(x))

    print("Distance between lens and the sharp image is {:.6f}mm".format(sharpDistance))
    print("Size of Gregor's image is {:.6f}mm".format(heighProj))
    print("One pixel has the size {:.6f}mm".format(pixelSize))
    print("Gregor's image in pixels is {:.6f}".format(heighPixel))
    print("Distance for image size of 500px is {:.6f}mm".format(targetDistance))

if __name__ == "__main__":
    args = parser.parse_args([] if "__file__" not in globals() else None)
    main(args)
