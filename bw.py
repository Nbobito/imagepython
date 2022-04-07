# created in 2022 by Nathan Galley
# converts an image into black and white
# binary

import sys
from time import sleep
from PIL import Image
import numpy
import textwrap



file_name = input ("What is the name of the image file you want to convert? \n")
image = ""


try:
    image = Image.open(file_name)
except:
    print ("File not found.")
    sys.exit()

# uncomment for grayscale
# image_bw = image.convert ("L")
# grayscale = True

# uncomment for non grayscale
image_bw = image.convert ("1")
grayscale = False


image_array = numpy.array (image_bw, dtype=numpy.uint8)


out = ""
threshhold = 255/2

# this for loop uses index instead of the array itself
# so it can modify the individual pixels
for row in range(0, len(image_array)):
    for pixel in range(0, len(image_array[row])):
        if (grayscale and (image_array[row][pixel] > threshhold)) or (not grayscale and image_array[row][pixel]):
            out += "1"
            image_array[row][pixel] = 255
        else:
            out += "0"
            image_array[row][pixel] = 0
out = '\n'.join (textwrap.wrap(out, 8))


print ("Created file " + file_name.split(".")[0] + "_bw_binary.txt")

with open(file_name.split(".")[0] + "_bw_binary.txt", "w+") as output_file:
    output_file.write("Height: " + str(len(image_array)) + "\n")
    output_file.write("Width : " + str(len(image_array[0])) + "\n")
    output_file.write("=======================================" + "\n")
    output_file.write(file_name + "\n")
    output_file.write("=======================================" + "\n")
    output_file.write(out)


preview = Image.fromarray(image_array)
preview.show()


print ("Finished!")
sys.exit()