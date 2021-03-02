# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 09:46:55 2020

@author: AbbieEnders
"""
#IMPORTS 
import subprocess
import os

# here we will call on each of our processes
# Step X: Run X 
# subprocess.run(['python', 'filename.py'], shell=True)
#VARIABLES
path = 'jcamp_files'
bad_path_1 = 'cond_not_met'
bad_path_2 = 'in_trans'
path_to_csv = 'unnormalized_csv'
path_to_dest = 'csv'
path_to_images = 'images'
ext_1 = '/*.csv'
ext_2 = '/*_n.csv'
ext_3 = '/*.jpg'
top_dir = ['nitrile','ketone','ether','ester','carboxylic_acid','aromatic',
              'amine','amide','alkyne','alkane','alkene','alcohol',
              'nitro','alkyl_halide','acyl_halide','methyl','aldehyde']
func_groups = ['nitrile','ketone','ether','ester','carboxylic_acid','aromatic',
              'amine','amide','alkyne','alkane','alkene','alcohol',
              'nitro','alkyl_halide','acyl_halide','methyl','aldehyde',
              'not_nitrile','not_ketone','not_ether','not_ester','not_carboxylic_acid','not_aromatic',
              'not_amine','not_amide','not_alkyne','not_alkane','not_alkene','not_alcohol',
              'not_nitro','not_alkyl_halide','not_acyl_halide','not_methyl','not_aldehyde']


# Step #1: Create directories if they don't exist
for i in top_dir:
    if not os.path.exists(top_dir):
        os.mkdir(os.path.join(top_dir, top_dir))
        not_dir = 'not_'+top_dir
        os.mkdir(os.path.join(top_dir, not_dir))

# Step #2: Move any files that are not in absorbance\wavenumbers
subprocess.run(['python', 'check_file_in_absorbance.py', path, bad_path_1, bad_path_2])

# Step #3: convert from jcampdx to csv
subprocess.run(['python', 'jcamp_to_csv.py', path])

# Step #4: move csv to their own folder
subprocess.run(['python', 'move_file.py', path, path_to_csv, ext_1])

# Step #5: normalize each spectrum
subprocess.run(['python', 'normalize_csv.py', path_to_csv, path_to_dest])

# Step #6: move normalized spectrum
subprocess.run(['python', 'move_file.py', path, path_to_csv, ext_2])

# Step #7: turn each csv file into a jpg image
subprocess.run(['python','convert_to_jpg.py',path_to_dest])

# Step #8: move jpg images
subprocess.run(['python', 'move_file.py', path_to_dest, path_to_images, ext_3])

# Step #9: copy files to the folder for functional groups
for d in top_dir:
    dst_for_images = d
    #for fg in func_groups:
    listname = d+'.csv'
    dst_for_images = os.path.join(d, d)
    subprocess.call(['python','copy_file_to_ndir.py', path_to_images, listname, dst_for_images], shell=True)
    # then do the same but for "not_X"
    listname = 'not_'+d+'.csv'
    dst_for_images = os.path.join(d, 'not_'+d)
    subprocess.call(['python','copy_file_to_ndir.py', path_to_images, listname, dst_for_images], shell=True)

# Step #10: "even" out folders and remove files for validation
for d in top_dir:
    dst_for_images1 = os.path.join(os.getcwd(), d, d)
    n = 'not_'+d
    dst_for_images2 = os.path.join(os.getcwd(), d, n)
    val = 'test_images'
    dst_for_val = os.path.join(os.getcwd(), d, val)
    # dst_for_val = d+'\test_images'
    subprocess.call(['python','random_number_files.py', dst_for_images1, dst_for_images2, dst_for_val], shell=True)

# Step 11: create functional group directory in each functional group's directory to move photo directories to
for direc in top_dir:
    d = direc
    n = 'not_'+d
    subprocess.call(['python', 'make_functional_group_directory.py', 'functional_group', d, n])
