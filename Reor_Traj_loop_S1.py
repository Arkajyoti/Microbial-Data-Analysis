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


h1,h2=30,1900
w1,w2=170,1900

###################################
'''
dp=[]
dc=[]
p=cv2.imread('P:/HA452_Motility/24h_R2/BR3/4/TR1/Top/Reor/fc2_save_2020-06-07-015042-0061.tif',0)
plt.imshow(p)
p1=p[h1:h2,:]
bin3 = cv2.adaptiveThreshold(p1,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,31,9)
bin3 = cv2.medianBlur(bin3,7)
#ax.imshow(bin3)
bin4=bin3-255
bin3=bin3[h1:h2,:]

f1 = tp.locate(p1, 25, invert=True, minmass=880,separation=20,threshold=1)
#f2=tp.locate(bin3, 21, invert=True, minmass=1900,separation=15,threshold=.0001)
#fig,ax=plt.subplots(figsize=(15,12))
#tp.annotate(f1,p1)
#tp.annotate(f1,p1)
fig2,ax2=plt.subplots(figsize=(25,22))
tp.annotate(f1,p1)
#tp.annotate(f2,bin3)         

'''
###################################################





#pth1='P:/HA452_Motility/24h_R2/BR1/6/TR1/Top/Reor/'
#sv1='C:/PhD/Hak_motility/24hrs/R2/Analysed_Reor/BR3/6/TR1/Top/Reor/S2/Py/'


filter_fr=45 #traj longer than
#n=1025 #no of frames per analysis
#frames,orm=[],[] 
#################def1#######################




imgs,binn=[],[]

#return(img)


#yy,xx=(imgs[0].shape)



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
            fig2,ax2=plt.subplots(nrows=1,ncols=2,figsize=(22,20))
            ax2[0].imshow(binn[0],cmap=cm.gray)
            
            ax2[1].imshow(imgs[0],cmap=cm.gray)
            fig2.savefig(save+'bin_demoF.png')
            print(save+'bin_demoF.png')
            return(binn)

#bin_im=binary_im(imgs)#,20,2025)


def trck(framez):  
   #fr=frames
           df = tp.batch(framez[:], 21, invert=True, minmass=880,separation=17,threshold=1)
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
                                  search_range=15,
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
           

        
#trck(bin_im)
    #return(d_fin)
#D=track(frames,'dump//',orm)  
#print(D) 

        
     
     #ax.set_xlim(0,2048)
     #ax.set_ylim(650,1370)
     
     #fig.savefig(save+str(n)+'/Traj//'+str(j)+'.png')
     
           
###############################################################



pth='P:/HA452_Motility/24h_R2/'
svz='C:/PhD/Hak_motility/24hrs/R2/Analysed_Reor/'
#sd=['UF','DF']
d,p='6/','Top/'
c=0
b=['BR1/','BR2/','BR3/']
t=['TR1/','TR2/']
#s=['S1/','S2/']
n=[37,43,40,41,36,36]
for ai in range(len(b)):
    for bi in range(len(t)):
        #for ci in range(len(s)):
                #pthf=P:/HA452_Motility/24h_R2/BR3/6/TR1/Bot/Reor/fc2_save_2020-06-07-083331-0001.tif
                pthf= pth+b[ai]+d+t[bi]+p+'/Reor/'
                save=svz+b[ai]+d+t[bi]+p+'/Reor/S1/Py/'
                
                n1=n[c]
                n2=n1+160
                #print('path:',pthf,'/n','sev:',save)
                if not os.path.exists(save):
    #os.makedirs(directory)
                    os.makedirs(save)
                save=save+'/'
                for filename in sorted(os.listdir(pthf))[n1:n2]:
                    print(filename)
                    imgs.append(cv2.imread((pthf+str('/')+str(filename)),0))
                bin_im=binary_im(imgs)
                trck(bin_im)
                imgs,binn=[],[]
                c=c+1
                
                