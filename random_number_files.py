# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 14:14:59 2020

@author: AbbieEnders
"""
'''
###############################################################################
########################TO RUN IN THE CONSOLE #################################
###############################################################################
python random_number_files.py [path_to_directory_1] [path_to_directory_2] 
'''
# imports
import os
import sys
import random
import shutil

# randomly delete files in folder that has excess images
dir_1 = os.path.join(os.getcwd(), sys.argv[1]) #this should be POSITIVE\CONTAINING functional group for naming purposes
dir_2 = os.path.join(os.getcwd(), sys.argv[2]) #this should be NEGATIVE\NOT CONTAINING functional group for naming purposes
dest_dir = os.path.join(os.getcwd(), sys.argv[3])


len_dir_one = len(os.listdir(dir_1))
len_dir_two = len(os.listdir(dir_2))
num_of_validation_files = 5
i = 0
# first we will randomly move five files each to be used as validation files

while i < num_of_validation_files:
    print('Im here') #is this meaningful?
    f_d1 = os.path.join(dir_1, random.choice(os.listdir(dir_1))) # file for directory 1
    f_d2 = os.path.join(dir_2, random.choice(os.listdir(dir_2))) # file for directory 2
    shutil.move(f_d1, dest_dir)
    shutil.move(f_d2, dest_dir)
    i += 1
    
if len_dir_one > len_dir_two:
    # get difference of files in the two directories and remove random files to 
    # get the directories to equal lengths
    dif = len_dir_one - len_dir_two
    for file in random.sample(os.listdir(dir_1),dif):
        os.remove(os.path.join(dir_1,file))
elif len_dir_one < len_dir_two:
    # get difference of files in the two directories and remove random files to 
    # get the directories to equal lengths
    dif = len_dir_two - len_dir_one
    for file in random.sample(os.listdir(dir_2),dif):
        os.remove(os.path.join(dir_2, file))
else:
    exit()
