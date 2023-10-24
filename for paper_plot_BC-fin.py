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
    
    cmb,ubz,ccc=[],[],[]
    for ny in range(len(t)):
        yc2=pd.read_csv(pt+str(t[ny])+'/'+'count.csv')
        #af=yc2['frm']
        #afc=len((list(set(af))))
        print(pt+str(t[ny])+'/'+'count.csv')
        cnv=[]
        ll=[]
        for kc in range(len(frms)):
            
            dff=yc2[(yc2.frm==frms[kc])]
            #print(dff)
            yc1=dff['yval']
            #print(yc1[:4])
            cn,bn=np.histogram(yc1,bins=20)
            ll.append(np.sum(cn))
            #print(sum(cn))
            cn=cn/sum(cn)
            cnv.append(list(cn))
        ccc.append(ll)
            
            
        
        mpp=np.mean(cnv,axis=0)
        cmb.append(list(mpp))
        bv=ubs(mpp)
        #print('hhh',mpp)
        ubz.append(bv)
    print(ccc)
    return(ccc,cmb,ubz)
        
        
        

tym=[0,20,60,120]
############### BR1 ########################
p1='P:/HA452_Motility/Physical Sig/Analysed/20_8_22/Analysed-v2/BC/'
ckk,avd,avb=matt(tym,p1)
#print(avd,avb)

############### BR2 ########################
p2='P:/HA452_Motility/Physical Sig/Analysed/29_8_22/Analysed-v2/BC/'
ckk2,avd2,avb2=matt(tym,p2)
#print(avd2,avb2)

############### BR3 #######################
p3='P:/HA452_Motility/Physical Sig/Analysed/7_10_22/BC/'
ckk3,avd3,avb3=matt(tym,p3)

############### BR3 #######################
p4='P:/HA452_Motility/Physical Sig/Analysed/28_10_22/BC/'
ckk4,avd4,avb4=matt(tym,p4)

############### plots################
tymcol=['purple','#f75394','cyan','slateblue']
mbs,sbs=np.mean([avb,avb2,avb3,avb4],axis=0),np.std([avb,avb2,avb3,avb4],axis=0)
#print(mbs)
plt.rcParams["font.family"] = "Times new roman"
plt.bar(['0','20','60','120'],mbs,yerr=sbs,capsize=5,color='r')
plt.ylim(-0.25,0.55)
plt.show()
for dk2 in range(len(tym)):
    plt.gcf().set_size_inches(5,3)
    if dk2==3:
        mbs[dk2]=.01
    plt.bar(str(tym[dk2]),mbs[dk2],yerr=sbs[dk2],label=str(tym[dk2]),color=tymcol[dk2],capsize=5)
    print(dk2,mbs[dk2])
    plt.ylim(-0.35,0.7)
plt.show()
#print(mbs)
xaxs=list(np.arange(0,2000,100))
mds,sds=np.mean([avd,avd2,avd3,avd4],axis=0),np.std([avd,avd2,avd3,avd4],axis=0)
for dk in range(len(tym)):
    plt.errorbar(xaxs,mds[dk],label=str(tym[dk]),color=tymcol[dk])
    plt.fill_between(xaxs, mds[dk]-sds[dk], mds[dk]+sds[dk],facecolor=tymcol[dk],
    alpha=.35)#,linewidth=20,edgecolor='k')#tymcol[dk],facecolor=tymcol[dk])
    #linewidth=4, linestyle='dashdot')
    plt.gca().yaxis.tick_right()
    plt.ylim(0.015,0.15)
    plt.xlim(-20,1930)
    plt.legend(fontsize=12,loc='upper center')
    
plt.show()
print('**'*25*2)   
print('Mean', 'Stdev',np.mean([ckk,ckk2,ckk3,ckk4]),np.std([ckk,ckk2,ckk3,ckk4]))



plt.plot(['0','20','60','120'],[np.mean(ckk[0]),np.mean(ckk[1]),np.mean(ckk[2]),np.mean(ckk[3])],'o-',color='b',label='BR1')
plt.plot(['0','20','60','120'],[np.mean(ckk2[0]),np.mean(ckk2[1]),np.mean(ckk2[2]),np.mean(ckk2[3])],'o-',color='r',label='BR2')
plt.plot(['0','20','60','120'],[np.mean(ckk3[0]),np.mean(ckk3[1]),np.mean(ckk3[2]),np.mean(ckk3[3])],'o-',color='g',label='BR3')
plt.plot(['0','20','60','120'],[np.mean(ckk4[0]),np.mean(ckk4[1]),np.mean(ckk4[2]),np.mean(ckk4[3])],'o-',color='y',label='BR4')
plt.legend()
print('Cell count at t=0 is non-uniform. It is important that cell count amongst t=20 to 120 remain identical')