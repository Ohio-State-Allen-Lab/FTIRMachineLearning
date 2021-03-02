# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 09:09:48 2020

@author: AbbieEnders
"""
import os
import shutil

cwd = r'C:\Users\abiga\ml_nist'
top_dir = ['nitrile','ketone','ether',
              'amine','amide','alkyne','alkane','alkene','alcohol',
              'nitro','alkyl_halide','acyl_halide','aldehyde']
for d in top_dir:
    shutil.copy(os.path.join(cwd,'updatedv2_batch_classify.py'), os.path.join(cwd,d))
    os.chdir(os.path.join(cwd, d))
    os.system('python updatedv2_batch_classify.py test_images '+d+'_10000-0.001_classify.csv')
