#!\usr\bin\env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 09:24:53 2020

@author: AbbieEnders
"""

#create a jpg of each spectrum

import pandas as pd
import matplotlib.pyplot as plt
import os
import glob
import re
import sys
#path to spectra csv files
path = os.path.join(os.getcwd(), sys.argv[1])

extension = 'csv' # extension of the file you are searching for
os.chdir(path) # change the working directory so you can access this from anywhere on your computer
result = glob.glob('*.{}'.format(extension))
#Here are the files that fit your criterion that are within the path file

for filename in result:
    df = pd.read_csv(filename, index_col=False, header=0)
    filename = re.sub('_n.csv','',filename)
    filename=filename+".jpg"
    fig = df.plot(df.columns[0], df.columns[1], color='black', legend=None)
    fig.set_xlabel(None)
    fig.set_xlim(4000, 600)
    plt.savefig(filename)
    plt.close()