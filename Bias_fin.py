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
pthB='P:/HA452_Motility/24h_R2/BR1/'
svB='C:/PhD/Hak_motility/24hrs/R2/Analysed/BR1/'#3/TR2/Top/Bias//'
h1,h2=30,2020
n=4
#br=['BR1','BR2']
###No BR as diff BRs can have diff h1,h2####
sets=[1,2,3,4,5,6]
tr=['TR1','TR2']
pos=['Top','Bot']


for g in range(len(sets)):
    for k in range(len(tr)):
     for l in range(len(pos)):
        pth=pthB+str(sets[g])+'/'+tr[k]+'/'+pos[l]+'/Bias'
        svp=svB+str(sets[g])+'/'+tr[k]+'/'+pos[l]+'/Bias//'
        print(svp)

        imgs,binn=[],[]
        for filename in (os.listdir(pth))[::n]:
        #print(filename)
            imgs.append(cv2.imread((pth+str('/')+str(filename)),0))
        #return(img)

#raw_im=read_im(pthB,1)
#print(len(imgs))
#plt.gcf().set_size_inches(10,5)
#plt.imshow(imgs[5],cmap=cm.gray)
        yy,xx=(imgs[0].shape)
#print(xx,yy)



        def binary_im(img):
    
            for jj in range(len(img)):
        #print(jj)
        #fig,ax=plt.subplots(figsize=(xx/96,yy/96))
    
    #print(x)
                f1=img[jj]
        #f1=cv2.cvtColor(fcol, cv2.COLOR_BGR2GRAY)
                bin3 = cv2.adaptiveThreshold(f1,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,31,9)
                bin3 = cv2.medianBlur(bin3,7)
#ax.imshow(bin3)
                bin4=bin3-255
                bin4=bin4[h1:h2,:]
    #bin31=bin4[:,0:250]
   # bin32=bin4[:,1750:h]
        
                binn.append(bin4)
                #fig.savefig(save1+'/Binary//b{0}.png'.format(jj))
            return(binn)

        bin_im=binary_im(imgs)#,20,2025)
#print(len(bin_im))
#plt.imshow(bin_im[0],cmap=cm.gray)
#plt.show()
#Ara=[]
#contours, hierarchy = cv2.findContours(bin_im[0], cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#for ii in range(len(contours)):
#           cnt=contours[ii]
#           Ar=(cv2.contourArea( cnt))
#           Ara.append(Ar)
    #area.append(Ar)
        #print(len(area))
#plt.hist(Ara,bins=500,edgecolor='k')
#plt.gca().set_xlim([0,30])
#plt.show()
#print(np.median(Ara))
     
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
            return(l)
        cc=filt_count(bin_im,22)

        def plot_and_df(coord):
            dff=pd.DataFrame(columns=['frame','yval'])
            
            cnt_fr=[]
    
            cn=0
            for ll in range(len(coord)):
                xy=coord[ll]
        #print(xy)
        
                xv,yv=list(zip(*xy))
                pic=imgs[ll]
                fig2,ax2=plt.subplots(figsize=(20,15))
                ax2.imshow(pic[h1:h2,:],cmap=cm.gray)
                ax2.scatter(xv,yv,edgecolor='r',facecolor='None')
                frn=[cn]*len(yv)
                cnt_fr.append(len(yv))
                fig2.savefig(svp+str(cn)+'_anot.png')
        
                df1=(pd.DataFrame(zip(frn,yv),columns=['frame','yval']))
                dff=dff.append(df1)
                cn=cn+n
                dff.to_csv(svp+'y_combined.csv')
            return(dff,cnt_fr)

####fin_hist
        dd,cell_cnt=plot_and_df(cc[:])
#print(cell_cnt)   
        norm=np.mean(cell_cnt)   
#print(norm)
        
        yvl=list(dd['yval'])
#print(yvl)
        counts,bins=np.histogram(yvl)
#print(counts,bins)
        fig3,ax3=plt.subplots(figsize=(6,9))
        ax3.hist(yvl,bins=20,edgecolor='k',weights=(1/(len(imgs)*norm))*np.ones(len(yvl)),label='N='+str(round(norm)))
        ax3.set_ylabel ('Normalized count',size=15)
        ax3.set_xlabel('Channel height (pix)',size=15)
        ax3.tick_params(axis='both', which='major', labelsize=15)
        ax3.yaxis.set_ticks_position("right")
#ax3.yaxis.set_label_coords(5, 4.5)
        ax3.yaxis.set_label_position("right")
        ax3.legend(fontsize=15)
        ax3.set_ylim(0,.3)
        plt.yticks(rotation=90)
#plt.rc('axes',labelsize=15)
        fig3.savefig(svp+'hist_combined.png')
        
       
