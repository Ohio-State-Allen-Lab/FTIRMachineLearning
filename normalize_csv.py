#!\usr\bin\env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 19:27:00 2020
@author: AbbieEnders
Written by Nicole North, transfered to .py file by AE
Normalize csv data and save as a new csv file, preserving og data
"""
import pandas as pd
import numpy as np
import os
import glob
import csv
import re
import sys
import shutil
#This is where your data is coming from and going to
path = os.path.join(os.getcwd(), sys.argv[1])
dst = os.path.join(os.getcwd(), sys.argv[2])
#The following lines will find all of the files of a given type in the path's folder
extension = 'csv'
os.chdir(path)
result = glob.glob('*.{}'.format(extension))
#Here are the files that fit your criterion that are within the path file
li = []
for filename in result:
    #read in file
    df = pd.read_csv(filename, index_col=False, header=0)
    #rename file
    filename = re.sub('.csv','_n.csv',filename)
    #normalize with respect to max y value in file
    df['y']= (df['y']/np.amax(df['y']))
    li.append(df['y'])
    #write normalized files to a new csv
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file, delimiter = ',')
        writer.writerow(('cm-1', 'I'))
        writer.writerows(zip(df['x'],df['y']) )
    if not  file.closed:
        file.close()
    src = os.path.join(os.getcwd(), filename)
    dst = os.path.join(os.getcwd(), filename)
    shutil.move(src, dst)    
