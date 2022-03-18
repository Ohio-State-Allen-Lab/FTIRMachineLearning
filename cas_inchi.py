# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 17:28:01 2020

@author: AbbieEnders

#########################################################
################ TO RUN #################################
python cas_inchi.py --data_dir=data --cas_list=species.txt
"""
import os
import logging
import argparse
import sys

import pandas as pd 
import numpy as np

from rdkit import Chem, RDLogger
lg = RDLogger.logger()
lg.setLevel(RDLogger.CRITICAL)

from model.utils import set_logger
print('imports loaded')
func_grp_smarts = {'alkane':'[CX4;H0,H1,H2,H4]','methyl':'[CH3]','alkene':'[CX3]=[CX3]','alkyne':'[CX2]#C',
                   'alcohols':'[#6][OX2H]','amines':'[NX3;H2,H1;!$(NC=O)]', 'nitriles':'[NX1]#[CX2]', 
                   'aromatics':'[$([cX3](:*):*),$([cX2+](:*):*)]','alkyl halides':'[#6][F,Cl,Br,I]', 
                   'esters':'[#6][CX3](=O)[OX2H0][#6]', 'ketones':'[#6][CX3](=O)[#6]','aldehydes':'[CX3H1](=O)[#6]', 
                   'carboxylic acids':'[CX3](=O)[OX2H1]', 'ether': '[OD2]([#6])[#6]','acyl halides':'[CX3](=[OX1])[F,Cl,Br,I]',
                   'amides':'[NX3][CX3](=[OX1])[#6]','nitro':'[$([NX3](=O)=O),$([NX3+](=O)[O-])][!#8]'}




def identify_functional_groups(inchi):
    '''Identify the presence of functional groups present in molecule 
       denoted by inchi

    Args:
        root: (string) path to spectra data
        files: (list) jdx files present in root
        save_path: (string) path to store csv file
        bins: (np.array) used for standardizing
        is_mass: (bool) whether data being parsed is Mass or IR

    Returns:
        mol_func_groups: (list) contains binary values of functional groups presence
                          None if inchi to molecule conversion returns warning or error
    '''
    
    try:
        #Convert inchi to molecule
        mol = Chem.MolFromInchi(inchi, treatWarningAsError=True)   
        mol_func_grps = []

        #populate the list with binary values
        for _, func_struct in func_grp_structs.items():
            struct_matches = mol.GetSubstructMatches(func_struct)
            contains_func_grp = int(len(struct_matches)>0)
            mol_func_grps.append(contains_func_grp)
        return mol_func_grps
    except:

        return None
    
def save_target_to_csv(cas_inchi_df, save_path):
    '''Save the target dataframe as csv to path

    Args:
        cas_inchi_df: (pd.DataFrame) contains CAS and Inchi of molecules
        save_path: (string) path to store csv file

    Returns:
        None
    '''
    column_names = list(func_grp_structs.keys())    
    target_df = pd.DataFrame(index = cas_inchi_df.index, columns = column_names)

    #Iterate the rows, don't use df.apply since a list is being returned.
    for ind, (_, row) in enumerate(cas_inchi_df.iterrows()):
        target_df.iloc[ind, :] = identify_functional_groups(row['inchi'])
    

    target_df.dropna(inplace = True)
    target_df.to_csv(save_path)


if __name__ == '__main__':

    #Parsing the data from jdx and storing it in csv

    parser = argparse.ArgumentParser()
    parser.add_argument('--data_dir', default= './data',\
        help = "Directory path containing scrapped data")
    parser.add_argument('--cas_list', default= 'species.txt',\
        help = "File containing CAS number and smiles of molecules")

    args = parser.parse_args()

    data_dir = args.data_dir
    set_logger(data_dir, 'prepare_data.log')
    
    logging.info('Computing the structures of functional groups')
    func_grp_structs = {func_name : Chem.MolFromSmarts(func_smarts)\
                        for func_name, func_smarts in func_grp_smarts.items()}
    print('funcgrpstruct')
    
    inchi_path = os.path.join(data_dir, 'inchi.txt')
    logging.info('Loading inchi file from {}'.format(inchi_path))
    inchi_df = pd.read_csv(inchi_path, sep='\t', header = 0, usecols = [0,1],\
                        names = ['cas','inchi'], dtype = str)
    inchi_df.dropna(inplace = True)
    inchi_df.set_index('cas', inplace = True)
    
    # Create and save csv of target 
    target_path = os.path.join(data_dir, 'target.csv')
    logging.info('Creating target csv dataset in {}'.format(target_path))
    save_target_to_csv(inchi_df, target_path)