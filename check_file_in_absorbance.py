# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 17:19:16 2020

@author: AbbieEnders
"""

import jcamp
import os
import glob
import shutil
import sys
# This is where your data is coming from and going to
# The following lines will find all of the files of a given type in the path's folder

path = os.path.join(os.getcwd(), sys.argv[1])
destination = os.path.join(os.getcwd(), sys.argv[2])
final_dest = os.path.join(os.getcwd(), sys.argv[3])
# you are probably not moving the py file around, so just change directory to look\touch in correct folder
# Here are the files that fit your criterion that are within the path file

extension = 'jdx'
all_files = glob.glob(path + "\*.jdx")
# read jcampdx file and check absorbance and wavenumbers units
# return false if not in micrometers (wavenumbers does not equal micrometers = True)
# return false if not in absorbance (y-units in absorbance = True)

for file in all_files:
    data = jcamp.JCAMP_reader(file)
    wavenumbers = data.get('x_units', r'N\A').lower() != 'micrometers'
    absorbance = data.get('yunits', r'N\A').lower() == 'absorbance'
    # move file if wavenumbers is in micrometers
    
    if wavenumbers == False:
        print('bad apple')
        shutil.move(file, destination)
    
    # move file if not in absorbance
    if absorbance == False:
        shutil.move(file,final_dest)
       