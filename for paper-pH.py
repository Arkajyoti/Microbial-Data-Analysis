# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 16:38:46 2022

@author: arkajyoti.ghoshal
"""

import os
#import trackpy as tp
import numpy as np
import cv2
import matplotlib as mp
import matplotlib.pyplot as plt
import math
from matplotlib.patches import Circle
from skimage import measure
from skimage.segmentation import clear_border
import pandas as pd
import matplotlib.cm as cm
import scipy.stats as stats

pMd=[8.32,8.3,8.35,8.38] #(data: 14-10,16-9)
pT=[9.05,9.01,8.97,9.02,9.02] #(data: 14-10,16-9,29-8,NK data: 8-2-23)
pB=[9.06,9.08,9.02,9.12,9.19]

#pT=[9.2	,9.14,	9.09	,9.02] #(data: 12.8,16.8,29.8)
#pB= [9.17,	9.08,	9.06,	8.97]#(data: 12.8,16.8,29.8)
mpM,spm=np.mean(pMd),np.std(pMd)
mT,sT=np.mean(pT),np.std(pT)
mB,sB=np.mean(pB),np.std(pB)

plt.rcParams['font.family'] = 'Times new roman'
plt.bar(0,mpM,2,yerr=spm,capsize=10,color='gold')
plt.bar(5-1,mT,2,yerr=sT,capsize=10,color='r',label='Top')
plt.bar(5+1,mB,2,yerr=sB,capsize=10,color='b',label='Bottom')
#plt.bar(5+1,mB,2,yerr=sB,capsize=10,color='g',label='Mixed')
plt.xticks([0,4,6],[0,4,6])
plt.ylim(7.5,9.5)
plt.yticks(np.arange(7.5,10,.5))
plt.legend(loc=(1.01,1.01),fontsize=14)
plt.show()

''''final rules: alpha: .1, due to low sample no., equlvariance if var ratio < 2 (rounded)'''
def t_tst_f(x1,x2,bo):
    ' note: p value doesnt change on the order of x1 and x2'
    varl=[np.var(x1), np.var(x2),(np.var(x1)/np.var(x2))]
    tv,pv=stats.ttest_ind(x1, x2, equal_var = bo)
    #print('both variances+ratio',varl,varl[0]/varl[1])
    return(varl,tv,pv)
    
#t1,t2=t_tst_f(g1,g2,True)
#print(t1,t2)
vlfv,tvfv,pvfv=t_tst_f(pMd,pT,False)
print('med v cell:',vlfv,tvfv,pvfv)

vlfv2,tvfv2,pvfv2=t_tst_f(pB,pT,False)
print('T v B:',vlfv2,tvfv2,pvfv2)

'''If the P-value is smaller than the significance level (.05/.1), the means are stat different (we reject the null hypothesis which is same means) '''
print('mean pM',mpM,spm)
print('mean pT',mT,sT)
print('mean pB',mB,sB)

print(np.std([8.34,8.31])) ### 0hrs T
print(np.std([8.3,8.32])) ##0hrs bot

###0h ####
T0=[8.33,8.34]
B0=[8.35,8.36]

print('0H Top',np.mean(T0),np.std(T0))
print('0H Bot',np.mean(B0),np.std(B0))
### 48h ###
T48=[8.69,8.74] #### data: 10-10-22
print('48H Top',np.mean(T48),np.std(T48))

B48=[8.78,8.86] #### data: 10-10-22
print('48H Bot',np.mean(B48),np.std(B48))

### 144h ###
T44=[9.05,9.12] #### data: 11-1-23, 20-1-23
print('44H Top',np.mean(T44),np.std(T44))

B44=[9.13,9.22] #### data: 11-1-23,20-1-23
print('44H Bot',np.mean(B44),np.std(B44))

############# 240h/10d ################
T10=[9.09,9.09]
print('240H Top',np.mean(T10),np.std(T10))

B10=[9.11,9.13]
print('240H Bot',np.mean(B10),np.std(B10))

#### 18 d ###
T18=[9.05,9.07]  ### 10-1-23
B18=[9.1,9.13]
print('432H Top',np.mean(T18),np.std(T18))
print('432H Bot',np.mean(B18),np.std(B18))



##### 30d ###
T30=[8.23,8.28]  #### 12-1-23, 12-8-22
B30=[8.31,8.22]

print('30D Top',np.mean(T30),np.std(T30))
print('30D Bot',np.mean(B30),np.std(B30))


############ plot over time (ot) ###################

mTot,sTot=[np.mean(T0),np.mean(T48),mT,np.mean(T44),np.mean(T10),np.mean(T18),np.mean(T30)],[np.std(T0),np.std(T48),sT,np.std(T44),np.std(T10),np.std(T18),np.std(T30)]
mBot,sBot=[np.mean(B0),np.mean(B48),mB,np.mean(B44),np.mean(B10),np.mean(B18),np.mean(B30)],[np.std(B0),np.std(B48),sB,np.std(B44),np.std(B10),np.std(B18),np.std(B30)]

tva=[0,48,96,144,240,432,720]
#tcol=['r','r','r','r','r','r','r']
#plt.bar(-2,mpM,2,yerr=spm,capsize=10,color='gold')

'''
plt.bar(3-1,mTot[0],2,yerr=sTot[0],capsize=10,color=tcol[0],label='Top')
plt.bar(5+1,mB,2,yerr=sB,capsize=10,color='b',label='Bottom')

'''
xtyk=[]
nv=4
for yy in range(len(tva)):
    plt.bar(nv-1,mTot[yy],2,yerr=sTot[yy],capsize=5,color='r',label='Top')
    plt.bar(nv+1,mBot[yy],2,yerr=sBot[yy],capsize=5,color='b',label='Bottom')
    #plt.plot([0,27],[mpM,mpM],'--',color='gold')
    nv=nv+5
    xtyk.append(nv)
    #print(nv)

print(xtyk)
#xtyks=[-2,4]+xtyk
#print(xtyks)
xtyk=[4]+xtyk
xtyk=xtyk[:-1]
plt.xticks(xtyk,tva)
plt.ylim(8,9.5)
plt.yticks(np.arange(8,10,.5))
#plt.legend(loc=(1,1),fontsize=14)
#plt.plot([xtyks[1],xtyks[-2]],[mpM,mpM],'--',color='gold')
plt.show()

################### bot-top (delta ph=dp, ot=over time) ##############
dpot=np.array(mBot)-np.array(mTot)
sdot=np.sqrt((np.array(sBot))**2+(np.array(sTot))**2) #####  std dev during substraction  #####

print(dpot)
sdot2=np.array(sBot)-np.array(sTot)
#print(sdot2)
plt.errorbar(xtyk,dpot,fmt='o-',color='purple')
lim1,lim2=(dpot-sdot2),(dpot+sdot2)
#lim1[-2]=dpot[-2]+.01
#lim2[-2]=
plt.fill_between(xtyk, lim1,lim2,facecolor='purple',
    alpha=.35)
plt.yticks(np.arange(0,.15,.05))
plt.xticks(xtyk,tva)
plt.gcf().set_size_inches(6,6.5)
print('lim1',lim1[-2])
print('lim2',lim2[2])