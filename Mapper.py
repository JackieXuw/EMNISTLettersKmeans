#!/bin/env/python3.6
'''This python script implements our mapper for our K-means mapreduce task on EMNIST dataset.'''
'''
Usage: python Mapper.py labelCentroidsFilePath
using stdin to input the data points
'''

import sys
import numpy as np

labelCentroidsFile = open(sys.argv[1], 'r')
labelCentroidsDict = dict()
for line in labelCentroidsFile:
    label, Centroids = line.split('\t')
    label = eval(label)
    Centroids = np.fromiter(eval(Centroids), dtype='float')
    labelCentroidsDict[label] = Centroids
labelCentroidsFile.close()

numClusters = eval(sys.argv[2])

# Initialize the partial counting and partial sum of different labels
labelPartialCounting = { label:0 for label in labelCentroidsDict.keys()}
labelPartialSum = { label:np.zeros(784) for label in labelCentroidsDict.keys()}

for line in sys.stdin:
    imgIdx, imgData, imgLabel = line.split('\t')
    imgData = np.fromiter(eval(imgData), dtype='float')

    minDistanceToCentroids = 28*255
    minDistanceCentroidLabel = -1
    for label in labelCentroidsDict.keys():
        if(np.linalg.norm(labelCentroidsDict[label]-imgData) < minDistanceToCentroids):
            minDistanceCentroidLabel = label
            minDistanceToCentroids = np.linalg.norm(labelCentroidsDict[label]-imgData)

    labelPartialCounting[minDistanceCentroidLabel] += 1
    labelPartialSum[minDistanceCentroidLabel] += imgData
    
for label in labelCentroidsDict.keys():
    print(str(label)+'\t'+str(labelPartialCounting[label])+'\t'+str(labelPartialSum[label].tolist()))












