#####Author: Abbie Enders#######
# Modified from CANDIY-NIST Code
# November 17 2020
################################
######### TO RUN ###############################################################################
# python get_jdx.py --save_dir = './data/' --cas_list=species.txt --get_IR=true --get_inchi=true
################################################################################################

import os
import requests, urllib
import argparse
import pandas as pd 
from model.utils import set_logger

nist_url = "https://webbook.nist.gov/cgi/cbook.cgi"

def get_data(cas_ls, params, data_dir):
	'''Collect data from NIST database and store them in jdx format.

    Args:
        cas_ls: (list) CAS ids to download data for
		params: (dict) queries to be added to url
		data_dir: (string) path to store the data

    Returns:
        None
    '''	
	#Create directory for the relevant spetra 
	spectra_path = os.path.join(data_dir, params['Type'].lower(), '')
	if not os.path.exists(spectra_path):
		os.makedirs(spectra_path)
	for cas_id in cas_ls:
		params['JCAMP'] = 'C' + cas_id
		response = requests.get(nist_url, params=params)
		if response.text == '##TITLE=Spectrum not found.\n##END=\n':
			continue
		with open(spectra_path +cas_id +'.jdx', 'wb') as data:
			data.write(response.content)

def get_inchi(cas_ls, params, data_dir):
	'''Collect Inchi keys from NIST database and store them in txt format.

    Args:
        cas_ls: (list) CAS ids to download data for
		params: (dict) queries to be added to url
		data_dir: (string) path to store the data

    Returns:
        None
    '''	
	#Create file path for storing inchi keys
	inchi_path = os.path.join(data_dir, 'inchi.txt')
	with open(inchi_path,'a') as file:
		content = '{}\t{}\n'.format('cas_id', 'inchi')
		file.write(content)
		for cas_id in cas_ls:
			params['GetInChI'] = 'C' + cas_id
			response = requests.get(nist_url, params=params)
			content = '{}\t{}\n'.format(cas_id,response.content.decode("utf-8"))
			file.write(content)
			
parser = argparse.ArgumentParser()
parser.add_argument('--save_dir', default= './data',\
     help = "Directory path to store scrapped data")
parser.add_argument('--cas_list', default= 'species.txt',\
    help = "File containing CAS number and formula of molecules")
parser.add_argument('--get_IR', default= True,\
    help = "Whether to download IR or not")
parser.add_argument('--get_inchi', default= True,\
    help = "Whether to download InChi or not")

args = parser.parse_args()

#Check if file containing CAS ids exist
assert os.path.isfile(args.cas_list),"No file named {} exists".format(args.cas_list)

#Create data directory to store logs and spectra
data_dir = args.save_dir
if not os.path.exists(data_dir):
	os.makedirs(data_dir)

#Obtain CAS ids used for downloading the content from NIST
cas_df = pd.read_csv(args.cas_list, sep='\t', names = ['name', 'formula', 'cas'], header = 0)
cas_df.dropna(subset=['cas'], inplace=True)
cas_df.cas = cas_df.cas.str.replace('-', '')

cas_ids = list(cas_df.cas)

if args.get_IR:
	params={'JCAMP': '', 'Type': 'IR', 'Index': 0}	
	get_data(cas_ids, params, data_dir)

if args.get_inchi:
	params={}
	get_inchi(cas_ids, params, data_dir)
