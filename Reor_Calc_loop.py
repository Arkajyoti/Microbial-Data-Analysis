# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 18:53:43 2020

@author: arkajyoti.ghoshal
"""
from scipy import interpolate
import numpy as np
import pandas as pd
import trackpy as tp
import matplotlib.pyplot as plt
import statistics as st

from collections import Counter

fps=1/16
sclz=1000/580
#pth='C:/PhD/H3107/Old/T2/S1/Py/'#Tot_resultF.csv'
#df8=pd.read_csv(pth+'res_Full_P.csv')

#pth='C:/PhD/H3107/Old/T2/S1/Py/'#Tot_resultF.csv'
#df8=pd.read_csv(pth+'res_Full_P.csv')
d,p=['1/'],['Bot/']#,'Bot/']

b=['BR1/','BR2/','BR3/']
t=['TR1/','TR2/']
s=['S1/','S2/']
sgnz,lo='Up','UF'
pth='C:/PhD/Hak_motility/24hrs/R2/Analysed_Reor/'


import time
st_t=time.time()

def h(l):
    ln=np.array(l)
    
    k=ln[1:]-ln[:-1]
    return(k)



def bin_omega(omg,th_D,syz):
        #print('hhhhooo', len(omg),'pppooo',len(tht))
        #tht=tht[1:]
        #th_D=np.degrees(tht)
        #sdv=[]
        sort_omg=[]
        sort_tht=[]
        bins=np.arange(-180,185,syz) ######1st and last val missing##########
        #print('bins:',(bins),len(bins),bins[6],bins[-1])
        for po in range(len(bins)-1):
            bln2=[]
            
            for op in range(len(omg)):
                if bins[po]<(th_D[op])<=bins[po+1]:
                    bln2.append(omg[op])
            #print(bln2,(tht[po]+tht[po+1])/2)#,av_omg=(sum(bln2))/len(bln2)) 
            if len(bln2)>0:
             #   print(np.degrees(tht[po]+tht[po+1])/2)
                av_omg=np.mean(bln2)
                #s_omg=np.std(bln2)
                #sdv.append(s_omg)
                sort_tht.append((bins[po]+bins[po+1])/2)
                sort_omg.append(av_omg)
            elif len(bln2)==0:
                print([],(bins[po]+bins[po+1])/2)
        
        #plt.ylim(-.5,.5)
        #plt.plot(sort_tht,sort_omg,'o',color=col)
        #plt.savefig('C:/Users/arkajyoti.ghoshal/Documents/Python Scripts/reor d/8//'+str(col)+'.jpg')
        #plt.show()
        #print('b4',sort_omg)
        for rr in range(len(sort_tht)):
            if sort_omg[rr]>.5 or sort_omg[rr]<-.5:
                #print(sort_omg[rr])
                sort_omg[rr]=0
        #sort_omg[11]=0
        #sort_omg[23]=0
        #print('a4',sort_omg)
        return(sort_tht,sort_omg)
 

########################################################
def sfit(data,thtt,sgn,guess_amplitude,pth1) :
    from scipy.optimize import curve_fit

    #print(len(data),len(sdd))
#N = 1000 # number of data points
    t = (np.linspace(min(thtt),max(thtt),len(thtt)))
    #print(t,'ooooooo')
    #print(np.radians(t))
    t=np.radians(t)
    if sgn=='Up':
        k=-1
        cl='g'
        
    elif sgn=='Dwn':
        k=1
        cl='b'
        
        
    guess_freq = 1
    guess_amplitude = guess_amplitude*k#3*np.std(data)/(2**0.5)
    guess_phase = 0
    guess_offset = 0
    
    p0=[guess_freq, guess_amplitude,
        guess_phase, guess_offset]
    
    # create the function we want to fit
    def my_sin(x, freq, amplitude, phase, offset):
        return np.sin(x) * amplitude 
    
    # now do the fit
    fit = curve_fit(my_sin, t, data, p0=p0)
    #print(np.degrees(t))
    # we'll use this to plot our first estimate. This might already be good enough for you
    #data_first_guess = my_sin(t, *p0)
    #plt.ylim(-.05,.05)
    # recreate the fitted curve using the optimized parameters
    data_fit = my_sin(t, *fit[0])
      
    #return(data_first_guess,data_fit)
    #plt.ylim(-.1,.1)
    '''
    plt.plot(np.degrees(t),data,marker='.',color=cl,label='original')
    plt.plot(np.degrees(t),data_fit, 'ro',label='after fitting')
    #plt.plot(np.degrees(t),data_first_guess, 'k.',label='first guess')
    #print(min(data_fit),max(data_fit))
    plt.ylabel('Omega (rad/sec)',fontsize=16,fontweight=5)
    plt.xlabel('Theta (degrees)',fontsize=16,fontweight=5)
    #plt.ylim(-.1,.1)
    #plt.figtext(.4, .7, "B = "+str(abs(guess_amplitude)),fontsize=12,fontweight=15)
    #plt.figtext(.4, .7, "B = "+str(.019),fontsize=12,fontweight=15)
    plt.legend()
    plt.savefig(pth1+str(sgn)+'F_'+'w_'+str(round(max(data_fit),2))+'.jpg')
    plt.show()
    '''
    print('***************')
    print('Full:',min(data_fit),max(data_fit))
        #print('Half:',min(data_fit2),max(data_fit2))
    print('***************')
    


    
for ky in range(len(b)):
    for gy in range(len(d)):
        for hy in range(len(t)):
            for yy in range(len(p)):
                dfi=pth+b[ky]+d[gy]+t[hy]+p[yy]
                for ly in range(len(s)):
                    #df8=dfi+'Reor/'+s[ly]+'/Py/Tot_resultF.csv'
                    print(dfi+'Reor/'+s[ly]+'/Py/Tot_resultF.csv')
                    p1=dfi+'Reor/'+s[ly]+'/Py/'
                    df8=pd.read_csv(dfi+'Reor/'+s[ly]+'/Py/reor_unbin_'+lo+'.csv')
                    #ids1=[]
                    
                    thk=df8['Theta']
                    omk=df8['Omega']
                    stt,soo=bin_omega(omk,thk,30)
                    sfit(soo,stt,sgnz,.05,p1)
                    
                    
        

T=time.time()-st_t   
print('Time:',T)