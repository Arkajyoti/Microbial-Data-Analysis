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
'''
T11=pd.read_csv('C:/PhD/Hak_motility/24hrs/R2/Analysed_Reor/Combined/11h/Top/Us/11h_Top_Us_Allreplicates.csv')
#print(T11)
T11f=T11['Time'][:12]
B11=pd.read_csv('C:/PhD/Hak_motility/24hrs/R2/Analysed_Reor/Combined/11h/Bot/Us/11h_Top_Us_Allreplicates.csv')
#print(T11)
B11f=B11['Time'][:12]
#print(T11f)
T00=pd.read_csv('file:///C:/PhD/Hak_motility/24hrs/R2/Analysed_Reor/Combined/00h/Top/Ds/Allreplicates.csv')
T00f=T00['Time'][:12]

B00=pd.read_csv('file:///C:/PhD/Hak_motility/24hrs/R2/Analysed_Reor/Combined/00h/Bot/Us/Allreplicatess.csv')
B00f=B00['Time'][:12]

T1m,T1s=np.mean(T11f),np.std(T11f)
T0m,T0s=np.mean(T00f),np.std(T00f)
B1m,B1s=np.mean(B11f),np.std(B11f)
B0m,B0s=np.mean(B00f),np.std(B00f)
'''
plt.bar('11h',12.38,yerr=5.4,facecolor='g',label='Up_stable')
plt.bar('00h',10.5,yerr=4.49,facecolor='b',label='Down_stable')
plt.ylabel('Timescale (sec)',fontsize=16)
plt.xlabel('Timepoint (hours)',fontsize=16)
plt.ylim(0,20)
#plt.tick_params(axis='both', which='minor', labelsize=120)
plt.legend()
plt.show()
plt.bar('11h',6.22,yerr=2.5,facecolor='g',label='Up_stable')
plt.bar('00h',4.03,yerr=2.03,facecolor='g',label='Up_stable')
plt.ylabel('Timescale (sec)',fontsize=16)
plt.xlabel('Timepoint (hours)',fontsize=16)
plt.ylim(0,12.5)
#plt.tick_params(axis='both', which='minor', labelsize=120)
plt.legend()
plt.show()

'''
x=['A','B','C']
y1=[.811,.858,.6]
y2=[.893,1.09,2.97]
y3=[1.94,2.94,3.38]

plt.plot(x,y1,'o',label='Round 1')
plt.plot(x,y2,'o',label='Round 2')
plt.plot(x,y3,'o',label='Round 3')
plt.ylim(0,5)
plt.ylabel('DNA conc. (ng/ul)')
plt.xlabel('Replicates')
plt.legend()
'''
plt.plot([1],'ro',label='BR1TR1')
plt.plot([2],'bo',label='BR1TR2')
plt.plot([3],'k',label='Average')
plt.legend()
