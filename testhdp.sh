#!/bin/bash

HADOOP_HOME=/usr/hdp/2.4.2.0-258
HADOOP_MAPREDUCE=${HADOOP_HOME}/hadoop-mapreduce
HADOOP_STREAMER=${HADOOP_MAPREDUCE}/hadoop-streaming-2.7.1.2.4.2.0-258.jar
HDFS_DATA_HOME=/user/liuyangtest/wenjie
DATA_NAME=$1   

# test the existence of data
#if [ $(hadoop dfs -test -f ${HDFS_DATA_HOME}/${DATA_NAME}) -ne 0 ];
#   then
#       echo "The data dose not exist in HDFS path ${HDFS_DATA_HOME}"
#       exit 1
#fi
 
# first remove existing output file
if $(hadoop dfs -test -d ${HDFS_DATA_HOME}/clustering/${DATA_NAME}-output);
 then hadoop dfs -rm -r ${HDFS_DATA_HOME}/clustering/${DATA_NAME}-output;
fi

hadoop jar ${HADOOP_STREAMER} \
-file Mapper.py -mapper 'python Mapper.py wenjie/clustering/labelCentroids.txt 41' \
-file Reducer.py -reducer 'python Reducer.py wenjie/clustering/labelCentroids.txt' \
-input ${HDFS_DATA_HOME}/clustering/${DATA_NAME}.txt -output ${HDFS_DATA_HOME}/clustering/${DATA_NAME}-output


 
