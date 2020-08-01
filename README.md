# network-related-prerelease
this is the prerelease version of our group project
it now contains two parts: one is for evaluating the link prediction performance of deepwalk on eight data sets which are used in SEAL("Link Prediction Based on Graph Neural Networks");
the other is for evaluating the link prediction performance of several algorithms on HUAWEI's data. For reasons of confidentiality, the data set will not be shared, but the code is available after obtaining consent；
There will be another part, which is for evaluating the dynamic link prediction performance of several algorithms on some benchmark data sets. The code is still under organization.

the implement of deepwalk code is copied from https://github.com/phanein/deepwalk
you can follow the instruction in /deepwalk folder to valid it
then you can run 

$ python train_test_split_pre.py

to get the training and testing set of each data set(using negative sampling) then run

$ python trainning_data_pre.py

to construct the observed graph for each data set, next with

$bash get_embeddings.sh 

to get the embedding for each node within the observed graphs mentioned before. finally, use

$ python link_prediction_pre.py 

to get the link prediction performance of deepwalk on eight data sets.
In our report, we run it for 10 time to get the estimated mean value and std. of AUC.


To run baseline algorithms on HUAWEI's data, 
for SEAL, you can refer to 

https://github.com/muhanzhang/SEAL/tree/master/Python

just add the data(of .mat form) into the data folder of SEAL and use

$python Main.py --data-name Subgraph_Data

to get the AUC

As for embedding-baesd algorithm, take deepwalk as an example, you need to process the data.mat follow the steps mentioned before(train_test_split -> use training data to learning the embeddings of each node -> link prediction evaluation)

For the implementation of LINE and Node2vec, you can refer to:
https://github.com/shenweichen/GraphEmbedding

For the implementation of VGAE, you can refer to:
https://github.com/zfjsail/gae-pytorch
