import sys
import numpy
import cv2 as cv

# sys.argv[0] = script name
# sys.argv[1] = image file
# sys.argv[2] = width, in inches
# sys.argv[3] = height, in inches
def main():

    # check argument count
    if len(sys.argv) != 4:
        print("invalid number of arguments; argc = ", len(sys.argv))
        print("\tsys.argv[0] = script name")
        print("\tsys.argv[1] = image file")
        print("\tsys.argv[2] = width, in inches")
        print("\tsys.argv[3] = height, in inches")
        exit()

    # read in the specified image file
    image = cv.imread(sys.argv[1])

    if (not type(image) is numpy.ndarray):
        print("Invalid image file: ", sys.argv[1])
        exit()

    try:
        # retrieve the original dimensions. the underscore indicates a value were not interested in
        originalWidth, originalHeight =  image.shape
    except:
        try:
            originalWidth, originalHeight, _ =  image.shape
        except:
            print("unable to pull original dimensions for ", sys.argv[1])
            exit()

    # calculate new dimensions
    width = int(sys.argv[2]) * 96
    height = int(sys.argv[3]) * 96
    dimension = (width, height)

    # determine which interpolation to use
    if originalWidth < width and originalHeight < height:
        # were making the image larger 
        resizeType = cv.INTER_CUBIC   

    elif originalWidth > width and originalHeight > height:
        # were shrinking the image
        resizeType = cv.INTER_AREA

    else: 
        # stretching the image in some way
        resizeType = cv.INTER_AREA

    # create the resized image
    resized = cv.resize(image, dimension, interpolation=resizeType)

    # overwrite the original image file
    cv.imwrite(sys.argv[1], resized)

    print("Finished processing: ", sys.argv[1])

if __name__ == "__main__":
    main()
