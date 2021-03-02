# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 12:54:59 2020

@author: AbbieEnders
"""

# move csv files to new folder

import shutil
import os
import sys
import glob
extension = '.csv' # file format
og = os.path.join(os.getcwd(), sys.argv[1]) # original 
new = os.path.join(os.getcwd(), sys.argv[2]) # destination
os.chdir(og) # change directory
# get all of the files in the folder that match the extension
results = glob.glob('*.{}'.format(extension)) 
for file in results:
    og = os.path.join(og, file)
    new = os.path.join(new, file)
    shutil.move(og, new) # move