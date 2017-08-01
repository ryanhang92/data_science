import time
import scipy.io as sio
import numpy as np
import os
from sklearn import svm
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import cross_val_score

start_time = time.time()

path = os.getcwd()

#Problem 1 - SVM
#Reference http://scikit-learn.org/stable/modules/svm.html

#Import the data from matlab
dataPath = path + '/digit-dataset/train.mat';
digitData = sio.loadmat(dataPath)

#Prepare data for svm input - Imported in ndarray format
featureMatrix = digitData['train_images']
labelMatrix = digitData['train_labels']
feature_count = featureMatrix.shape[0] * featureMatrix.shape[1]
sample_count = featureMatrix.shape[2]

trainingData = np.transpose(featureMatrix.reshape(feature_count, sample_count)) #A correct 60000, by 28*28 Matrix
labelData = labelMatrix.reshape(sample_count,)

#Shuffle the data
perm = np.random.permutation(sample_count)
datas = trainingData[perm]
labels = labelData[perm]