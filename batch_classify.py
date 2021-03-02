# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 08:37:12 2020

@author: AbbieEnders
"""

import tensorflow as tf, sys
import csv
from os import walk
import numpy as np

image_dir = sys.argv[1]
output_file = sys.argv[2]
graph_path = 'graph.pb'
labels_path = 'labels.txt'

#Create list of files in given directory
image_list = []
for (dirpath, dirnames, filenames) in walk(image_dir):
	image_list.extend(filenames)
	break
#Open output (.csv) file to be written to 
csv_header = ['Image Name', 'Containing Fn Group', 'Not Containing Fn Group']
with open(output_file, 'w') as csvFile:
	writer = csv.writer(csvFile)
	writer.writerow(csv_header)
	csvFile.close()

for image_path in image_list:
	# Read in the image_data
	image_name =  image_path 		# save image name for column
	image_path = image_dir + '/' + image_path #TEST: build correct img path 
	image_data = tf.gfile.FastGFile(image_path, 'rb').read()

	# Loads label file, strips off carriage return
	label_lines = [line.rstrip() for line
		in tf.gfile.GFile(labels_path)]

	# Unpersists graph from file
	with tf.gfile.FastGFile(graph_path, 'rb') as f:
		graph_def = tf.GraphDef()
		graph_def.ParseFromString(f.read())
		_ = tf.import_graph_def(graph_def, name='')

	# Feed the image_data as input to the graph and get first prediction
	with tf.Session() as sess:
		softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')
		predictions = sess.run(softmax_tensor,
		{'DecodeJpeg/contents:0': image_data})
    	# Sort to show labels of first prediction in order of confidence. Later, sorted by image name.
		top_k = predictions[0].argsort()[-len(predictions[0]):][::-1] 
		score_list = [[]]					# Clear list 
		score_list[0].append(image_name)

		for node_id in np.sort(top_k):
			human_string = label_lines[int(node_id)]
			score = predictions[0][int(node_id)]
			score = format(score, '.5f') 			#Format score
			print('TEST----------------------') 
			score_list[0].append(score)
			# print('%s (score = %.5f)' % (human_string, score))
		with open(output_file, 'a') as csvFile:
			writer = csv.writer(csvFile)
			writer.writerows(score_list)
			csvFile.close()
		image_path = ' '

# Ensure output file is properly closed
if not csvFile.closed:
	csvFile.close()