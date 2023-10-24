# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 17:19:32 2020

@author: arkajyoti.ghoshal
"""

import numpy as np
import multiprocessing
import pylab
from pylab import *
from skimage.io import imread
#print(multiprocessing.cpu_count())
#basic code
from openpiv import tools, process, validation, filters, scaling 

import matplotlib.pyplot as plt
from openpiv import  pyprocess
folder_R1='C:/PhD/PIV/Anh/Good_data/Analysis/Monolayer/Results//'
folder_Q1='C:/PhD/PIV/Anh/Good_data/Analysis/Monolayer/Quiver//'
#name=str(folder[:-1]+'\\Ext_srch\\pass1.txt')
path='C:/PhD/PIV/Anh/Good_data/_Experiment_Time Lapse_20191109_367_/rawframes_cropped_26_301'
'''
for i in range(26,99):
    frame_a  = tools.imread( path+'//crop0'+str(i+0)+'.tif'  )
    frame_b  = tools.imread( path+'//crop0'+str(i+1)+'.tif'  )
#name=str(folder[:-1]+'\Ext_srch\\pass1'+str(i)+'.txt')
#fig,ax=plt.subplots(figsize=(12,10))
#subplot(1,2,1)
#imshow(frame_a,cmap=cm.gray)
#subplot(1,2,2)
#imshow(frame_b,cmap=cm.gray)


 #fig,ax = plt.subplots(1,2)
#ax[0].imshow(frame_a,cmap=plt.cm.gray)
#ax[1].imshow(frame_b,cmap=plt.cm.gray)
    winsize = 32 # pixels
    searchsize = 32
  # pixels, search in image B
    overlap = 20 # pixels
    dt = .1 # sec
    u0, v0, sig2noise = process.extended_search_area_piv( frame_a.astype(np.int32), frame_b.astype(np.int32), window_size=winsize, overlap=overlap, dt=dt, search_area_size=searchsize, sig2noise_method='peak2peak' )
    x, y = process.get_coordinates( image_size=frame_a.shape, window_size=winsize, overlap=overlap )
    u1, v1, mask = validation.sig2noise_val( u0, v0, sig2noise, threshold = 1.2 )
    u2, v2 = filters.replace_outliers( u1, v1, method='localmean', max_iter=50, kernel_size=2.5)
    x, y, u3, v3 = scaling.uniform(x, y, u2, v2, scaling_factor = 100000 )

    tools.save(x, y, u3, v3, mask, folder_R1+'R'+str(i)+'.csv',delimiter='\t' )
    #tools.display_vector_field(name, scale=100, width=0.0025)
    fig,ax = plt.subplots(figsize=(12,12))
#ax.imshow(plt.imread('C:\PhD\Images\FD2_1\\'+str(1)+' '+'('+str(px)+')'+'.tif')[::-1,:],cmap=plt.cm.gray,origin='lower')
    ax.quiver(x*100,y*100,u3*100,v3*100,color='green',units='xy',angles='xy',scale=1.25)
    plt.savefig(folder_Q1+'Q'+str(i)+'.png')
''' 
folder_R2='C:/PhD/PIV/Anh/Good_data/Analysis/Multilayer/Results//'
folder_Q2='C:/PhD/PIV/Anh/Good_data/Analysis/Multilayer/Quiver//'
for i in range(299,300):
    frame_a  = tools.imread( path+'//crop'+str(i+0)+'.tif'  )
    frame_b  = tools.imread( path+'//crop'+str(i+1)+'.tif'  )
#name=str(folder[:-1]+'\Ext_srch\\pass1'+str(i)+'.txt')
#fig,ax=plt.subplots(figsize=(12,10))
#subplot(1,2,1)
#imshow(frame_a,cmap=cm.gray)
#subplot(1,2,2)
#imshow(frame_b,cmap=cm.gray)


 #fig,ax = plt.subplots(1,2)
#ax[0].imshow(frame_a,cmap=plt.cm.gray)
#ax[1].imshow(frame_b,cmap=plt.cm.gray)
    winsize = 32 # pixels
    searchsize = 32
  # pixels, search in image B
    overlap = 20 # pixels
    dt = .05 # sec
    u0, v0, sig2noise = process.extended_search_area_piv( frame_a.astype(np.int32), frame_b.astype(np.int32), window_size=winsize, overlap=overlap, dt=dt, search_area_size=searchsize, sig2noise_method='peak2peak' )
    x, y = process.get_coordinates( image_size=frame_a.shape, window_size=winsize, overlap=overlap )
    u1, v1, mask = validation.sig2noise_val( u0, v0, sig2noise, threshold = 1 )
    u2, v2 = filters.replace_outliers( u1, v1, method='localmean', max_iter=50, kernel_size=2.5)
    x, y, u3, v3 = scaling.uniform(x, y, u2, v2, scaling_factor = 100000 )

   # tools.save(x, y, u3, v3, mask, folder_R2+'R'+str(i)+'.csv',delimiter='\t' )
    #tools.display_vector_field(name, scale=100, width=0.0025)
    fig,ax = plt.subplots(figsize=(12,12))
#ax.imshow(plt.imread('C:\PhD\Images\FD2_1\\'+str(1)+' '+'('+str(px)+')'+'.tif')[::-1,:],cmap=plt.cm.gray,origin='lower')
    ax.quiver(x*100,y*100,u3*100,v3*100,color='green',units='xy',angles='xy',scale=1)
    #plt.savefig(folder_Q2+'Q'+str(i)+'.png')

