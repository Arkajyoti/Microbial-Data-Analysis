# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 12:16:59 2021

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

#BR2=[902,1142,1542,2015,2554,2853,1912,1645,1610]
#BR1T=[2507,2646,2757,2984,3447,3782,3994,2913,2256]
#BR2T=[770,961,1062,1268,1373,1259,1259,786,717]
BR1T=[2718,4037,3232,3022,3255,3385,3426,2538,1974]
BR2T=[1302,1694,774,471,616,728,826,1006,1077]
#ya=[2700,3800,3000,1600,1100]
#xb,yb=[1700,2100,1840,2000,0],[3100,3800,3780,3700,3200]
#tm=[0,4,8,15,20]


#tm=[0,5,10,15,20]
tm2=[0,5,10,15,20,25,30,45,60]
#dmix=list(np.array(mnz[1:])-np.array(mnz[:-1]))
#dtm1=[1,2,3,4]
dtm2=[1,2,3,4,5,6,7,8]
#plt.plot(dtm2,dmix,'k',marker='o',label='Mixed_Av')
#plt.legend()
'''
def av_p(a,b):
    av,s=[],[]
    for k in range(len(a)):
        t=np.mean([a[k],b[k]])
        av.append(t)
        s.append(np.std([a[k],b[k]]))
    return(av,s)
#ax,by=av_p(BR1TR1,BR1TR2)
#bx,cy=av_p(ax,BR1TR2)
#print(ax,by)
#print(bx)
    

def normlz (x,y):
    xd,yd=[],[]
    
    for ii in range(len(x)):
        j=x[ii]/(sum(x))
        xd.append(j)
        k=y[ii]/(sum(y))
        yd.append(k)
    bd,sm=av_p(xd,yd)
    plt.plot(tm2,xd,'bo',label='BR1TR1')
    plt.plot(tm2,yd,'r^',label='BR2TR1')
    plt.plot(tm2,bd,'k',label='Avergae')
    plt.ylabel('Relative Frequency',fontsize=14)
    plt.xlabel('Time (in min)',fontsize=14)
    plt.ylim(.025,.3)
    plt.legend()
    plt.show()
'''    
    


tk=list(.5*(np.array(BR1T)+np.array(BR2T)))
print(tk)
plt.plot(tm2,BR1T,'-o',label='BR1')
plt.plot(tm2,BR2T,'-o',label='BR2')
plt.plot(tm2,tk,'-o',label='Average')
plt.ylabel('Absolute Count',fontsize=15)
plt.xlabel('Time (hours)',fontsize=15)
plt.ylim(0,5000)
plt.legend()
plt.show()

mix=pd.read_csv('P:/HA452_Motility/Tall Chamber/Analysed/26_11_R5/Mixed_50_50/fin.csv')
#print(mix)
mixb1=mix['BR1']
mixb2=mix['BR2']
tm3=[0,5,10,15,20,30,45,60,90,120]

mixav=list(.5*(np.array(mixb1)+np.array(mixb2)))
#print()
plt.plot(tm3,mixb1,'-o',label='BR1')
plt.plot(tm3,mixb2,'-o',label='BR2')
plt.plot(tm3,mixav,'-o',label='Average')
plt.ylabel('Absolute Count',fontsize=15)
plt.xlabel('Time (hours)',fontsize=15)
plt.ylim(0,5000)
plt.legend()
plt.show()

mixd=[1000,1200,1600,2000,2400,2200,2000,1950]
print(mixav)
mixav=mixav[:-2]
#print(mixav)
tk=tk[:5]+tk[6:9]
tm5=[0,5,10,15,20,25,30,45,60,90,120]
print(tm5[:5]+tm5[6:9])
print(len(mixav),len(mixd),len(tk))
avl=list((np.array(mixav)+np.array(mixd)+np.array(tk))/3)

tm4=[0,5,10,15,20,30,45,60]
plt.plot(tm4,mixd,'-o',label='Average')
plt.plot(tm4,avl,'-co',label='Average')
plt.ylabel('Absolute Count',fontsize=15)
plt.xlabel('Time (hours)',fontsize=15)
plt.ylim(0,5000)
plt.legend()
plt.show()


##############single frames#################
tm6=[0,5,10,15,20,30,45,60,120,180]
b1s=[0,1714,1779,2051,2390,2701,2884,2800,3507,4324]
b2s=[2200,2701,2920,2900,2689,2879,2904,3000,2954,2475]
plt.plot(tm6,b1s,'-o',label='B1s')
plt.plot(tm6,b2s,'-o',label='B2s')
plt.ylabel('Absolute Count',fontsize=15)
plt.xlabel('Time (hours)',fontsize=15)
plt.ylim(0,5000)
plt.legend()
plt.show()

plt.plot(tm6[:7],b2s[:7],'-ro',label='B2s')
plt.ylabel('Absolute Count',fontsize=15)
plt.xlabel('Time (hours)',fontsize=15)
plt.ylim(0,5000)
plt.legend()
plt.show()














