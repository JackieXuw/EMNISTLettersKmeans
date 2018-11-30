#!bin/env/python
# note that the label here is not the true letter label but just an index
import sys
import numpy as np

labelInputFile = sys.argv[1]
labelInputFile = open(labelInputFile, 'r')

labelsList = []
for line in labelInputFile:
    label, Centroids = line.split('\t')
    labelsList.append(label)

labelInputFile.close()

currentLabel = -1
currentCount = None
currentSum = None

for line in sys.stdin:
    label, labelPartialCounting, labelPartialSum = line.split('\t')
    label = eval(label)
    labelPartialCounting = eval(labelPartialCounting)
    labelPartialSum = np.fromiter(eval(labelPartialSum), dtype='float')
    if currentLabel != label:
        # we output the currentLabel's result first
        if currentLabel != -1:
            if currentCount == 0:
                currentCentroid = labelPartialSum.tolist() # we just choose the former data point as the newly updated
                                                             # centroid
                print(str(currentLabel)+'\t'+str(currentCentroid))
            else:
                currentCentroid = currentSum/currentCount
                print(str(currentLabel)+'\t'+str(currentCentroid.tolist()))
        # update the currentLabel, currentCount, currentSum
        currentLabel = label
        currentCount = labelPartialCounting
        currentSum = labelPartialSum
    else:
        currentCount+=labelPartialCounting
        currentSum+=labelPartialSum

    print('reduce', line)

if currentCount == 0:
    currentCentroid = 784*[0]  # we just choose the former data point as the newly updated
    # centroid
    print(str(currentLabel) + '\t' + str(currentCentroid))
else:
    currentCentroid = currentSum / currentCount
    print(str(currentLabel) + '\t' + str(currentCentroid.tolist()))




