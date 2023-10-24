# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 01:46:32 2020

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
import statistics as st
import math
from scipy.stats import norm
import matplotlib.mlab as mlab
import trackpy as tp
from scipy import interpolate

#p1='C:/PhD/Hak_motility/Anupams data/Test_Traj_code/AS1/Analysed/Control/ControlTraj_res_filt_100F.csv'
#path2='C:/PhD/Hak_motility/24hrs/R2/Analysed_traj_2/BR2/4/TR1/Bot/Traj/Traj_res_filt_100F.csv'
#p3='C:/PhD/Hak_motility/Anupams data/Test_Traj_code/AS1/Analysed/Control/imj Traj.csv'
#p4='C:/Users/arkajyoti.ghoshal/Desktop/Demo traj/AS1/Analysed/Split/SplitTraj_res_filt_100F.csv'
#p5='C:/PhD/Hak_motility/Anupams data/Test_Traj_code/AS1/Analysed/Control2/C2.csv'
#sv1='C:/Users/arkajyoti.ghoshal/Desktop/Demo traj/AS1/Analysed/Split/'
p6='file:///C:/PhD/Hak_motility/H3107/R4/Young/BR1/ImJ/TR1/S1/Results.csv'
#sv6='C:/PhD/Hak_motility/Anupams data/Reorientation/R2/Analysed/4//'
#p7='C:/PhD/Hak_motility/FD data demo/Analysed//FD_demo_filt_100.csv'
#sv7='C:/PhD/Hak_motility/FD data demo/Analysed/'
## for p6, scale= 1024 p= 4k um=== 256. else for other paths, 235
#################def1#######################
#br=['BR1','BR2']
###No BR as diff BRs can have diff h1,h2####
sets=[1]#,2,3,4,5,6]
tr=['New']
pos=['Top','Bot']
#sets=[2]
#tr=['TR2']
#pos=['Bot']
fpz=16
scle=1000/600
###actual scale= 1000/402
plt.rc('axes', labelsize=20)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=16)    # fontsize of the tick labels
plt.rc('ytick', labelsize=16)    # fontsize of the tick labels
plt.rc('legend', fontsize=15)
fx,fy=12,8


#################def1#######################

        

       
def velp (pt,fps,scale):
            #pt=path1
            dft=pd.read_csv(pt)
            #dft=dft.iloc[:]
            #print(dft)
            name=dft.particle.unique()
            names=name.tolist()
            #names=names[:500]
            #names.remove(66)
            #print(names) #.index(1))
            
            dictn={elem : pd.DataFrame for elem in names} #(blank dict of dfs??)
#print(elem)
            for key in dictn.keys():
                dictn[key] = dft[:][dft.particle == key]
            #print(dictn)
            mean_vel,del_x_avg,del_y_avg,dy_abs,dx_abs=[],[],[],[],[]
 

#xy=[4,6660]
            for i in names:
                #xci,yci=[],[]
             
                file=dictn[i]
              
                v,delx,dely=[],[],[]
                dy_abs1,dx_abs1=[],[]
                #print(file.iloc[0:2,0:3])
                for j in range (0,(len(file)-1)):
    #print (rd.iloc[i,1])
                    #dt3=t3[j+1]-t3[j]
                    dt3=(file.iloc[j+1,1]-file.iloc[j,1])
                    dx3=(file.iloc[j+1,2]-file.iloc[j,2])*scle*(fpz)*(1/dt3)
                    dy3= (file.iloc[j+1,3]-file.iloc[j,3])*scle*(fpz)*(1/dt3)
                    #dx3=(x2[j+1]-x2[j])*scle*(fpz)*(1/dt3)
                    #dy3= (y2[j+1]-y2[j])*scle*(fpz)*(1/dt3)
                    #print(dt3)
                    #print(y)
                    velocity= ((dx3**2)+(dy3**2))**.5
                    v.append(velocity)
                    #print(velocity,dt3)
                    delx.append(dx3)
                    dy_abs1.append(abs(dy3))
                    dely.append(dy3)
                    dx_abs1.append(abs(dx3))
                    s=st.mean(v)
                    x_av=st.mean(delx)
                    y_av=st.mean(dely)
                    y_a_ab=np.mean(dy_abs1)
                    x_a_ab=np.mean(dx_abs1)
                #ids.append(i)
    
                mean_vel.append(s)
                del_x_avg.append(x_av)
                del_y_avg.append(y_av)
                dy_abs.append(y_a_ab)
                dx_abs.append(x_a_ab)
            final_dt={'particle':names, 'Avg velocity': mean_vel, 'Avg_u': del_x_avg, 'Avg_v': del_y_avg,'Ab v':dy_abs, 'Ab u':dx_abs} #, 'Avg_y_-1': y_abs_avg, 'Avg_x_abs': xab_av, 'Avg_y_abs': yab_av }
            final_dft=pd.DataFrame(final_dt)
            #print()
            print(final_dft)
            return(final_dft)
            #final_dft.to_csv(sv1+str(sr)+'//'+'vel_p.csv',index=False)
   

            

            #final_dft.to_csv(sv1+'/'+'vel_p.csv',index=False)
            #print('done',sv1+'/'+'vel_p.csv')


bookD=velp(p6,fpz,scle)
#bookD.to_csv(sv6+'vel_pF.csv')   

###############################################################

       
######################################################################

dff=bookD
#dff=pd.read_csv(sv7+'vel_pF.csv')
#dff=dff.loc[abs(dff['Avg_v'])<250]
yy=dff['Avg_v']
xx=dff['Avg_u']
yab=dff['Ab v']
xab=dff['Ab u']
yyu,yyd=[],[]
xxu,xxd=[],[]

for k in range(len(yy)):
    if yy[k]>0:
        yo=(yy[k])*-1
        yyd.append(yo)
        xxd.append(xx[k])
    
    if yy[k]<0:
        yo=(yy[k])*-1
        yyu.append(yo)
        xxu.append(xx[k])
#plt.gcf().set_size_inches(12,8)   
print(len(yyu),len(yyd))

plt.hist(yyu,edgecolor='k',bins=20,facecolor='orange',label='Upswimmers ['+str(len(yyu))+']')
plt.hist(yyd,edgecolor='k',bins=15,facecolor='red',label='Downswimmers ['+str(len(yyd))+']')
plt.xlabel('Velocity_y_component ('+'\u03BC'+'m/s)',labelpad=15)
plt.legend()
plt.show()
        
       
        
plt.hist((yyu+yyd),edgecolor='k',bins=20,facecolor='red',label='Combined')
plt.ylabel('Frequency',labelpad=15)
plt.xlabel('Velocity_y_Component('+'\u03BC'+'m/s)',labelpad=15)
plt.legend()
plt.show()
plt.hist(dff['Avg_u'],edgecolor='k',bins=20,facecolor='y',label='Combined')
plt.ylabel('Frequency',labelpad=15)
plt.xlabel('Velocity_x_Component('+'\u03BC'+'m/s)',labelpad=15)
plt.legend()
plt.show()
plt.hist(dff['Avg velocity'],edgecolor='k',bins=20,facecolor='orange',label='Combined')
plt.ylabel('Frequency',labelpad=15)
plt.xlabel('Absolute Speed ('+'\u03BC'+'m/s)',labelpad=15)
plt.legend()
plt.show()

plt.hist(dff['Ab u'],edgecolor='k',bins=20,facecolor='cyan',label='Combined')
plt.ylabel('Frequency',labelpad=15)
plt.xlabel('Absolute Speed x_Component('+'\u03BC'+'m/s)',labelpad=15)
plt.legend()
plt.show()
plt.hist(dff['Ab v'],edgecolor='k',bins=20,facecolor='magenta',label='Combined')
plt.ylabel('Frequency',labelpad=15)
plt.xlabel('Absolute Speed y_Component('+'\u03BC'+'m/s)',labelpad=15)
plt.legend()
plt.show()
print(np.mean(dff['Avg velocity']))



#fig,ax=plt.subplots(figsize=(8,6))
        #fig2,ax2=plt.subplots(figsize=(8,6))
'''
'''
b,c,p=ax.hist(vF,bins=np.arange(0,max(vF)+15,15),edgecolor='black',label='Absolute_Speed')
ax.set_xlabel('Speed ('+str(u'\u03bc')+str('m/s')+')',labelpad=15)
ax.set_ylabel('Frequency',labelpad=15)
ax.legend()
#fig.savefig(sv1+'/Abs_spd.png')
        #print(b,c,sum(b))

########################################################################
fig2,ax2=plt.subplots(figsize=(8,6))


ax2.hist(xF,bins=np.arange(-200,200,15),color='cyan',edgecolor='black',alpha=.8,label='x_Component')
ax2.hist(yF,bins=np.arange(-200,200,15),color='gray',edgecolor='black',alpha=1,label='y_Component')
ax2.set_xlabel('Velocity Component ('+str(u'\u03bc')+str('m/s')+')',labelpad=15)
ax2.set_ylabel('Frequency',labelpad=15)
ax2.legend()
#fig2.savefig(sv1+'/Components.png')


####################################################################################
uy,ux,uv,uyp=[],[],[],[]
dy,dx,dv,dyn=[],[],[],[]
for ii in range(len(yF)):
            if dfF.iloc[ii,3]>0: #(dwn_swm)
                dy.append((dfF.iloc[ii,3]))
                dx.append(dfF.iloc[ii,2])
                dv.append((dfF.iloc[ii,1])*-1)
                dyn.append((dfF.iloc[ii,3])*-1)
            if dfF.iloc[ii,3]<0:
                uy.append(dfF.iloc[ii,3])
                ux.append(dfF.iloc[ii,2])
                uv.append(dfF.iloc[ii,1])
                uyp.append((dfF.iloc[ii,3])*-1)
        
        
fign,axn=plt.subplots(figsize=(fx,fy))
        #b3,c3=np.histogram
axn.hist(uv,bins=np.arange(-200,200,15),color='g',edgecolor='black',alpha=.8,label='Speed_Up (N='+str(len(uv))+')')
axn.hist(dv,bins=np.arange(-200,120,15),color='blue',edgecolor='black',alpha=.6,label='Speed_Down (N='+str(len(dv))+')')
axn.set_xlabel('Speed ('+str(u'\u03bc')+str('m/s')+')',labelpad=15)
axn.set_ylabel('Frequency',labelpad=15)
axn.legend()
#fign.savefig(sv1+'/Up_v_Dwn_Spd.png')
        
        
       
figt,axt=plt.subplots(figsize=(fx,fy))

axt.hist(uyp,bins=np.arange(-200,200,15),color='green',edgecolor='black',alpha=.8,label='y_component (N='+str(len(uyp))+')')
axt.hist(ux,bins=np.arange(-200,200,15),color='y',edgecolor='black',alpha=.8,label='x_component (N='+str(len(ux))+')')
axt.set_xlabel(str(u'\u03bc')+str('m/s'),labelpad=15)
axt.set_ylabel('Frequency',labelpad=15)
axt.legend()
#figt.savefig(sv1+'/Components_up.png')

figk,axk=plt.subplots(figsize=(fx,fy))

axk.hist(dyn,bins=np.arange(-200,200,15),color='blue',edgecolor='black',alpha=.8,label='y_component (N='+str(len(dyn))+')')
axk.hist(dx,bins=np.arange(-200,200,15),color='r',edgecolor='black',alpha=.4,label='x_component (N='+str(len(dx))+')')
axk.set_xlabel(str(u'\u03bc')+str('m/s'),labelpad=15)
axk.set_ylabel('Frequency',labelpad=15)
axk.legend()
#figk.savefig(sv1+'/Components_down.png')





  

#print(uyp[0:10],uy[0:10])
###############################################################################

'''
figpk = plt.figure(figsize=(fx+2,fy+2))

axp  = figpk.add_subplot(polar=True)

axp.set_theta_zero_location("E")
axp.set_theta_direction(1) #cw 1 or ccw -1


bin_size = 15
inv_tan_corr,inv_tan_corr2=[],[]

tan1=list(map(lambda p,q: p/q,yyu,xxu))
inv_tan1=list(map(lambda z:(math.degrees(math.atan(z))),tan1))
#print((inv_tan1))
##########gives angle b/w vector and x##############
for ty1 in inv_tan1:
    if 0<=ty1<=90:
#ty1=180-ty1
#ty2=ty2+270
        inv_tan_corr.append(ty1)
    if -90<=ty1<0:
        ty1=180+ty1
#ty2=270+ty2
        inv_tan_corr.append(ty1)
#print(inv_tan1)
a1_norm=[]
a1 , b1=np.histogram(inv_tan_corr, bins=np.arange(0, 375, bin_size))
c1=sum(a1)

for ok in a1:
    ad1=ok/c1
    a1_norm.append(ad1)
#print('0'*200,a1_norm,c1,a1,b1)
centers = np.deg2rad(np.ediff1d(b1)//2 + b1[:-1])
axp.bar(centers, a1_norm, width=np.deg2rad(bin_size), bottom=0.0, color='green', edgecolor='k',label='Speed_Up')
#print(b1,'0'*200,max(inv_tan1))    

#################bot swim#########################

tan12=list(map(lambda p,q: p/q,yyd,xxd))
inv_tan12=list(map(lambda z:(math.degrees(math.atan(z))),tan12))
#print((inv_tan12))
##########gives angle b/w vector and x##############

for ty2 in inv_tan12:
    if 0<=ty2<=90:
#ty2=90-ty2
        ty2=180+ty2
        inv_tan_corr2.append(ty2)
    if -90<=ty2<0:
#ty2=-90-ty2
        ty2=360+ty2
        inv_tan_corr2.append(ty2)
inv_tan121=inv_tan_corr2
#print(len(inv_tan121))
#print(inv_tan121)

a2_norm=[]
a12 , b12=np.histogram(inv_tan_corr2, bins=np.arange(0, 375, bin_size))
c2=sum(a12)
print(c1,c2)
for ok1 in a12:
    ad2=ok1/c2
    a2_norm.append(ad2)
#print('0'*200,a1_norm,c1,a1,b1)
centers2 = np.deg2rad(np.ediff1d(b12)//2 + b12[:-1])

axp.bar(centers2, a2_norm, width=np.deg2rad(bin_size), bottom=0.0, color='yellow', edgecolor='k',label='Speed_down')
axp.legend(fontsize=12)
#plt.savefig(sv1+'/rose.png')

       #print(len(inv_tan1),len(inv_tan12),'0'*200)

##############################################################################
#HeatMAp##

'''
'''
fig3,ax3=plt.subplots(figsize=(15,15))
ax3.set_ylim(-100,100)
ax3.set_xlim(-100,100)
from matplotlib.lines import Line2D
custom_lines = [Line2D([0], [0], color='green', lw=4),
                Line2D([0], [0], color='red', lw=4),
                ]
ax3.legend(custom_lines, ['Up_swim', 'Down_swim']) #,'Horiz_swim'])
ax3.set_ylabel('Vertical speed('+str(u'\u03bc')+str('m/s)'),labelpad=15)
#ax.set_legend()
ax3.set_xlabel('Horizontal speed('+str(u'\u03bc')+str('m/s)'),labelpad=15)
ax3.set_xticks(np.arange(-100, 101, step=50))
ax3.set_yticks(np.arange(-100, 101, step=50))
#ax.set_legend()
cm1 = plt.cm.get_cmap('Greens')
cm2 = plt.cm.get_cmap('Reds')

vmn,vmx=min(uv),max(uv)
vmn1,vmx1=min(dv),max(dv)
#print(vmn,vmn1,vmx,vmx1)

pn=ax3.scatter(ux,uy,c=uv,cmap=cm1,edgecolor='green',vmin=0)
pn1=ax3.scatter(dx,dy,c=dv,cmap=cm2,edgecolor='red',vmin=0)


#cbaxes1 = fig.add_axes([0.8, 0.1, 0.03, 0.8]) 
cb1 = plt.colorbar(pn,pad=.05,ticks=np.arange(0, 120, step=10)) #cax = cbaxes1
cb2 = plt.colorbar(pn1,pad=.06,ticks=np.arange(0, 120, step=10))

cb1.ax.get_yaxis().labelpad = 25
cb1.ax.set_ylabel('Absolute speed', rotation=270)


#######################heatmap###############
bins=np.arange(-140,200,step=10)
#print(heatmap)
YCa=uy+dy


XCa=ux+dx
print(len(XCa),len(YCa))
fign,axn=plt.subplots(figsize=(16,10))
axn.set_ylabel('Vertical speed('+str(u'\u03bc')+str('m/s)'),labelpad=15)
#ax.set_legend()
axn.set_xlabel('Horizontal speed('+str(u'\u03bc')+str('m/s)'),labelpad=15)
counts, xedges, yedges, hm=axn.hist2d(ux,uy,bins,cmap=plt.cm.jet,weights=np.ones(len(uy)) / len(uy))


cbar = plt.colorbar(hm)
cbar.ax.get_yaxis().labelpad = 25
cbar.ax.set_ylabel('Relative Frequency', rotation=270)



fign1,axn1=plt.subplots(figsize=(16,10))
axn1.set_ylabel('Vertical speed('+str(u'\u03bc')+str('m/s)'),labelpad=15)
#ax.set_legend()
axn1.set_xlabel('Horizontal speed('+str(u'\u03bc')+str('m/s)'),labelpad=15)
counts1, xedges1, yedges1, hm1=axn1.hist2d(dx,dy,bins,cmap=plt.cm.jet,weights=np.ones(len(dy)) / len(dy))

cbar1 = plt.colorbar(hm1)
cbar1.ax.get_yaxis().labelpad = 25
cbar1.ax.set_ylabel('Relative Frequency', rotation=270)

#fign1.savefig(save2+'/'+str(namez)+'bot_cloud.png')

fign2,axn2=plt.subplots(figsize=(16,10))
axn2.set_ylabel('Vertical speed('+str(u'\u03bc')+str('m/s)'),labelpad=15)
#ax.set_legend()
axn2.set_xlabel('Horizontal speed('+str(u'\u03bc')+str('m/s)'),labelpad=15)
counts2, xedges2, yedges2, hm2=axn2.hist2d(XCa,YCa,bins,cmap=plt.cm.jet,weights=np.ones(len(YCa)) / len(YCa))

cbar1 = plt.colorbar(hm2)
cbar1.ax.get_yaxis().labelpad = 25
cbar1.ax.set_ylabel('Relative Frequency', rotation=270)

'''
################  with interpolation ##########
'''
#if len(file['frame'])>80:
                #plt.plot(file['x'],file['y'],'ro')
                
                #tck2,u2=interpolate.splprep([file['x'], file['y']], k=2,s=1*10**6,per=0,u=np.linspace(min(file['x']),max(file['x']),len(file['x'])))
                #x2,y2=interpolate.splev(np.linspace(min(file['x']),max(file['x']),num=1*len(file['x'])), tck2)
                #file['x']=(list(x2))
                #file['y']=(list(y2))
                #plt.plot(x2,y2,'o')
                
                #plt.savefig(sv6+'/'+str(names[i])+'.jpg')
                #plt.show()
                #print(file.iloc[:,:])
                #xc,yc,t3=file['x'],file['y'],list(file['frame'])
                #n=set(file['particle'])
                #tck2,u2=interpolate.splprep([xc, yc], k=3,s=1*10**6,per=0,u=np.linspace(min(xc),max(xc),len(xc)))
                #x2,y2=interpolate.splev(np.linspace(min(xc),max(xc),num=1*len(xc)), tck2)
                #x2=list(x2)
                #y2=list(y2)
                #print(y2)
                #plt.plot(xc,yc)
                #plt.plot(x2,y2)
                #plt.show()
#bookD=velp(p5,sv1,fpz,scle)
'''