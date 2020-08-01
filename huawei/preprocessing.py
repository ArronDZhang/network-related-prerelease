#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 05:55:50 2020

@author: siyi
"""

import pandas as pd
import networkx as nx
import scipy.io as scio

data = pd.read_table('Subgraph Data.txt')

nodes = list(set(list(data['Node_ID'])))
node = list(data['Node_ID'])
paths = list(data['Flow_Order'])

dic = {}
for i in range(len(nodes)):
    dic.update({nodes[i]:i})

nodeB_index = []
for i in range(len(paths)):
    if paths[i] == 0:
        nodeB_index.append(i)
    node[i] = dic[node[i]]
    
path_lst = []
for i in range(len(nodeB_index)-1):
    path = [node[j] for j in range(nodeB_index[i], nodeB_index[i+1])]
    path_lst.append(path)

def path2edges(lst):
    num = len(lst)
    edges = []
    for i in range(num-1):
        tp = (lst[i], lst[i+1])
        edges.append(tp)
    return edges

edges = []
for i in range(len(path_lst)):
    edges += path2edges(path_lst[i])
    
super_node = len(nodes)
for i in range(1, len(nodeB_index)):
    edges += [(super_node, nodeB_index[i]-1)]
    
G = nx.Graph(edges)
adj_mat = nx.adj_matrix(G)
filename = 'Subgraph_Data.mat'
scio.savemat(filename, {'network':adj_mat})

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    