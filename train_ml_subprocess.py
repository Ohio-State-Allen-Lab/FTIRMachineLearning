# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 20:14:05 2020

@author: AbbieEnders
"""

# run the machine learning for each compound
import os
import shutil

cwd = os.getcwd()
top_dir = ['nitrile','ketone','ether',
              'amine','amide','alkyne','alkane','alkene','alcohol',
              'nitro','alkyl_halide','acyl_halide']
for d in top_dir:
    #shutil.copytree(os.path.join(cwd,'scripts'), os.path.join(cwd,d,'scripts'))
    os.chdir(os.path.join(cwd, d))
    os.system('python scripts/retrain.py --image_dir functional_group --output_graph 10000-0.001_graph.pb'+
              ' --output_labels 10000-0.001_labels.txt --summaries_dir 10000-0.001_sum --how_many_training_steps'+
              ' 10000 --learning_rate 0.001 --architecture inception_v3')