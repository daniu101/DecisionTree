#!/usr/bin/env python
# -*- coding: utf-8  

import operator   

#多数表决算法
def majorityCnt(classList):  
    classCount ={}  
    for vote in classList:  
        if vote not in classCount.keys():  
            classCount[vote]=0  
            classCount[vote]=1  
            sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)   
    return sortedClassCount[0][0]   

#创建样本数据集  
def createDataSet():  
    dataSet = [[1, 1, 'no'], [1, 1, 'no'], [1, 0, 'yes'], [0, 1, 'yes'], [0, 1, 'yes']]  
    return dataSet  

data = createDataSet()

classList = [example[-1] for example in data] 

mCnt = majorityCnt(classList)

print('classList:',classList)
print('majorityCnt:',mCnt)


