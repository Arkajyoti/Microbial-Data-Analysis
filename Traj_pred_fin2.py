# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 05:28:48 2020

@author: arkajyoti.ghoshal
"""
import os
import matplotlib as mpl
import matplotlib.pyplot as plt
import cv2
import numpy as np
import pandas as pd

import pims
import trackpy as tp
import cv2
from collections import Counter
import matplotlib.cm as cm
pth1='P:/HA452_Motility/24h_R2_Raw/BR3/'
sv1='C:/PhD/Hak_motility/24hrs/R2/AnalysedF/BR3/'


filter_fr=45 #traj longer than
#n=1025 #no of frames per analysis
#frames,orm=[],[] 
#################def1#######################

h1,h2=30,1850
w1,w2=50,1850
#n1,n2=15,135
#br=['BR1','BR2']
###No BR as diff BRs can have diff h1,h2####
sets=[1,2,3,4,5,6]
tr=['TR1','TR2']
#tr=['New']
pos=['Bot','Top']


for g in range(len(sets)):
    for k in range(len(tr)):
     for l in range(len(pos)):
        pth=pth1+str(sets[g])+'/'+tr[k]+'/'+pos[l]+'/Traj'
        save=sv1+str(sets[g])+'/'+tr[k]+'/'+pos[l]+'/Traj//'
        print(save)
        os.makedirs(save)
        #if pth!=pth1+str(sets[3])+'/'+tr[1]+'/'+pos[1]+'/Traj':
            #n1,n2=15,135
        #else:
        n1,n2=15,135
        #d_fin2=pd.read_csv(save+'res_filt_100.csv')
        #fig,ax=plt.subplots(figsize=(8,5))
        #tp.plot_traj(d_fin2)#,superimpose=framez[j])
        #fig.savefig(save+'traj_fin.png')
           
        
        imgs,binn=[],[]
        for filename in sorted(os.listdir(pth))[n1:n2]:
            print(filename)
            imgs.append(cv2.imread((pth+str('/')+str(filename)),0))
        #return(img)


        yy,xx=(imgs[0].shape)



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
                #bin4=bin3-255
                bin3=bin3[h1:h2,:]
    #bin31=bin4[:,0:250]
   # bin32=bin4[:,1750:h]
        
                binn.append(bin3)
            fig2,ax2=plt.subplots()
            ax2.imshow(binn[0],cmap=cm.gray)
            fig2.savefig(save+'bin_demoF.png')
            return(binn)

        bin_im=binary_im(imgs)#,20,2025)


        def trck(framez):  
   #fr=frames
           df = tp.batch(framez[:], 21, invert=True, minmass=1000,separation=7,threshold=1)
           pred = tp.predict.NearestVelocityPredict()
   #tr = tp.link_df(df, 5, memory=20)
   #for ii in range(len(framez)):
   
   #tr = pred.link_df(df, search_range=5,memory=10)
#print(f1)
   #tp.linking.Linker.MAX_SUB_NET_SIZE = 50
   #tp.linking.Linker.MAX_SUB_NET_SIZE_ADAPTIVE = 30
           f_iter = (frame for fnum, frame in df.groupby('frame'))
#t0=time.time()
           tr = pd.concat(pred.link_df_iter(f_iter,
                                  search_range=12,
                                  memory=5,
                                  adaptive_stop=5,
                                  adaptive_step=0.95))
           
           tr.to_csv(save+'Tot_resultF.csv')
           key=[]
           xk=list(tr['particle'])
#print(xk)

           mn=Counter(xk)
#print(mn)
           for jj,ii in (mn.items()):
            if ii>filter_fr:
        #print(ii)
             key.append(jj)
           key_df=pd.DataFrame(key,columns= ['particle'])
#print (rd2)
           d_fin=key_df.merge(tr, on= 'particle',how='inner')
           d_fin.to_csv(save+'res_filt_45F.csv')

        
        trck(bin_im)
    #return(d_fin)
#D=track(frames,'dump//',orm)  
#print(D) 

        
     
     #ax.set_xlim(0,2048)
     #ax.set_ylim(650,1370)
     
     #fig.savefig(save+str(n)+'/Traj//'+str(j)+'.png')
     
           
###############################################################



#trck(frames2,'Mid',save1,x2,y2)
     
'''
###########check tp anotate############

dp=[]
dc=[]
p=cv2.imread('P:/HA452_Motility/24h_R2/Old_new/1/New/Top/Traj/fc2_save_2020-06-10-115454-0001.tif',0)
plt.imshow(p)
p1=p[h1:h2,:]
bin3 = cv2.adaptiveThreshold(p1,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,31,9)
bin3 = cv2.medianBlur(bin3,7)
#ax.imshow(bin3)
bin4=bin3-255
bin3=bin3[h1:h2,:]

f1 = tp.locate(p1, 25, invert=True, minmass=800,separation=7,threshold=1)
f2=tp.locate(bin3, 21, invert=True, minmass=1000,separation=7,threshold=1)
fig,ax=plt.subplots(figsize=(40,30))
#tp.annotate(f1,p1)
tp.annotate(f1,p1)
fig2,ax2=plt.subplots(figsize=(40,30))
#tp.annotate(f1,p1)
tp.annotate(f2,bin3)         
'''
