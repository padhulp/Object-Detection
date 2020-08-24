

"""
Course:  Training YOLO v3 for Objects Detection with Custom Data

Section-4
Creating Custom Dataset in YOLO format
File: creating-train-and-test-txt-files.py modified to write all file names in a folder to a text file
Modify the input file path in the code below and run to create output filenames.txt 
Create File names as txt file
"""


# Creating files filenames.txt
# for training in Darknet framework
#
# Algorithm:


# Importing needed library
import os
import argparse

#set Params
ap = argparse.ArgumentParser()

ap.add_argument("-i", "--inputdir", required=True, help="Input file path")
ap.add_argument( "-o", "--outputDir", default=".",  help="Output file folder")

args = vars(ap.parse_args())

"""
Start of:
Setting up full path to directory with downloaded images
"""
# Enter full path nmae of directory with image and annotations files. 
full_path_to_images = args["inputdir"] 
#    '/home/paddy/mywork/yolo/data/augumentedJPGXML'

"""
End of:
Setting up full path to directory with downloaded images
"""


"""
Start of:
Getting list of full paths to downloaded images
"""

# Check point
# Getting the current directory
# print(os.getcwd())

# Changing the current directory
# to one with images
os.chdir(full_path_to_images)

# Check point
# Getting the current directory
# print(os.getcwd())

# Defining list to write paths in
p = []

# Using os.walk for going through all directories
# and files in them from the current directory
# Fullstop in os.walk('.') means the current directory
for current_dir, dirs, files in os.walk('.'):
    # Going through all files
    for f in files:
        # Checking if filename ends with '.jpg'
        if f.endswith('.jpg'):
            path_to_save_into_txt_files = full_path_to_images + '/' + f

            p.append(path_to_save_into_txt_files + '\n')


"""
End of:
Getting list of full paths to downloaded images
"""


"""
Start of:
Writing txt file with filenames
"""
# Creating file filenames.txt 
with open('filenames.txt', 'w') as file_txt:
    # Going through all elements of the list
    for e in p:
        # Writing current path at the end of the file
        file_txt.write(e)

"""
End of:
Creating filenames.txt
"""
