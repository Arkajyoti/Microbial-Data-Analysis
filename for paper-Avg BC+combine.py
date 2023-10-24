# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 16:52:50 2022

@author: arkajyoti.ghoshal
"""

import os
#import trackpy as tp
import numpy as np
import cv2
import matplotlib as mp
import matplotlib.pyplot as plt

from matplotlib.patches import Circle
from skimage import measure
from skimage.segmentation import clear_border
import pandas as pd
import matplotlib.cm as cm
import time

seconds = time.time()
local_time = time.ctime(seconds)
print("Experiment Begins,Local time:", local_time)


plt.rcParams['font.family'] = ['Times New Roman']

def norm(x):
    y=[]
    
    z=np.sum(x)
    for k in range(len(x)):
        s=(x[k]/z)
        y.append(s)
    print(z)
    #sums.append(z)
    return(y)
    
####### plots ##########
#############################BR1_28-10-22##############################
tA0d=list(pd.read_csv('P:/HA452_Motility/Tall Chamber/Analysed/28_10_22/BC/0/Overall.csv')['yvalc'])

tA20d=list(pd.read_csv('P:/HA452_Motility/Tall Chamber/Analysed/28_10_22/BC/20/Overall.csv')['yvald'][:14])
tA20d.reverse()

tA60d=list(pd.read_csv('P:/HA452_Motility/Tall Chamber/Analysed/28_10_22/BC/60/Overall.csv')['yvalc'][:14])


tA120d=list(pd.read_csv('P:/HA452_Motility/Tall Chamber/Analysed/28_10_22/BC/120/Overall.csv')['yval'])
tA120d.reverse()

#################### norm ######################
tA0d,tA20d,tA60d,tA120d=norm(tA0d),norm(tA20d),norm(tA60d),norm(tA120d)


print('BR1',len(tA0d),len(tA20d),len(tA60d),len(tA120d))





#############################BR2_28-10-22/2##############################
tB0d=list(pd.read_csv('P:/HA452_Motility/Tall Chamber/Analysed/28_10_22/BC-T2/0/Overall.csv')['yvalc'][:14])

tB20d=list(pd.read_csv('P:/HA452_Motility/Tall Chamber/Analysed/28_10_22/BC-T2/20/Overall.csv')['yvald'][:14])
tB20d.reverse()
#print(t20d)
tB60d=list(pd.read_csv('P:/HA452_Motility/Tall Chamber/Analysed/28_10_22/BC-T2/60/Overall.csv')['yval'][:])


tB120d=list(pd.read_csv('P:/HA452_Motility/Tall Chamber/Analysed/28_10_22/BC-T2/120/Overall.csv')['yvald'][:14])
tB120d.reverse()
#print(tB120d)
print('BR2',len(tB0d),len(tB20d),len(tB60d),len(tB120d))

tB0d,tB20d,tB60d,tB120d=norm(tB0d),norm(tB20d),norm(tB60d),norm(tB120d)
#############################BR3_1-11-22/2##############################
tC0d=list(pd.read_csv('P:/HA452_Motility/Tall Chamber/Analysed/1_11_22/BC/0/Overall.csv')['yvald'][:14])
#print(tC0d)
tC20d=list(pd.read_csv('P:/HA452_Motility/Tall Chamber/Analysed/1_11_22/BC/20/Overall.csv')['yvald'][:14])
tC20d.reverse()

tC60d=list(pd.read_csv('P:/HA452_Motility/Tall Chamber/Analysed/1_11_22/BC/60/Overall.csv')['yvald'][:14])


tC120d=list(pd.read_csv('P:/HA452_Motility/Tall Chamber/Analysed/1_11_22/BC/120/Overall.csv')['yval'])
tC120d.reverse()

print('BR3',len(tC0d),len(tC20d),len(tC60d),len(tC120d))
tC0d,tC20d,tC60d,tC120d=norm(tC0d),norm(tC20d),norm(tC60d),norm(tC120d)

#############################BR3_7-11-22/2##############################
tD0d=list(pd.read_csv('P:/HA452_Motility/Tall Chamber/Analysed/7_11_22/BC/0/Overall.csv')['yval'])
tD0d.reverse()

tD20d=list(pd.read_csv('P:/HA452_Motility/Tall Chamber/Analysed/7_11_22/BC/20/Overall.csv')['yval'][:])
tD20d.reverse()

tD60d=list(pd.read_csv('P:/HA452_Motility/Tall Chamber/Analysed/7_11_22/BC/60/Overall.csv')['yvald'][:])
tD60d.reverse()

tD120d=list(pd.read_csv('P:/HA452_Motility/Tall Chamber/Analysed/7_11_22/BC/120/Overall.csv')['yval'])

print('BR4',len(tD0d),len(tD20d),len(tD60d),len(tD120d))
tD0d,tD20d,tD60d,tD120d=norm(tD0d),norm(tD20d),norm(tD60d),norm(tD120d)

pm20d,ps20d=np.array([0.08613652, 0.0808672,  0.07502785, 0.08043472, 0.07262774 ,0.07357758,
 0.07278724, 0.07276122, 0.06868365, 0.0663435 , 0.06666063, 0.0671723,
 0.06383451 ,0.05308535]),np.array([0.00642476, 0.00182209, 0.0041125 , 0.00067382 ,0.00396325, 0.00126242,
 0.00377356, 0.0011127 , 0.00081279, 0.00089246, 0.00181339, 0.00123823,
 0.00203642, 0.00840476])

av0d,sd0d=np.mean([tA0d,tB0d,tC0d,tD0d],axis=0),np.std([tA0d,tB0d,tC0d,tD0d],axis=0)
av20d,sd20d=np.mean([tA20d,tB20d,tC20d,tD20d],axis=0),np.std([tA20d,tB20d,tC20d,tD20d],axis=0)
av60d,sd60d=np.mean([tA60d,tB60d,tC60d,tD60d],axis=0),np.std([tA60d,tB60d,tC60d,tD60d],axis=0)
av120d,sd120d=np.mean([tA120d,tB120d,tC120d,tD120d],axis=0),np.std([tA120d,tB120d,tC60d,tD120d],axis=0)

#print(av0d)
tymcol=['purple','#f75394','darkorange','lime']


xaxx=list(np.arange(0,14,1))

plt.plot(tA0d,'.')
plt.plot(tC0d,'.')
plt.plot(tB0d,'.')
plt.plot(tD0d,'.')

plt.plot(tC20d,'o-')
plt.plot(tB20d,'o-')
plt.plot(tA20d,'o-')
plt.plot(tD20d,'o')

#plt.gcf().set_size_inches(8,4)
plt.gca().yaxis.tick_right()
plt.legend()
plt.tight_layout()
plt.show()
##########################################################################################
###########################  for paper v2 ############################################
plt.plot(xaxx,pm20d,'b',label='pre-flip')
plt.fill_between(xaxx, pm20d-ps20d, pm20d+ps20d,facecolor=tymcol[0],alpha=.35)


plt.plot(xaxx,av0d,'purple',label='0')
plt.fill_between(xaxx, av0d-sd0d, av0d+sd0d,facecolor=tymcol[0],alpha=.35)

plt.plot(xaxx,av20d,tymcol[1],label='20')
plt.fill_between(xaxx, av20d-sd20d, av20d+sd20d,facecolor=tymcol[1],alpha=.35)

plt.ylim(0.025,0.16)
plt.gca().yaxis.tick_right()
plt.legend(loc='upper center',fontsize=15)
plt.tight_layout()
plt.show()

##########################################################################
#                 'Upward bias'
def ubs(lsf,rg):
    bl=[]
    for ii in range(len(lsf)):
        var=lsf[ii]
        #print(var)
        n1v,n2v=np.sum(var[:rg]),np.sum(var[-rg:])
        #print('lenght n1-n2',len(n1v),len(n2v))
        bvl=(n1v-n2v)/(n1v+n2v)
        bl.append(bvl)
    nbl=np.array(bl)
    
    avb,sb=np.mean(nbl),np.std(nbl)
    #print('*'*80,avb)
    return(nbl,avb,sb)
    
ub0,avb0,sb0=ubs([tA0d,tB0d,tC0d],3)
print(avb0,sb0)
ub20,avb20,sb20=ubs([tA20d,tB20d,tC20d],3)
print(avb20,sb20)

pm20T,ps20T=0.15653831686501174, 0.007668939320498072
pm20B,ps20B=0.12566272718218902, 0.0317749570847635
avb0T,sb0T=-0.26563190342305315, 0.16912410300962408
avb20T,sb20T= 0.16924827023396638, 0.09229606894257643
avb0B,sb0B=-0.3039709937207174, 0.17615014419865613
avb20B,sb20B=0.18040726032509444, 0.14804692580829099

plt.bar(0,pm20T,2,yerr=ps20T,color='r',capsize=10)
plt.bar(2,avb0T,2,yerr=sb0T,color='#ee5c42',capsize=10)
plt.bar(4,avb20T,2,yerr=sb20T,color='#a0522d',capsize=10)
plt.ylim(-.5,.4)
plt.xticks([0,2,4],['as','s','kk'])
plt.yticks(np.arange(-.5,1,.5))
plt.gcf().set_size_inches(3,4)
plt.show()

plt.bar(0,pm20B,2,yerr=ps20B,color='b',capsize=10)
plt.bar(2,avb0B,2,yerr=sb0B,color=tymcol[0],capsize=10)
plt.bar(4,avb20B,2,yerr=sb20B,color=tymcol[1],capsize=10)
plt.ylim(-.5,.4)
plt.yticks(np.arange(-.5,1,.5))
plt.gcf().set_size_inches(3,4)
plt.xticks([0,2,4],['as','s','kk'])

print('Top cell count',np.mean([24469,14454,16590]),np.std([24469,14454,16590]))
print('Bot cell count',np.mean([18831,23527,28793,13784]),np.std([18831,23527,28793,13784]))

print('Bot cell count mod 0 min',np.mean([28831,33527,38793,23784]),np.std([28831,33527,38793,23784]))

print('Bot cell count mod 20 min',np.mean([30331,34527,38293,22784]),np.std([30331,34527,38293,22784]))

