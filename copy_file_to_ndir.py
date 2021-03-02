#!\usr\bin\env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 09:09:56 2020

@author: AbbieEnders
"""
# move files based on the functional group present
from shutil import copyfile
import csv
import re
import glob
import os
import sys
#path to spectra csv files

path = os.path.join(os.getcwd(), sys.argv[1])
path_to_list = os.path.join(os.getcwd(), sys.argv[2])
dst = os.path.join(os.getcwd(), sys.argv[3])

# read list from file with names of files containing or not containing a functional group
with open(path_to_list, newline='') as f:
    reader = csv.reader(f)
    filenames = list(reader)
os.chdir(path)
extension = 'jpg' # extension of the file you are searching for

#results = glob.glob(path + extension)
#print(results)
os.chdir(path)
results = glob.glob('*.{}'.format(extension))
print(results)
#Here are the files that fit your criterion that are within the path file

for file in filenames:
    file = str(file)
    file = re.sub('\[','',file)
    file = re.sub('\'','',file) 
    file = re.sub('\]','',file)
    file = file+'.jpg'
    if file in results:
        print('file in list')
        src = os.path.join(path, file)
        dest = os.path.join(dst, file)
        print(dest)
        copyfile(src, dest)