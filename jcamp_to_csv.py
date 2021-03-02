#!\usr\bin\env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 17:53:29 2020
@author: AbbieEnders
Using jcamp.py from GITHUB

#####################################################################################
########################NOTES########################################################
#####################################################################################
RUN IN COMMAND LINE: 1 ) python -m pip install git+https://github.com/nzhagen/jcamp
numpy version: pip install numpy==1.19.0
(install git, pip if you don't have it)
2) python jcamp_to_csv.py
#####################################################################################
"""
# read in jcampdx file to dict and write list to csv file
import jcamp
import os
import glob
import csv
import re
import sys

#This is where your data is coming from and going to

path = os.path.join(os.getcwd(), sys.argv[1])
#The following lines will find all of the files of a given type in the path's folder
extension = 'jdx'
os.chdir(path) #you are probably not moving the py file around, so just change directory to look\touch in correct folder
#Here are the files that fit your criterion that are within the path file
result = glob.glob('*.{}'.format(extension))
all_files = glob.glob(path + "\*.jdx")
for file in all_files:
    data = jcamp.JCAMP_reader(file)
    nfn = re.sub('.jdx','.csv',file) #nfn = new filename
    with open(nfn, 'w', newline = '') as f:
        writer = csv.writer(f, delimiter = ',')
        writer.writerow(('x','y'))
        writer.writerows(zip(data['x'], data['y']))

    if not f.closed:
        f.close()
