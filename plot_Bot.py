# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 16:44:48 2021

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

col=['r','k','b','g','y','cyan','olive','brown','aquamarine','blanchedalmond','chartreuse','coral','darkorchid2','deeppink1']
##experiment setup: c1,c2=cells only,c3=cells+BC,c4=cells+TC##############

############controls 30m###################

#Cc1_30m=pd.read_csv('P:/HA452_Motility/Agarose coin/Analysed/R10/Botcell/Control_A/30/combf.csv')['yval']
#Cc2_30m=pd.read_csv('P:/HA452_Motility/Agarose coin/Analysed/R10/Botcell/Control_B/30/combf.csv')['yval']
Cc3_30m=pd.read_csv('P:/HA452_Motility/Agarose coin/Analysed/R11/Botcell/BC/0/combf.csv')['yval'][2:]
Cc4_30m=pd.read_csv('P:/HA452_Motility/Agarose coin/Analysed/R11/Botcell/TC/0/combf.csv')['yval']
L1=[list(Cc3_30m),list(Cc4_30m)]

#print(L1,len(L1))

def plts(o,n):
    for ii in range(len(o)):
        #print(o[ii])
        l2=list(range(0,len(o[ii])))
        #print(len(l2))
        plt.bar(l2,o[ii],facecolor=col[n+ii])
        plt.ylim(0,600)
        print('1en',len(o[ii]))
        print('cnt','cc',np.sum(np.array(o[ii])))
        plt.show()

def norm(x):
    return(np.array(x)/np.sum(np.array(x)))
    


def Bv(a,b,c,d,t):
    an,bn,cn,dn=norm(a),norm(b),norm(c),norm(d)
    Bcn1=cn[:16]-an[:16]
    Bcn2=cn[-16:]-an[-16:]
    Tcn1=dn[:16]-bn[:16]
    Tcn2=dn[-16:]-bn[-16:]
    ddn1=(Tcn1-Bcn1)
    ddn2=(Tcn2-Bcn2)
    Nn1=np.sum(ddn1) #### atleast 48 elements so 1/3rd is 16####
    Nn2=np.sum(ddn2)
    print('***',Nn1-Nn2,Nn1+Nn2)
    NB=(Nn1-Nn2)/(Nn1+Nn2)
    print('Normal_method_'+t,np.round(Nn1,3),np.round(Nn2,3),np.round(NB,3))
    Dn1=-(dn[:16]-cn[:16])
    Dn2=-(dn[-16:]-cn[-16:])
    Mn1=np.sum(Dn1) #### atleast 48 elements so 1/3rd is 16####
    Mn2=np.sum(Dn2)
    MB=(Mn1-Mn2)/(Mn1+Mn2)
    print('Master_method'+t,np.round(Mn1,3),np.round(Mn2,3),np.round(MB,3))
    lz=list(range(0,len(ddn1)))
    plt.ylim(-.02,.02)
    plt.bar(lz,ddn1,facecolor='violet')
    plt.show()
    plt.ylim(-.02,.02)
    plt.bar(lz,ddn2,facecolor='b')
    plt.show()
    


  
plts(L1,2)
'''        
############controls 60m###################

#Cc1_60m=pd.read_csv('P:/HA452_Motility/Agarose coin/Analysed/R10/Botcell/Control_A/60/combf.csv')['yval']
#Cc2_60m=pd.read_csv('P:/HA452_Motility/Agarose coin/Analysed/R10/Botcell/Control_B/60/combf.csv')['yval']

#L2=[list(Cc1_60m),list(Cc2_60m)]
#plts(L2,4)
'''
############Experiments 30m###################

Ec3_30m=pd.read_csv('P:/HA452_Motility/Agarose coin/Analysed/R11/Botcell/BC/30/combf.csv')['yval']#[1:-4]
Ec4_30m=pd.read_csv('P:/HA452_Motility/Agarose coin/Analysed/R11/Botcell/TC/30/combf.csv')['yval']#[1:-4]

L3=[list(Ec3_30m),list(Ec4_30m)]
plts(L3,6)


##### normal method#####


Bv(Cc3_30m,Cc4_30m,Ec3_30m,Ec4_30m,'30m')



############Experiments 60m###################

Ec3_60m=pd.read_csv('P:/HA452_Motility/Agarose coin/Analysed/R11/Botcell/BC/60/combf.csv')['yval']
Ec4_60m=pd.read_csv('P:/HA452_Motility/Agarose coin/Analysed/R11/Botcell/TC/60/combf.csv')['yval'][1:]

L4=[list(Ec3_60m),list(Ec4_60m)]
plts(L4,10)
Bv(Cc3_30m,Cc4_30m,Ec3_60m,Ec4_60m,'60m')


############Experiments 120m###################

Ec3_120m=pd.read_csv('P:/HA452_Motility/Agarose coin/Analysed/R11/Botcell/BC/120/combf.csv')['yval']
Ec4_120m=pd.read_csv('P:/HA452_Motility/Agarose coin/Analysed/R11/Botcell/TC/120/combf.csv')['yval']

L5=[list(Ec3_120m),list(Ec4_120m)]
plts(L5,8)
Bv(Cc3_30m,Cc4_30m,Ec3_120m,Ec4_120m,'120m')


