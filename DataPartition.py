#!/usr/bin/env python
# -*- coding: utf-8 

#根据dataSet元素的第axis个特征是否等于value进行划分
def splitDataSet(dataSet, axis, value):  

    retDataSet = []    
    for featVec in dataSet:  
        if featVec[axis] == value:  
            reducedFeatVec = featVec[:axis]  
            reducedFeatVec.extend(featVec[axis+1:])  
            retDataSet.append(reducedFeatVec)  
    return retDataSet  

#创建样本数据集  
def createDataSet():  
    dataSet = [[1, 1, 'yes'], [1, 1, 'yes'], [1, 0, 'no'], [0, 1, 'no'], [0, 1, 'no']]  
    return dataSet  

data = createDataSet()

split01 = splitDataSet(data,0,1)
split00 = splitDataSet(data,0,0)
split02 = splitDataSet(data,0,2)

print('split01:',split01)
print('split00:',split00)
print('split02:',split02)


