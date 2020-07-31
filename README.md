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
