#!env/bin/python
'''This python script implements the top module for the k-means clustering process.'''

import numpy as np
import sys
import os
import subprocess
from subprocess import call
#process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)



prevLabelCentroids = dict()
currLabelCentroids = dict()

hdfsInputDataFile = sys.argv[1]
hdfsOutputDataFile = sys.argv[2]
hdfsInputDict = dict()
hdfsOutputDict = dict()



StopCriterionThreshold = 1e-3
MaxIter = 100

def execute(cmd):
    popen = subprocess.Popen(cmd, stdout=subprocess.PIPE, universal_newlines=True)
    for stdout_line in iter(popen.stdout.readline, ""):
        yield stdout_line 
    popen.stdout.close()
    return_code = popen.wait()
    if return_code:
        raise subprocess.CalledProcessError(return_code, cmd)


for iterIdx in range(MaxIter):
    #process = subprocess.Popen('bash testhdp.sh trainData'.split(' '), shell=True, stdout=subprocess.PIPE)  
    #process.wait()
    
    execute('bash testhdp.sh trainData'.split(' '))


    #print(hdfsInputDataFile)

    process = subprocess.Popen(('hadoop fs -cat '+hdfsInputDataFile+' temp.txt').split(' '), shell=True, stdout=subprocess.PIPE)
    process.wait()
 
    hdfsInputData = open('temp.txt','r')
    for line in hdfsInputData:
        label, centroid = line.split('\t')
        hdfsInputDict[label] = np.fromiter(eval(centroid), dtype='float')

    process = subprocess.Popen(('hadoop fs -cat '+hdfsOutputDataFile+' temp.txt').split(' '), shell=True, stdout=subprocess.PIPE)
    process.wait()


    hdfsOutputData = open('temp.txt','r')
    for line in hdfsOutputData:
        label, centroid = line.split('\t')
        hdfsOutputDict[label] = np.fromiter(eval(centroid), dtype='float')
    
    TempSum = 0
    for label in hdfsInputDict.keys():
        TempSum+= ((hdfsInputDict[label]-hdfsOutputDict[label])**2).sum()
    
    process = subprocess.Popen(('hadoop fs -cp '+hdfsOutputDataFile+' '+hdfsInputDataFile).split(' '), shell=True, stdout=subprocess.PIPE)
    process.wait()
    if TempSum < StopCriterionThreshold:
        break







