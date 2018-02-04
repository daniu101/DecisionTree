#!/usr/bin/env python
# -*- coding: utf-8 

from math import log  

#计算给定数据集的香农熵 
def calcShannonEnt(dataSet):  
    numEntries = len(dataSet)  
    
    #为所有的分类创建字典
    labelCounts = {}  
    for featVec in dataSet:  
        currentLabel = featVec[-1]  
        if currentLabel not in labelCounts.keys():  
            labelCounts[currentLabel] = 0  
        labelCounts[currentLabel] += 1  
        
    #计算香农熵 
    shannonEnt = 0.0  
    for key in labelCounts:  
        prob = float(labelCounts[key]) / numEntries  
        shannonEnt -= prob * log(prob, 2)  
    return shannonEnt

#创建样本数据集  
def createDataSet():  
    dataSet = [[1, 1, 'yes'], [1, 1, 'yes'], [1, 0, 'no'], [0, 1, 'no'], [0, 1, 'no']]  
    return dataSet  

data = createDataSet()
entD = calcShannonEnt(data)

print('data:',data)
print('Ent(D):',entD)


