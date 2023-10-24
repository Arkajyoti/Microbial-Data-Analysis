# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 18:49:32 2021

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

PAR=[]
FvmT=[.619,.85,.65,.7,.87,.56]
FvmB=[.6,.77,.64,.55,.68,.66]

plt.plot(FvmT,'g',marker='o',label='Top')
plt.plot(FvmB,'b',marker='^',label='Bot')
plt.ylim(.3,1.3)
plt.ylabel('Fv/Fm',fontsize=12)
plt.xlabel('Replicates',fontsize=12)
plt.legend()
plt.show()
z=plt.bar(['Top','Bottom'],[np.mean(FvmT),np.mean(FvmB)],yerr=[np.std(FvmT),np.std(FvmB)])
z[0].set_color('g')
z[1].set_color('b')
plt.ylabel('Fv/Fm',fontsize=12)#,fontweight=224)
#plt.xlabel('Fv/Fm',fontsize=12)
plt.show()

EtmT=[77.9,73.6,55.2,74.7,64.3,63.3]
EtmB=[69.4,62.4,55.3,66.2,59.2,56.8]

plt.plot(EtmT,'g',marker='o',label='Top')
plt.plot(EtmB,'b',marker='^',label='Bot')
#plt.ylim(.3,1.3)
plt.ylabel('ETR_Max',fontsize=12)
plt.xlabel('Replicates',fontsize=12)
plt.legend()
plt.show()
z=plt.bar(['Top','Bottom'],[np.mean(EtmT),np.mean(EtmB)],yerr=[np.std(EtmT),np.std(EtmB)])
z[0].set_color('g')
z[1].set_color('b')
plt.ylabel('ETR_Max',fontsize=12)

bot1=pd.read_csv('file:///P:/Hak Molecular/HA452_Molecular/PAM/For FD/16_7_PAM/Bot/B1T1B.CSV')['NPQ']
bot2=pd.read_csv('file:///P:/Hak Molecular/HA452_Molecular/PAM/For FD/16_7_PAM/Bot/B1T2B.CSV')
bot3=pd.read_csv('file:///P:/Hak Molecular/HA452_Molecular/PAM/For FD/16_7_PAM/Bot/B2T2B.CSV')

print(bot1)