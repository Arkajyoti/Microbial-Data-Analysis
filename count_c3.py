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
import time
###bot=Blue, top=Green
seconds = time.time()
local_time = time.ctime(seconds)
print("Experiment Begins,Local time:", local_time)



def binary_im(imgs):
    binn=[]
    #print(imgs)
    for jj in range(len(imgs)):
#print(jj)
#fig,ax=plt.subplots(figsize=(xx/96,yy/96))

#print(x)
        f1=imgs[jj]
#f1=cv2.cvtColor(fcol, cv2.COLOR_BGR2GRAY)
        bin3 = cv2.adaptiveThreshold(f1,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
    cv2.THRESH_BINARY,67,9)
        bin3 = cv2.medianBlur(bin3,7)
        #print(bin3)
        plt.imshow(bin3,cmap=cm.gray)
        #plt.close()
#ax.imshow(bin3)
        #bin4=bin3-255
        #bin4=bin4[h1:h2,:]
#bin31=bin4[:,0:250]
   # bin32=bin4[:,1750:h]

        binn.append(bin3)
        #fig.savefig(save1+'/Binary//b{0}.png'.format(jj))
    return(binn)


 
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



def plot_and_df(imgs,coord,sv3):
    dff=pd.DataFrame(columns=['frame','yval'])
    
    cnt_fr=[]

    cn=0
    for ll in range(len(coord)):
        xy=coord[ll]
#print(xy)

        xv,yv=list(zip(*xy))
        pic=imgs[ll]
        fig2,ax2=plt.subplots(figsize=(20,15))
        ax2.imshow(pic,cmap=cm.gray)
        ax2.scatter(xv,yv,edgecolor='r',facecolor='None')
        frn=[cn]*len(yv)
        cnt_fr.append(len(yv))
        fig2.savefig(sv3+str(ll+1)+'_anot.png')
        #print('ha')
        plt.close(fig2)
        cnt_fr.append(len(xv))
        df1=(pd.DataFrame(zip([cn],[len(yv)]),columns=['frame','yval']))
        dff=dff.append(df1)
        #cn=cn+n
        dff.to_csv(sv3+str(ll+1)+'cnt.csv')
        #print(cnt_fr)
        #print('hi')
    #print(dff)
    return(list(dff['yval']))

####fin_hist
#n2=['fc2_save_2021-08-31-175921-00','fc2_save_2021-08-31-175940-00','fc2_save_2021-08-31-175957-00','fc2_save_2021-08-31-180014-00']
#            ld=plot_and_df(imgs,lc,sv2)
#n3=['fc2_save_2021-09-06-161908-00']
#n3=['fc2_save_2021-09-06-141903-00','fc2_save_2021-09-06-141938-00','fc2_save_2021-09-06-142030-00','fc2_save_2021-09-06-142056-00','fc2_save_2021-09-06-142123-00','fc2_save_2021-09-06-142149-00']
#n3=['fc2_save_2021-09-06-150337-00','fc2_save_2021-09-06-150404-00','fc2_save_2021-09-06-150432-00','fc2_save_2021-09-06-150458-00',]            
#file:///P:/HA452_Motility/Agarose coin/19_4_22/TC/c1/ct_30
t2=['30','60','90','150']
t2=['0','30','60','120']
#t0=['30m']
for ki in range(len(t2)):
    pt='P:/HA452_Motility/Agarose coin/20_4_22/TC/c3/ex_'+t2[ki]+'/'
    
    svq='P:/HA452_Motility/Agarose coin/Analysed/R11/Topcell/BC/'+t2[ki]+'/'   
#pt='P:/HA452_Motility/Agarose coin/21_3_22/BC/Control/30m/c1'
#svq='P:/HA452_Motility/Agarose coin/Analysed/R7/Botcell/Control/BC/'    
    fn,fn2=[],[]
    for kk in sorted(os.listdir(pt)):
        #fn2.append[kk]
        if kk.startswith('fc2'):
            kk=kk[:-4]
            if not kk.endswith('.jpg'):
                fn.append(kk[:-4])
        #fn.append(kk)
    fns=list(set(fn))
    rn=sorted(fns,key = lambda x:x[-7:-2])
    #print('setfilter:',rn)
    #rn=rn[-1:]
    print('setfilter:',rn)
    #fr=list(range(10,90,n))
    
    sr=list(range(8,2048,204))
    sr=sr+[2048]
    for ia in range(len(rn)):
        xu=[]
        rnn=rn[ia]
        print('it:',ia,'len:',len(rn),len(rn[:-1]))
       
        fr=list(range(10,30,4))
        print(fr)
        for ib in range(len(fr)):
            frr=fr[ib]
            fm=pt+rnn+str('00')+str(frr)+'.jpg'
            #print(fm)
            fmm=cv2.imread(fm,0)
            #print(fmm)
            fulfrm=[]
            for ic in range(len(sr)-1):
                sa,sb=sr[ic],sr[ic+1]
                fulfrm.append(fmm[sa:sb,:])
                #print(rn[ia],fr[ib],sa,sb)
            #print(len(fulfrm))
            #plt.imshow(fulfrm[0])
            #plt.show()
            #for ig in range(len(fulfrm)):
                #plt.imshow(fulfrm[ig])
                #plt.show()
                #print('xxxxxxxxxxxxxxxx')
            xa=binary_im(fulfrm)
            #for ig in range(len(xa)):
                #plt.imshow(xa[ig])
                #plt.show()
                #print('yyyyyyyyyyyyyy')
            xb=filt_count(xa,60)
            
            svz=svq+str(rnn)+'/'+str(frr)+'/'
            print(svz)
            if not os.path.exists(svz):
                   os.makedirs(svz)
                   xc=plot_and_df(fulfrm,xb,svz)
                   #print('oooo',xc)
                   xu.append(xc)
        xd=np.array(xu)
        dfx=pd.DataFrame()
        xg=[]
        xe=(np.mean((xd),axis=0))
        #print(len(xd))
        for xf in range(len(xd)):
            dc1=xd[xf]
            dcf=pd.DataFrame(dc1,columns=['y'+str(xf)])
            dfx=dfx.append(dcf)
        
        xg=pd.DataFrame(xe,columns=['yval'])
        dfx=dfx.append(xg)
        dfx = dfx.apply(lambda x: pd.Series(x.dropna().values))
        #print(dfx)
            
        #print(dfx)
        dfx.to_csv(svq+str(rnn)+'/'+'comb.csv')
                #print(svz)#len(xb))
                
    seconds2 = time.time()
    local_time2 = time.ctime(seconds2)
    print("Experiment Ends,Local time:", local_time2)
    #print(local_time2-local_time)