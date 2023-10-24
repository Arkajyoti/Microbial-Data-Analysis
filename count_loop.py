# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 11:18:01 2020

@author: arkajyoti.ghoshal
"""
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 15:10:01 2020

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
###bot=Blue, top=Green
pth='P:/10_8_21-28_11_21/Tall Chamber/26_11/Mixed/'
svp='P:/HA452_Motility/Tall Chamber/Analysed/26_11_R5/Mixed_50_50/BR1/'

tv=90

h1,h2=10,90000000000000000
w1,w2=159,1625
n=1
zv=10
cs='t90_2021-11-26-131022-'
#br=['BR1','BR2']
###No BR as diff BRs can have diff h1,h2####
#s0=list(np.arange(386,8300,434))
#sf=list(np.arange(400,8314,434))
#s0=[2]


#'''
s0=[0]
sf=[11]
#print(s0,sf)



#s0=[125]
#sf=[128]

bl=[]
if not os.path.exists(svp):
            os.makedirs(svp)
            print(svp)
if not os.path.exists(svp+'Anot/'):
            os.makedirs(svp+'Anot/')
            #print(svp)
#print(s0,'***********************',sf)
#imgs,binn=[],[]


#for filename in sorted((os.listdir(pth))[:]):
 #   if filename.endswith('.jpg'):
  #      bl.append(filename)

        
xl0=list(np.arange(0,10,1))
xl1=list(np.arange(10,100,1))
xl2=list(np.arange(100,999+1,1))
xl3=list(np.arange(1000,9999+1,1))
#xl4=list(np.arange(10000,16000+1,1))
#print(xl)

bl=[]
for k in range (len(xl0)):
    ds=cs+str('000')+str(xl0[k])+'.jpg'
    bl.append(ds)
for k1 in range (len(xl1)):
    ds=cs+str('00')+str(xl1[k1])+'.jpg'
    bl.append(ds)
for k2 in range (len(xl2)):
    ds=cs+str('0')+str(xl2[k2])+'.jpg'
    bl.append(ds)
for k3 in range (len(xl3)):
    ds=cs+str(xl3[k3])+'.jpg'
    bl.append(ds)
#for k4 in range (len(xl4)):
  #  ds=cs+str(xl4[k4])+'.jpg'
   # bl.append(ds)

#yy,xx=(imgs[0].shape)
#print(xx,yy)


def binary_im(img):
    
            for jj in range(len(img)):
        #print(jj)
        #fig,ax=plt.subplots(figsize=(xx/96,yy/96))
    
    #print(x)
                f1=img[jj]
        #f1=cv2.cvtColor(fcol, cv2.COLOR_BGR2GRAY)
                bin3 = cv2.adaptiveThreshold(f1,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,11,3)
                bin3 = cv2.medianBlur(bin3,5)
                plt.imshow(bin3,cmap=cm.gray)
#ax.imshow(bin3)
                bin4=bin3-255
                bin4=bin4[h1:h2,w1:w2]
                #print(bin4)
    #bin31=bin4[:,0:250]
   # bin32=bin4[:,1750:h]
        
                binn.append(bin4)
                #fig.savefig(save1+'/Binary//b{0}.png'.format(jj))
            print(')))))))))))',len(binn))
            return(binn)
            

#bin_im=binary_im(imgs)#,20,2025)


     
def filt_count(bin_ims,a_val):
            l=[]
            for kk in range(len(bin_ims)):
                l.append([])
                ims=bin_ims[kk]
                contours, hierarchy = cv2.findContours(ims, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
                for ii in range(len(contours)):
                    cnt=contours[ii]
                    Ar=(cv2.contourArea( cnt))
                    if 0<Ar<a_val:
                        M1=cv2.moments(cnt)
                        cx = int(M1['m10']/M1['m00'])
                        cy = int(M1['m01']/M1['m00'])
                        l[kk].append((cx,cy))
            #print(len(l))
            return(l)
#cc=filt_count(bin_im,60)

def plot_and_df(coord,nm,ki):
                it,cnt=[],[]
                xy=coord[ki]
        #print(xy)
        
                xv,yv=list(zip(*xy))
                pic=imgs[ki]
                fig2,ax2=plt.subplots(figsize=(50,30))
                ax2.imshow(pic[h1:h2,w1:w2],cmap=cm.gray)
                ax2.scatter(xv,yv,edgecolor='r',facecolor='None')
                fig2.savefig(svp+'Anot/'+'t'+str(tv)+'#'+str(nm)+'_anot.png')
                for tz in range(len(coord)):
                    tot=len(coord[tz])
                    it.append(tz+nm)
                    cnt.append(tot)
                #fig2.savefig(svp+str(cn)+'_anot.png')
        
                dff=(pd.DataFrame(zip(it,cnt),columns=['frame','Count']))
                
                dff.to_csv(svp+'t'+str(tv)+'#'+str(nm)+'-'+str(nm+zv)+'.csv')
                print(np.mean(dff['Count']))
                #return(dff,cnt_fr)
#print(bl,s0,'bl,s0')
for kp in range(len(s0)):
    #print(kp)
    print('strt:'+str(s0[kp]),'stp:'+str(sf[kp]))
    imgs,binn=[],[]
    bl1=bl[s0[kp]:sf[kp]] #####init frames#######
    for k8 in bl1:        
        #
        imgs.append(cv2.imread((pth+str('/')+str(k8)),0))
        print(pth+str('/')+str(k8))
    bin_im=binary_im(imgs)
    cc=filt_count(bin_im,60)
    cell_cnt=plot_and_df(cc[:],s0[kp],1)

#print('hhhh',s0[0])     