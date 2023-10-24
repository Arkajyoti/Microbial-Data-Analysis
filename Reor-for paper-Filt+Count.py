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
d,p=['1/'],['Top/']#,'4/','6/']#,'Bot/']

b=['BR1/','BR2/','BR3/']
t=['TR1/','TR2/']
s=['S1/','S2/']

pth='C:/PhD/Hak_motility/24hrs/R2/Analysed_Reor/'

mea=[]
                    #print(df8)
                    

#df8=pd.read_csv(+b+d+t+p+'Reor/'+s+'/Py/Tot_resultF.csv')
#pth1='C:/PhD/Hak_motility/24hrs/R3/Analysed_Reor/'+b+d+t+p+'Reor/'+s+'/Py/'
#pth1='C:/PhD/Hak_motility/H3107/R4/Young/S1_f20_185/ImJ/'
uOm,dOm,uTh,dTh=[],[],[],[]
rTu,rOu,rTd,rOd=[],[],[],[]

###########################df 10 changes#############################
def omega_theta(xn2,yn2,tn2):
 dlx2,dly2,dty2,thtsf2,thtf2=[],[],[],[],[]
 #print(tn2)
 for ia2 in range(len(xn2)-1):
      dlx2.append(((xn2[ia2+1]-xn2[ia2])))#,ia2))
      dly2.append(((yn2[ia2+1]-yn2[ia2])))#,ia2))
      dty2.append(((tn2[ia2+1]-tn2[ia2]))*fps)
#  print(dlx2[k4],'0'*2000,dly2[k4],'#'*2000)

 
 #print(dty2)
 for ib2 in range(len(dlx2)):
      xvl2=dlx2[ib2]
      yvl2=dly2[ib2]
      
      if xvl2==0 or yvl2==0:
          print('Danger!! check',ib2)
      if xvl2>0 and yvl2<0:
            th2=np.pi+(np.arctan(xvl2/yvl2))
            thtf2.append((th2,ib2))
            if th2>np.pi or th2<-np.pi:
                print(xvl2,yvl2,th2)
      elif xvl2<0 and yvl2<0:
            th2=-(np.pi)+((np.arctan(xvl2/yvl2)))
            thtf2.append((th2,ib2))
            if th2>np.pi or th2<-np.pi:
                print(xvl2,yvl2,th2)
      elif xvl2>0 and yvl2>0:
            th2=(np.arctan(xvl2/yvl2))
            thtf2.append((th2,ib2))
            if th2>np.pi or th2<-np.pi:
                print(xvl2,yvl2,th2)
      elif xvl2<0 and yvl2>0:
            th2=(np.arctan(xvl2/yvl2))
            thtf2.append((th2,ib2))
            if th2>np.pi or th2<-np.pi:
                print(xvl2,yvl2,th2)
      else:
            print('WRONG!!!',xn2[ib2],yn2[ib2])
      
  #print(thtf)
 thtf2=sorted(thtf2,key=lambda x:x[1])
  #thtsf[k].append(thtf[k])
 thts2,nn=list(zip(*thtf2))
 thtsf2=thtsf2+(list(thts2))
  #print(thts2)
  #print(len(thts))
  #print(np.degrees(thts))
  #print(sdir[k4])
 #print(np.degrees(thtsf2))
 return(thtsf2,dlx2,dly2,dty2)     
 
########################################## 
def omega_dtheta(theta,dtm):
  thn,dtht,dtht2,dthtF,thnF=[],[],[],[],[]
  #print(dtm)
      
  for k8 in range(len(theta)-1):
          tht1=theta[k8]
          tht2=theta[k8+1]
          if 0<tht1<np.pi and 0<tht2<np.pi:
              dv= tht2-tht1
              dtht.append((dv,k8))
              thn.append((tht2,k8))
          elif -np.pi<tht1<0 and -np.pi<tht2<0:
              dv= tht2-tht1
              dtht.append((dv,k8))
              thn.append((tht2,k8))
          elif 0<tht1<np.pi and -np.pi<tht2<0:
              dv= ((2*np.pi)-(tht2+tht1))
              dtht.append((dv,k8))
              thn.append((tht2,k8))
          elif 0<tht1<-np.pi and 0<tht2<np.pi:
              dv= -((2*np.pi)-(tht2+tht1))
              dtht.append((dv,k8))
              thn.append((tht2,k8))
          
          
  #print(thn)     
  dtht=sorted(dtht,key=lambda x:x[1])
  deltht_s,nn=list(zip(*dtht))
  
  thn=sorted(thn,key=lambda x:x[1])
  thnf,_=list(zip(*thn))
  
  dtht2=dtht2+(list(deltht_s))
  thnF=thnF+list(thnf)   
  dtym=dtm[1:]
  #dtym=list(map(lambda x: x/16, dtym))
  #print('time:',dtym,len(dtht2),len(dtym),len(thnF))
  omega1=list(map(lambda x,y: x/y, dtht2,dtym))
  #print(omega1,'0000000000000000000000')
 
  dthtF=dthtF+(omega1)

            
  
  return(thnF,dthtF)
 
##############################################
def bin_omega(omg,tht,syz):
        #print('hhhhooo', len(omg),'pppooo',len(tht))
        #tht=tht[1:]
        th_D=np.degrees(tht)
        sdv=[]
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
                s_omg=np.std(bln2)
                sdv.append(s_omg)
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
        return(sort_tht,sort_omg,sdv)
 

########################################################
def sfit(data,thtt,sgn,guess_amplitude,sdd) :
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
    data_first_guess = my_sin(t, *p0)
    #plt.ylim(-.05,.05)
    # recreate the fitted curve using the optimized parameters
    data_fit = my_sin(t, *fit[0])
      
    #return(data_first_guess,data_fit)
    #plt.ylim(-.1,.1)
    
    plt.errorbar(np.degrees(t),data,fmt='.',color=cl,label='original')
    plt.plot(np.degrees(t),data_fit, 'ro',label='after fitting')
    plt.plot(np.degrees(t),data_first_guess, 'k.',label='first guess')
    #print(min(data_fit),max(data_fit))
    plt.ylabel('Omega (rad/sec)',fontsize=16,fontweight=5)
    plt.xlabel('Theta (degrees)',fontsize=16,fontweight=5)
    #plt.ylim(-.1,.1)
    #plt.figtext(.4, .7, "B = "+str(abs(guess_amplitude)),fontsize=12,fontweight=15)
    #plt.figtext(.4, .7, "B = "+str(.019),fontsize=12,fontweight=15)
    plt.legend()
    #plt.savefig(pth1+str(sgn)+'F_'+'w_'+str(round(max(data_fit),2))+'.jpg')
    plt.show()
    print('***************')
    print('Full:',min(data_fit),max(data_fit))
        #print('Half:',min(data_fit2),max(data_fit2))
    print('***************')
    
    #dff=pd.DataFrame(zip(np.degrees(t),data),columns=["Theta","Omega"])
    #dff.to_csv(pth1+'reor_binF.csv')
    
############################################################################## 
##############################################################################
cu,cd=[],[] 
cl=0
ck=0 
kh=[]
import time
st_t=time.time()

for ky in range(len(b)):
    for gy in range(len(d)):
        for hy in range(len(t)):
            for yy in range(len(p)):
                dfi=pth+b[ky]+d[gy]+t[hy]+p[yy]
                for ly in range(len(s)):
                    #df8=dfi+'Reor/'+s[ly]+'/Py/Tot_resultF.csv'
                    print(dfi+'Reor/'+s[ly]+'/Py/Tot_resultF.csv')
                    df8=pd.read_csv(dfi+'Reor/'+s[ly]+'/Py/Tot_resultF.csv')
                    #ids1=[]

                    name=df8.particle.unique()
                    names=name.tolist()
                    #names=[919,795,908,801,893,775,884,770,882,763,883,764,831,824,807,813]
                    dictn={elem : pd.DataFrame for elem in name} #(blank dict of dfs??)
                    #print(elem)
                    for key in dictn.keys():
                        dictn[key] = df8[:][df8.particle == key]
                    #print(len(names))
                    for i in names[:]:
                        file=dictn[i]
                        
                        if len(file)>45:
                            #print(file)
                            
                            xv=file['x']
                            yv=(file['y'])*-1
                            tv=list(file['frame'])
                            #print(tv,'KKKKKKKKKKKKKKKK')
                            dxv=(xv.iloc[-1]-xv.iloc[0])
                            dyv=(yv.iloc[-1]-yv.iloc[0])
                            scl=(np.sqrt(dxv**2+dyv**2))*fps*sclz
                            kh.append(scl)
                            #print(scl,'sclllllll')
                            if scl>3 and scl<17:
                                #print('***********')
                                dyc=np.mean(np.gradient(yv))
                                tck2,u2=interpolate.splprep([xv, yv], k=2,s=1*10**6,per=0,u=np.linspace(min(xv),max(xv),len(xv)))
                                x2,y2=interpolate.splev(np.linspace(min(xv),max(xv),num=1*len(xv)), tck2)
                                if dyc>0:
                                    lb,c='Up','g'
                                    cl=cl+1
                                    #print(cl)
                                #swim_dir[k].append(lb)
                                elif dyc<0:
                                    lb,c='Dwn','b'
                                    ck=ck+1
                                    #print(ck)
                    print(cl)
                    mea.append(cl)
                    print(ck)
                    cl,ck=0,0
                    print('###################################################################')
                               
                                



'''
dfU=pd.DataFrame(zip(np.degrees(uTh),uOm),columns=["Theta","Omega"])
dfU.to_csv(pth1+'reor_unbin_UF.csv')
dfD=pd.DataFrame(zip(np.degrees(dTh),dOm),columns=["Theta","Omega"])
dfD.to_csv(pth1+'reor_unbin_DF.csv')

sTu,sOu,sDu=bin_omega(uOm,uTh,30)
sfit(sOu,sTu,'Up',.05,sDu)

sTd,sOd,sDd=bin_omega(dOm,dTh,30)
sfit(sOd,sTd,'Dwn',.06,sDd)

T=time.time()-st_t   
print('Time taken:',T)
print('***************************************************************')
print('Up_cnt:',len(cu))
print('Dn_cnt:',len(cd))
'''
st_s=time.time()
print('time:',st_s-st_t)
print(np.mean(mea),np.std(mea))
print(mea)