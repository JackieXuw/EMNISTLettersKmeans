#!bin/env/python
'''This python script generates the input (key, value) data to the mapReduce framework.'''
import sys
from mlxtend.data import loadlocal_mnist

# We first check the number of arguments from the command line
if len(sys.argv) != 4:
    print("Usage: python generateinputData.py image_path label_path output_path")
    exit()

imagesPath = sys.argv[1]
labelsPath = sys.argv[2]
outputPath = sys.argv[3]

images, labels = loadlocal_mnist(images_path=imagesPath, labels_path=labelsPath)
outputFile = open(outputPath,'w')

numImages = images.shape[0]

for imageIdx in range(numImages):
    line = str(imageIdx)+'\t'+str(images[imageIdx].tolist())+'\t'+str(labels[imageIdx])+'\n'
    outputFile.write(line)

outputFile.close()
