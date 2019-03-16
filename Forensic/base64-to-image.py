# coding: utf-8
import base64
import argparse
import os
from sys import argv, exit
from types import *
import imghdr

#base64toimage -f file.txt -o /home/image

parser = argparse.ArgumentParser(description="Convert base64 string to image type based on input's firsts bytes.\nbase64toimage -f filename.txt -o path/to/output")
parser.add_argument("-f", "--filename", help="file containing Base64 string", type=str, required=True)
parser.add_argument("-o", "--output", help="save image to an output file | don't add extension", required=True)
args = parser.parse_args()


file_name = args.filename
path_name = args.output

# Open the source file and read in the base64 encoded data
try:
    source = open(file_name, 'r')
except IOError:
    print ("Unable to open {}.  Are you sure it's there?".format(file_name))
    exit()
else:
    b64_data = source.read()
    source.close()

# Convert the base64 data back to regular binary image data and figure out the image type (png, gif, jpg, etc)
image_data = base64.b64decode(b64_data)
image_type = imghdr.what('', image_data) #http://docs.w3cub.com/python~3.6/library/imghdr/#imghdr.what


# Create the image file and tell the user about it
destination_file_name = path_name + '.' + image_type

try:
    destination = open(destination_file_name, 'wb')
except IOError:
    print ("Unable to create image file. You might not have permission to create a file in this location.")
    exit()
else:
    destination.write(image_data)
    destination.close()
    print ("New image file: {}".format(destination_file_name))
