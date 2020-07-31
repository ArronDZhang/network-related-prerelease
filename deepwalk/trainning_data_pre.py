#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 16:02:41 2020

@author: siyi
"""

import networkx as nx
import scipy.io as scio
from train_test_split_pre import get_train_test

data_lst = ['USAir.mat', 'PB.mat', 'NS.mat', 'Yeast.mat', 'Celegans.mat', \
            'Power.mat', 'Router.mat', 'Ecoli.mat']

def construct_train_graph(dataset):
    train_pos, train_neg, test_pos, test_neg = get_train_test(dataset)
    graph, train_neg_txt, test_pos_txt, test_neg_txt = [],[],[],[]
    for i in range(len(train_pos[0])):
        graph.append((train_pos[0][i],train_pos[1][i]))
        train_neg_txt.append((train_neg[0][i],train_neg[1][i]))
        
    with open(dataset[:-4]+'train_pos.txt','a') as file:
        file.write("{}\n".format(graph))
    file.close()
    with open(dataset[:-4]+'train_neg.txt','a') as file:
        file.write("{}\n".format(train_neg_txt))
    file.close()
    
    for i in range(len(test_pos[0])):
        test_pos_txt.append((test_pos[0][i],test_pos[1][i]))
        test_neg_txt.append((test_neg[0][i],test_neg[1][i]))
    
    with open(dataset[:-4]+'test_pos.txt','a') as file:
        file.write("{}\n".format(test_pos_txt))
    file.close()
    with open(dataset[:-4]+'test_neg.txt','a') as file:
        file.write("{}\n".format(test_neg_txt))
    file.close()
    
    G = nx.Graph(graph)
    adj_mat = nx.adj_matrix(G)
    filename = 'new_'+dataset
    scio.savemat(filename, {'network':adj_mat})
    return

if __name__=='__main__':
    for i in range(len(data_lst)):
        construct_train_graph(data_lst[i])
