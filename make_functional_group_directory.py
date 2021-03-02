# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 19:41:52 2020

@author: AbbieEnders
"""

import os
import sys
import shutil
# directory to create inside the original directory
target_dir = os.path.join(os.getcwd(), sys.argv[2], sys.argv[1])
move_dir1 = os.path.join(os.getcwd(), sys.argv[2], sys.argv[3])
move_dir2 = os.path.join(os.getcwd(), sys.argv[2], sys.argv[2])

os.mkdir(target_dir)
shutil.move(move_dir1, target_dir)
shutil.move(move_dir2, target_dir)
