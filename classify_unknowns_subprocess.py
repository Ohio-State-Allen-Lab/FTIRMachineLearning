# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 14:22:27 2020

@author: AbbieEnders
"""

import os


cwd = r'C:\Users\abiga\ml_nist'
top_dir = ['nitrile','ketone','ether','ester','carboxylic_acid','aromatic',
              'amine','amide','alkyne','alkane','alkene','alcohol',
              'nitro','alkyl_halide','acyl_halide','methyl','aldehyde']
for d in top_dir:
    #shutil.copy(os.path.join(cwd,d+'_batch_classify.py'), os.path.join(cwd,d))
    os.chdir(os.path.join(cwd, d))
    os.system('python '+d+'_batch_classify.py unknowns '+d+'_1_unknown_classify.csv')
