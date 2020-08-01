#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 17:26:36 2020

@author: siyi
"""

import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score

def reconstruct(dataset):
    lst = ['train_pos.txt', 'train_neg.txt', 'test_pos.txt','test_neg.txt']
    output = []
    for i in range(len(lst)):
        name = dataset+lst[i]
        data = open(name)
        data1 = data.readlines()[0]
        data2 = data1.split('), (')
        data2[0], data2[-1] = data2[0][2:], data2[-1][:-3]
        for i in range(len(data2)):
            data2[i] = data2[i].split(', ')
            data2[i][0], data2[i][1] = int(data2[i][0]), int(data2[i][1])
        output.append(data2)
    return output


def get_embedding(dataset):
    data = open(dataset+'.embeddings')
    embeddings = data.readlines()
    for i in range(1, len(embeddings)):
        embeddings[i] = embeddings[i][:-1].split(' ')
        for j in range(len(embeddings[i])):
            embeddings[i][j] = float(embeddings[i][j])
        
    dic = {int(embeddings[i][0]):embeddings[i][1:] for i in range(1, len(embeddings))}  
    return dic
    
    
def get_train_test(dataset):
    lst, dic = reconstruct(dataset), get_embedding(dataset)
    train_pos, train_neg, test_pos,test_neg = lst
    num = len(dic[train_pos[0][0]])
    train, test = [], []
    for i in range(len(train_pos)):
        if train_pos[i][0] in dic.keys() and train_pos[i][1] in dic.keys():
            row1 = dic[train_pos[i][0]]+dic[train_pos[i][1]]+[1]
        elif train_pos[i][0] in dic.keys() and train_pos[i][1] not in dic.keys():
            row1 = dic[train_pos[i][0]]+[0 for i in range(num)]+[1]
        elif train_pos[i][0] not in dic.keys() and train_pos[i][1] in dic.keys():
            row1 = [0 for i in range(num)]+dic[train_pos[i][1]]+[1]
        else:
            row1 = [0 for i in range(num*2)]+[1]
        
        if train_neg[i][0] in dic.keys() and train_neg[i][1] in dic.keys():
            row2 = dic[train_neg[i][0]]+dic[train_neg[i][1]]+[0]
        elif train_neg[i][0] in dic.keys() and train_neg[i][1] not in dic.keys():
            row2 = dic[train_neg[i][0]]+[0 for i in range(num)]+[0]
        elif train_neg[i][0] not in dic.keys() and train_neg[i][1] in dic.keys():
            row2 = [0 for i in range(num)]+dic[train_neg[i][1]]+[0]
        else:
            row2 = [0 for i in range(num*2)]+[0]
            
        train.append(row1)
        train.append(row2)
        
    for i in range(len(test_pos)):
        if test_pos[i][0] in dic.keys() and test_pos[i][1] in dic.keys():
            row1 = dic[test_pos[i][0]]+dic[test_pos[i][1]]+[1]
        elif test_pos[i][0] in dic.keys() and test_pos[i][1] not in dic.keys():
            row1 = dic[test_pos[i][0]]+[0 for i in range(num)]+[1]
        elif test_pos[i][0] not in dic.keys() and test_pos[i][1] in dic.keys():
            row1 = [0 for i in range(num)]+dic[test_pos[i][1]]+[1]
        else:
            row1 = [0 for i in range(num*2)]+[1]
            
        if test_neg[i][0] in dic.keys() and test_neg[i][1] in dic.keys():
            row2 = dic[test_neg[i][0]]+dic[test_neg[i][1]]+[0]
        elif test_neg[i][0] in dic.keys() and test_neg[i][1] not in dic.keys():
            row2 = dic[test_neg[i][0]]+[0 for i in range(num)]+[0]
        elif test_neg[i][0] not in dic.keys() and test_neg[i][1] in dic.keys():
            row2 = [0 for i in range(num)]+dic[test_neg[i][1]]+[0]
        else:
            row2 = [0 for i in range(num*2)]+[0]          
            
        test.append(row1)
        test.append(row2)
    return pd.DataFrame(train), pd.DataFrame(test)
    
def link_prediction(dataset):
    train, test = get_train_test(dataset)
    x, y = train.drop(train.columns[-1], axis=1), train.iloc[:,-1]
    clf = LogisticRegression()
    clf.fit(x, y)
#    clf = LogisticRegression(random_state=0).fit(x, y)
    test_x, test_y = test.drop(train.columns[-1], axis=1), test.iloc[:,-1]
    pred = clf.predict_proba(test_x)[:,1]
    return roc_auc_score(test_y, pred)

data_lst = ['Subgraph Data']
if __name__=='__main__':
    with open('result.txt','a') as file:
        for i in range(len(data_lst)):
            score = link_prediction(data_lst[i])
            file.write(data_lst[i])
            file.write('    ')
            file.write(str(score))
            file.write('\n')
        
        
        
        

        














