import os
#import trackpy as tp
import numpy as np
import cv2
import matplotlib as mp
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from matplotlib.patches import Circle
from skimage import measure
from skimage.segmentation import clear_border
import pandas as pd
import matplotlib.cm as cm
#plt.rcParams['text.usetex'] = True
import math
#### orig culture: 24_6_21#####
#####expt starts: 6_6_21
### seed age: ~12 days/ 288 hrs ############

t=[0,24,48,72,96,192,264,336,384,432,552,672,720]
x=np.array([592,608,510,573])/3.5
print(np.mean(x),np.std(x))
y1=np.array([0,10.86,22.14,39.85,63.42,115,204.43,195,204.29,225.9,222.79,163.1,162])/100
s1=np.array([0,1.74,2.74,4.43,2.20,6.5,1.29,4.64,10.3,15.85,28.86,5.79,10.62])/100

y2=np.array([0,5.428571429,10.71428571,21.35714286,40.21428571,111.8571429,234.2857143,208.5714286,221.2142857,232.8571429,229.7142857,170.5,152.4285714])/100

#### note: 6th element removed wrt original data #####


#plt.errorbar(t,y1,yerr=s1,fmt='o-')
#plt.ylim(0,2.5,.005)
#plt.show()
#print(len(t),len(y1),len(s1))
#print(t,np.array(y1)*3.5)
#y12=[0,38,77.5,139.5,222,402.5,431,720,695,715,790.6666667,779.75,570.75,567.5]
#t2=[0,24,48,72,96,192,216,264,336,384,432,552,672,720]
#plt.errorbar(t2,y12,fmt='o-')
#######___fit_link: https://ipython-books.github.io/93-fitting-a-function-to-data-with-nonlinear-least-squares/###############
def logf(x,A,x0,k,off):
        return A / (1 + np.exp(-k*(x-x0)))+off
A=5.69
x0=300
k=0
off=0

popt, pcov = curve_fit(logf, t, y1, p0=[A,x0,k,off])
y1f=(logf(t, *popt))[:-1]
y2f=[0.05974402, 0.12606738, 0.22143639, 0.3528779,  0.52383031, 1.39187301,
     1.78979314+.26, 1.93059622+.26, 1.96247443+.26, 1.97570258+.26, 1.9838742+.26 ]
#print(y1f)
'''
plt.gcf().set_size_inches(13,13)
plt.ylim(0,3)
#plt.gca().set_aspect('equal', adjustable='box')
print('hhh',y1)
plt.errorbar(t,y1,yerr=s1,fmt='o--',label='Original',color='purple')
plt.plot(t[:-2], y1f, 'r^-',label='Fitted function')
plt.plot(t[:-2], y2f, 'g+-',label='Logistic_Fitted function')
plt.ylabel('Cell Count',fontsize=15,fontweight=15)
plt.xlabel('Time (in hours)',fontsize=15,fontweight=15)
plt.legend()
plt.show()
#print(y1f)

popt2, pcov2 = curve_fit(logf, t, y2, p0=[A,x0,k,off])
y2f=(logf(t, *popt))[:-2]
#print(len(t),len(y1),len(y2))
plt.gcf().set_size_inches(13,13)
plt.ylim(0,3)
plt.plot(t,y2,'k^-',label='Original')
plt.plot(t[:-2],y2f, 'c-o',label='Fitted function')
plt.legend()
plt.show()


print(y1,'hhhh')
'''

########## for paper #####################

plt.rcParams["font.family"] = "Times New Roman"
#plt.rcParams["font.family"] = "Calibri"
#### modified with seed density ##############

plt.gcf().set_size_inches(5,11)
plt.ylim(0,3)
plt.xlim(-10,720)
plt.xticks(np.arange(0,800,100))
#plt.gca().set_aspect('equal', adjustable='box')
print('hhh',y1)
y1[0]=0.0567
print(y1)
plt.errorbar(t[:-1],y1[:-1],fmt='o-',label='Original',color='purple')
plt.fill_between(t[:-1],y1[:-1]+s1[:-1],y1[:-1]-s1[:-1],facecolor='purple',alpha=.35)
#plt.plot(t[:-1], y1f[:], 'r^--',label='Exponential function')
#plt.plot(t[:-2], y2f, 'g+-',label='Logistic_Fitted function')
plt.ylabel('Cell Concentration (C, ml$^-$ )',fontsize=15,fontweight=15)
plt.xlabel('Time (in hours)',fontsize=15,fontweight=15)
#plt.xscale('log')
#plt.legend(prop={'size':15,'weight':0})
plt.show()

print(y1[:-1][:5])
######################### D/N cycle plot ###############
#plt.plot([0,4,4,18,18,24],[0,0,535,535,0,0])
plt.plot([0,4],[0,0],color='grey',linewidth=5)
plt.plot([4,4,18],[0,535,535],color='gold',label='Day',linewidth=5)
plt.plot([18,18,24],[535,0,0],color='grey',label='Night',linewidth=5)
plt.plot([11,15],[0,0],'|-',color='darkgreen',markersize=25,label='Experiment window',linewidth=2.5)
plt.gcf().set_size_inches(3,3)
#plt.gcf().set_size_inches(17,7)
plt.xticks([0,4,11,15,18,24],fontsize=14)
plt.yticks([0,0,535,535,0,0],fontsize=14)
#plt.legend(loc='upper left',prop={'family':'Times New Roman', 'size':16})
#plt.ylabel('Light intensity,'+' '+'$\lambda$'+''+'(),fontsize=20)
plt.ylabel('Light power,'+' '+'$\it{L}$'+' '+'(mW)',fontsize=18)
#plt.ylabel(r'\textbf{L}',fontsize=16)
plt.xlabel('Time,'+' '+'$\it{t}$'+' '+'(hours)',fontsize=18)
plt.yticks([0,535],['0','1.35'],fontsize=14)
plt.show()
##################################################################
#############   zoom to 0 to 200 #############
plt.gcf().set_size_inches(3,2)
plt.ylim(0,1.5)
#plt.xlim(-10,720)
#plt.xticks(np.arange(0,800,100))
#plt.gca().set_aspect('equal', adjustable='box')
print('hhh',y1)
y1[0]=0.0567
print(y1)
plt.errorbar(t[:6],y1[:6],fmt='o-',label='Original',color='purple')
#plt.fill_between(t[:-1],y1[:-1]+s1[:-1],y1[:-1]-s1[:-1],facecolor='purple',alpha=.35)
#plt.plot(t[:-1], y1f[:], 'r^--',label='Exponential function')
#plt.plot(t[:-2], y2f, 'g+-',label='Logistic_Fitted function')
plt.ylabel('Cell Concentration (C, ml$^-$ )',fontsize=15,fontweight=15)
plt.xlabel('Time (in hours)',fontsize=15,fontweight=15)
#plt.legend(prop={'size':15,'weight':0})
plt.show()

########################################################
#################   log scale ############################

print(y1)
y1=list(map(lambda x: x*10**5,y1))
print(y1)
plt.plot(t[:4],y1[:4],'k-',label='Fitted')
plt.errorbar(t[:-1],y1[:-1],fmt='o-',label='Original',color='purple')
plt.fill_between(t[:-1],y1[:-1]+s1[:-1],y1[:-1]-s1[:-1],facecolor='purple',alpha=.35)

#plt.plot(t[:-1], y1f[:], 'r^--',label='Exponential function')
#plt.plot(t[:-2], y2f, 'g+-',label='Logistic_Fitted function')
plt.ylabel('Cell Concentration (C, ml$^-$ )',fontsize=15,fontweight=15)
plt.xlabel('Time (in hours)',fontsize=15,fontweight=15)
plt.yscale('log')
plt.gcf().set_size_inches(5,7)
#plt.ylim(0,3*10**5)
plt.legend(prop={'size':15,'weight':0})
plt.show()

##########  doubling time ################

#### calc growth rate : ln(Cf/Ci)=r(tf-ti)
#y1=y1[:4]
na,nb=0,4
cff=y1[na+1:nb]
cif=y1[na:nb-1]
tff=t[na+1:nb]
tif=t[na:nb-1]

lc=np.log(np.array(cff)/np.array(cif))
tc=(np.array(tff)-np.array(tif))
#print(tc)
grt=lc/tc
#print(grt)
mgrt,sgrt=np.mean(grt),np.std(grt)

print('mean g rate',mgrt,'+-',sgrt)

### doub time = ln2/grt
d2tym=np.log(2)/(grt)

print('mean double time',np.mean(d2tym),'+-',np.std(d2tym))

################### ratio of cells ###############


print('ratio with 96h', np.array(y1)[4]/np.array(y1)[0],np.array(y1)[4]/np.array(y1)[1],np.array(y1)[4]/np.array(y1)[2],np.array(y1)[4]/np.array(y1)[3],np.array(y1)[4]/np.array(y1)[4],)    