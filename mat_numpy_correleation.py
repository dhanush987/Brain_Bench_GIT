import scipy.io as sio
import h5py
import numpy as np
from scipy.stats.stats import pearsonr
import sys

#For data science file.

outfile = '/Users/Dhanush/Desktop/Projects/Brain_Bench/GIT_DATA/Michell_Data/NewNumpy/'
infile = '/Users/Dhanush/Desktop/Projects/Brain_Bench/GIT_DATA/Michell_Data/MRI_VoxelDone/'
#infile ='/Users/Dhanush/Desktop/Projects/Brain_Bench/GIT_DATA/Meg_data/MEG_VoxelDone/'
subjs1 = ['P1','P2','P3','P4','P5','P6','P7','P8','P9']
#subjs1 = ['A','B','C','D','E','F','G','I','J'];
length = 60

"""
# For Anderson Data
outfile = '/Users/Dhanush/Desktop/Projects/Brain_Bench/GIT_DATA/Anderson_Data/NewNumpy/'
infile = '/Users/Dhanush/Desktop/Projects/Brain_Bench/GIT_DATA/Anderson_Data/MRI_VoxelDone/'
subjs1 = ['P1','P2','P3','P4','P5','P6','P7','P8','P9']
length = 70
"""

"""
# For EEG data
outfile = '/Users/Dhanush/Desktop/Projects/Brain_Bench/GIT_DATA/EEG_data/NewNumpy/'
infile ='/Users/Dhanush/Desktop/Projects/Brain_Bench/GIT_DATA/EEG_data/EEG_VoxelDone/'
subjs1 = ['A','B','C','D','E','F','G'];
length = 60
"""
def getindex(ind,k):
	for i in range(30):
		if ind[i] ==k:
			return ind[i]

for i in range(9):
	file_in = infile + str(subjs1[i]) +'_voxselected.mat'
	print file_in
	S1 = h5py.File(file_in)
	#Brain_data = S1['data'][()].transpose()
	Brain_data = S1['data'][()].transpose()
	print Brain_data.shape
	
	#TEMPORARY CODE ADDED HERE TO SORT THE BRAIN DATA FOR ITALIAN FMRI
	"""
	data_sorted = np.empty(shape=[70, Brain_data.shape[1]])	
	ind =[0,3,1,4,6,7,14,15,16,17,18,66,52,43,29,19,60,21,45,\
	13,37,27,28,30,32,23,24,25,35,5,34,36,54,39,40,41,42,11,46,31,50,12,20,49,51,\
	53,56,55,64,59,8,9,26,2,10,58,44,47,57,62,61,22,33,65,48,67,38,68,69,63]
	print len(ind)
	z = 0
	for k in range(70):
		data_sorted[z,:]= Brain_data[ind[k]]
		z+=1
	Brain_data = data_sorted
	Brain_data.shape
	"""
	"""
	#for concrete only words#

	data_sorted = np.empty(shape=[30, Brain_data.shape[1]])
	ind =[4,15,17,66,29,19,60,45,13,37,23,5,40,42,11,46,50,12,51,64,8,26,44,\
	62,61,33,67,38,69,63]
	z = 0
	for k in range(30):
			data_sorted[z,:]= Brain_data[ind[k],:]
			z+=1
	Brain_data = data_sorted
	print Brain_data.shape
	"""
	"""
	# for Abstract words for Anderson
	
	data_sorted = np.empty(shape=[40, Brain_data.shape[1]])
	ind =[0,3,1,6,7,14,16,18,52,43,21,\
	27,28,30,32,24,25,35,34,36,54,39,41,31,20,49,\
	53,56,55,59,9,2,10,58,47,57,22,65,48,68]
	print len(ind)
	z = 0
	for k in range(40):
			data_sorted[z,:]= Brain_data[ind[k],:]
			z+=1
	Brain_data = data_sorted
	print Brain_data.shape
	"""

	"""
	#TEMPORARY CODE ADDED HERE TO SORT THE BRAIN DATA FOR EEG Data
	data_sorted = np.empty(shape=[60, Brain_data.shape[1]])	
	ind =[31,1,2,32,3,4,5,6,7,33,8,9,34,35,10,11,36,12,37,38,13,14,39,40,15,16,17,18,19,20,\
	21,52,22,23,24,41,25,42,43,26,44,45,46,47,48,49,50,51,27,53,54,55,56,57,58,28,59,29,60,30]
	print len(ind)
	z = 0
	for k in range(60):
		data_sorted[z,:]= Brain_data[ind[k]-1]
		z+=1
	Brain_data = data_sorted
	Brain_data.shape
	"""
	# Pearson correlation
	input_mat = np.empty((length, length))		
	input_mat.fill(0)						# initialize the mattrix made by input word vector
  
	# calculating correlation and generate the mattrix
	for word1 in range (0,length):
		vector1 = Brain_data[word1]
		for word2 in range (0,length):
			vector2 = Brain_data[word2]
			#print vector1
			#print vector2
			input_mat[word1][word2] = pearsonr(vector1, vector2)[0]
	# print (input_mat)	
	print input_mat.shape
	np.save(outfile+str(subjs1[i])+'_MRI.npy', input_mat)





