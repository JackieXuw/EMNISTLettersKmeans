#!bin/env/python
import numpy as np
import sys

K = 41
labelCentroidsFile = open(sys.argv[1], 'w')
for k in range(K):
    Centroid = np.random.randint(256, size=784)
    line = str(k)+'\t'+str(Centroid.tolist())+'\n'
    labelCentroidsFile.write(line)

labelCentroidsFile.close()



