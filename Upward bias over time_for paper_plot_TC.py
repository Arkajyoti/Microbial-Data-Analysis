# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 16:52:50 2022

@author: arkajyoti.ghoshal
"""

import os
import statistics as ss
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

frms=[0,10,20,30,40]


def ubs(lt):
    #ubv=[]
    #for zy in range(len(lt)):
        n1=np.sum(lt[:4])
        n2=np.sum(lt[-4:])
        B=(n1-n2)/(n1+n2)
        #ubv.append(B)
    #return(ubv)
        
        #print('ubv',B)
        return(B)
    
    
def matt(t,pt):
    
    cmb,ubz=[],[]
    for ny in range(len(t)):
        yc2=pd.read_csv(pt+str(t[ny])+'/'+'count.csv')
        #print(yc2)
        cnv=[]
        for kc in range(len(frms)):
            dff=yc2[(yc2.frm==frms[kc])]
            #print(dff)
            yc1=dff['yval']
            #print(yc1[:4])
            cn,bn=np.histogram(yc1,bins=20)
            cn=cn/sum(cn)
            cnv.append(list(cn))
            
        #print(cnv)
        mpp=np.mean(cnv,axis=0)
        cmb.append(list(mpp))
        bv=ubs(mpp)
        #print('hhh',mpp)
        ubz.append(bv)
    return(cmb,ubz)
    #return(ubz)
        
        
        

tym=[0,20,60,120]
############### BR1 ########################
p1='P:/HA452_Motility/Physical Sig/Analysed/20_8_22/Analysed-v2/TC/'
avd,avb=matt(tym,p1)
#print(avd,avb)

############### BR2 ########################
p2='P:/HA452_Motility/Physical Sig/Analysed/29_8_22/Analysed-v2/TC/'
avd2,avb2=matt(tym,p2)
#print(avd2,avb2)

############### plots################
tymcol=['r','navy','darkorange','lime']
mbs,sbs=np.mean([avb,avb2],axis=0),np.std([avb,avb2],axis=0)
#print(mbs)
plt.bar(['0','20','60','120'],mbs,yerr=sbs,capsize=5,color='r')
plt.ylim(-0.25,0.55)
plt.show()
for dk2 in range(len(tym)):
    plt.gcf().set_size_inches(5,3)
    plt.bar(str(tym[dk2]),mbs[dk2],yerr=sbs[dk2],label=str(tym[dk2]),color=tymcol[dk2],capsize=5)
    plt.ylim(-0.25,0.5)
plt.show()

xaxs=list(np.arange(0,2000,100))
mds,sds=np.mean([avd,avd2],axis=0),np.std([avd,avd2],axis=0)
for dk in range(len(tym)):
    plt.errorbar(xaxs,mds[dk],label=str(tym[dk]),color=tymcol[dk])
    plt.fill_between(xaxs, mds[dk]-sds[dk], mds[dk]+sds[dk],facecolor=tymcol[dk],
    alpha=.35)#,linewidth=20,edgecolor='k')#tymcol[dk],facecolor=tymcol[dk])
    #linewidth=4, linestyle='dashdot')
    plt.gca().yaxis.tick_right()
    plt.ylim(0.015,0.15)
    plt.xlim(-20,1930)
