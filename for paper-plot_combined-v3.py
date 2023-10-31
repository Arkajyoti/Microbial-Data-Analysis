# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 19:31:02 2022

@author: arkajyoti.ghoshal
"""
import matplotlib.pyplot as plt
import random
import pandas as pd
import numpy as np
from scipy.stats import chisquare as cq
from scipy.optimize import curve_fit
import matplotlib.image as mpi
import scipy

data=pd.read_csv('P:/Hak Molecular/HA452_Molecular/Microscopy/PC/Contour/Analysed/2_12_22/TT/Master-TT.csv')
#print(data)
tyms=['0','20','60','120']

############# 0 ######################
d0TT=data[data['tym']==0]
#print(d20)
bvm0TT,bvs0TT=np.mean(d0TT['b/a']),np.std(d0TT['b/a'])
cvm0TT,cvs0TT=np.mean(d0TT['c/a']),np.std(d0TT['c/a'])

############# 20 ######################
d20TT=data[data['tym']==20]
#print(d20)
bvm20TT,bvs20TT=np.mean(d20TT['b/a']),np.std(d20TT['b/a'])
cvm20TT,cvs20TT=np.mean(d20TT['c/a']),np.std(d20TT['c/a'])

######### 60 ###############
d60TT=data[data['tym']==60]
#print(d60)
bvm60TT,bvs60TT=np.mean(d60TT['b/a']),np.std(d60TT['b/a'])
cvm60TT,cvs60TT=np.mean(d60TT['c/a']),np.std(d60TT['c/a'])

############### 120 ################
d120TT=data[data['tym']==120]
#print(d120)
bvm120TT,bvs120TT=np.mean(d120TT['b/a']),np.std(d120TT['b/a'])
cvm120TT,cvs120TT=np.mean(d120TT['c/a']),np.std(d120TT['c/a'])

'''
plt.xlim(0,.2)
#plt.ylim(0,.8)
plt.errorbar(cvm0TT,bvm0TT,yerr=bvs0TT,xerr=cvs0TT,capsize=10,fmt='o',color='r',label='0')
plt.errorbar(cvm20TT,bvm20TT,yerr=bvs20TT,xerr=cvs20TT,capsize=10,fmt='o',color='navy',label='20')
plt.errorbar(cvm60TT,bvm60TT,yerr=bvs60TT,xerr=cvs60TT,capsize=10,fmt='o',color='darkorange',label='60')
plt.errorbar(cvm120TT,bvm120TT,yerr=bvs120TT,xerr=cvs120TT,capsize=10,fmt='o',color='lime',label='120')
plt.legend()
plt.show()
print('Top c/a:',cvm0,cvm20,cvm60,cvm120)
print('Top b/a:',bvm0,bvm20,bvm60,bvm120)
#print('del c/a:', cvm20-cvm0,cvm60-cvm20,cvm120-cvm60)
#print('del b/a:', bvm20-bvm0,bvm60-bvm20,bvm120-bvm60)
print('Top c/a sd:',cvs0,cvs20,cvs60,cvs120)
print('Top b/a sd:',bvs0,bvs20,bvs60,bvs120)
'''
############################################################################################################

data=pd.read_csv('P:/Hak Molecular/HA452_Molecular/Microscopy/PC/Contour/Analysed/2_12_22/BT/Master-BT.csv')
#print(data)
tyms=['0','20','60','120']

############# 0 ######################
d0BT=data[data['tym']==0]
#print(d20)
bvm0BT,bvs0BT=np.mean(d0BT['b/a']),np.std(d0BT['b/a'])
cvm0BT,cvs0BT=np.mean(d0BT['c/a']),np.std(d0BT['c/a'])

############# 20 ######################
d20BT=data[data['tym']==20]
#print(d20)
bvm20BT,bvs20BT=np.mean(d20BT['b/a']),np.std(d20BT['b/a'])
cvm20BT,cvs20BT=np.mean(d20BT['c/a']),np.std(d20BT['c/a'])

######### 60 ###############
d60BT=data[data['tym']==60]
#print(d60)
bvm60BT,bvs60BT=np.mean(d60BT['b/a']),np.std(d60BT['b/a'])
cvm60BT,cvs60BT=np.mean(d60BT['c/a']),np.std(d60BT['c/a'])

############### 120 ################
d120BT=data[data['tym']==120]
#print(d120)
bvm120BT,bvs120BT=np.mean(d120BT['b/a']),np.std(d120BT['b/a'])
cvm120BT,cvs120BT=np.mean(d120BT['c/a']),np.std(d120BT['c/a'])

##########################################################################################################
data=pd.read_csv('P:/Hak Molecular/HA452_Molecular/Microscopy/PC/Contour/Analysed/2_12_22/BB/Master-BB.csv')
#print(data)
tyms=['0','20','60','120']

############# 0 ######################
d0BB=data[data['tym']==0]
#print(d20)
bvm0BB,bvs0BB=np.mean(d0BB['b/a']),np.std(d0BB['b/a'])
cvm0BB,cvs0BB=np.mean(d0BB['c/a']),np.std(d0BB['c/a'])
print('hh',cvm0BB)
############# 20 ######################
d20BB=data[data['tym']==20]
#print(d20)
bvm20BB,bvs20BB=np.mean(d20BB['b/a']),np.std(d20BB['b/a'])
cvm20BB,cvs20BB=np.mean(d20BB['c/a']),np.std(d20BB['c/a'])

######### 60 ###############
d60BB=data[data['tym']==60]
#print(d60)
bvm60BB,bvs60BB=np.mean(d60BB['b/a']),np.std(d60BB['b/a'])
cvm60BB,cvs60BB=np.mean(d60BB['c/a']),np.std(d60BB['c/a'])

############### 120 ################
d120BB=data[data['tym']==120]
#print(d120)
bvm120BB,bvs120BB=np.mean(d120BB['b/a']),np.std(d120BB['b/a'])
cvm120BB,cvs120BB=np.mean(d120BB['c/a']),np.std(d120BB['c/a'])

##########################################################################################################
data=pd.read_csv('P:/Hak Molecular/HA452_Molecular/Microscopy/PC/Contour/Analysed/2_12_22/TB/Master-TB.csv')
#print(data)
tyms=['0','20','60','120']

############# 0 ######################
d0TB=data[data['tym']==0]
#print(d20)
bvm0TB,bvs0TB=np.mean(d0TB['b/a']),np.std(d0TB['b/a'])
cvm0TB,cvs0TB=np.mean(d0TB['c/a']),np.std(d0TB['c/a'])

############# 20 ######################
d20TB=data[data['tym']==20]
#print(d20)
bvm20TB,bvs20TB=np.mean(d20TB['b/a']),np.std(d20TB['b/a'])
cvm20TB,cvs20TB=np.mean(d20TB['c/a']),np.std(d20TB['c/a'])

######### 60 ###############
d60TB=data[data['tym']==60]
#print(d60)
bvm60TB,bvs60TB=np.mean(d60TB['b/a']),np.std(d60TB['b/a'])
cvm60TB,cvs60TB=np.mean(d60TB['c/a']),np.std(d60TB['c/a'])

############### 120 ################
d120TB=data[data['tym']==120]
#print(d120)
bvm120TB,bvs120TB=np.mean(d120TB['b/a']),np.std(d120TB['b/a'])
cvm120TB,cvs120TB=np.mean(d120TB['c/a']),np.std(d120TB['c/a'])


################################   plot   ####################################

plt.rcParams["font.family"] = "Times new roman"
plt.rcParams["font.size"] = 14 # 10 is default'
y1,y2=0,.25
sy1,sy2=2,1.5
#------------------------  T T------------------------------------------------
tcol=['#ee5c42','#a0522d','#daa520','darkorange']
#tcol=['k','r','b','magenta']
#plt.xlim(0,.2)
plt.ylim(y1,y2)
plt.gcf().set_size_inches(sy1,sy2)
plt.bar(tyms[0],cvm0TT,yerr=cvs0TT,capsize=10,color=tcol[0],label='0')
plt.bar(tyms[1],cvm20TT,yerr=cvs20TT,capsize=10,color=tcol[1],label='0')
plt.bar(tyms[2],cvm60TT,yerr=cvs60TT,capsize=10,color=tcol[2],label='0')
plt.bar(tyms[3],cvm120TT,yerr=cvs120TT,capsize=10,color=tcol[3],label='0')
plt.yticks(np.arange(0,.5,.25))
#plt.legend()
plt.show()


#------------------------  B T------------------------------------------------
#tcol=['#B03060','#FF00FF','#BA55D3','#B94E48']
tcol=['#FFFACD','#F9DAB1','#FFE4E1','#E7D5C5']
plt.ylim(y1,y2)
plt.gcf().set_size_inches(sy1,sy2)
plt.bar(tyms[0],cvm0BT,yerr=cvs0BT,capsize=10,color=tcol[0],label='0')
plt.bar(tyms[1],cvm20BT,yerr=cvs20BT,capsize=10,color=tcol[1],label='0')
plt.bar(tyms[2],cvm60BT,yerr=cvs60BT,capsize=10,color=tcol[2],label='0')
plt.bar(tyms[3],cvm120BT,yerr=cvs120BT,capsize=10,color=tcol[3],label='0')
#plt.legend()
plt.yticks(np.arange(0,.5,.25))
plt.show()


#------------------------  B B------------------------------------------------
tcol=['purple','#f75394','cyan','slateblue']
plt.ylim(y1,y2)
plt.gcf().set_size_inches(sy1,sy2)
plt.bar(tyms[0],cvm0BB,yerr=cvs0BB,capsize=10,color=tcol[0],label='0')
plt.bar(tyms[1],cvm20BB,yerr=cvs20BB,capsize=10,color=tcol[1],label='0')
plt.bar(tyms[2],cvm60BB,yerr=cvs60BB,capsize=10,color=tcol[2],label='0')
plt.bar(tyms[3],cvm120BB,yerr=cvs120BB,capsize=10,color=tcol[3],label='0')
#plt.legend()
plt.yticks(np.arange(0,.5,.25))
plt.show()



#------------------------  T B------------------------------------------------
tcol=['#2F4F4F','#9B8080','#6B809D','#DCDCDC']
plt.ylim(y1,y2)
plt.gcf().set_size_inches(sy1,sy2)
plt.bar(tyms[0],cvm0TB,yerr=cvs0TB,capsize=10,color=tcol[0],label='0')
plt.bar(tyms[1],cvm20TB,yerr=cvs20TB,capsize=10,color=tcol[1],label='0')
plt.bar(tyms[2],cvm60TB,yerr=cvs60TB,capsize=10,color=tcol[2],label='0')
plt.bar(tyms[3],cvm120TB,yerr=cvs120TB,capsize=10,color=tcol[3],label='0')
#plt.legend()
plt.yticks(np.arange(0,.5,.25))
plt.show()
print('TT',cvm0TT,cvs0TT,cvm20TT,cvs20TT,cvm60TT,cvs60TT,cvm120TT,cvs120TT)
print('BT',cvm0BT,cvs0BT,cvm20BT,cvs20BT,cvm60BT,cvs60BT,cvm120BT,cvs120BT)
print('BB',cvm0BB,cvs0BB,cvm20BB,cvs20BB,cvm60BB,cvs60BB,cvm120BB,cvs120BB)
print('TB',cvm0TB,cvs0TB,cvm20TB,cvs20TB,cvm60TB,cvs60TB,cvm120TB,cvs120TB)
