import sys
import numpy
import cv2 as cv

# sys.argv[0] = script name
# sys.argv[1] = image file
# sys.argv[2] = dim?
# sys.argv[3] = dim?
def main():

    #check argument count
    if sys.argv.__sizeof__ != 4:
        print("invalid number of arguments")
        exit()

    image = cv.imread(sys.argv[1])
    result = cv.


if __name__ == "__main__":
    main()
