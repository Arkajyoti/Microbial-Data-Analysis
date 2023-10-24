# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 11:55:34 2020

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

pth1='C:/PhD/Hak_motility/24hrs/R2/AnalysedF_Full/'


cellc=[]
spdl=[]
##########################4 poz changes ###################
def mot_plt(pth,parm,x0,xf,n,lab,nem):
    tym=['11h','15h','20h','00h','04h','08h']
    colz=['r','orange','g','k','cyan','indigo']
    bins=np.arange(x0,xf,n)
    cc=len(bins)
    binsf=np.arange((x0+(n/2)),(xf-(n/2)),n)
    allM,allS=[],[]
    bine0=list(np.arange(x0+n,xf,n))
    bines=list(map(lambda z: str(z),bine0))
    br=['BR1/','BR2/','BR3/']
###No BR as diff BRs can have diff h1,h2####
    sets=[1]#,2,3,4,5,6]
    tr=['TR1/','TR2/']
    pos=['Top/']#,'Bot/']

    
    
    #cellc,fnf=[],[]
    #l=((np.arange(20,0,-1).tolist()))
    #print(l)
    for ps in range(len(pos)):    
        for st in range(len(sets)):
            matP,dvP=[],[]
            #matC=[]
            
            
            for b in range(len(br)):
                #if br[b]=='BR1/':
                 #   k='Full'
                #else:
                 #   k='45'
                for rt in range(len(tr)):
                    
                    path=pth+str(br[b])+str(sets[st])+'/'+str(tr[rt])+str(pos[ps])+'velP_scl_filt_0.7'+'.csv'
                    print(path)
                    if not os.path.exists(path):
                        os.makedirs(path)
                    #save=svB+str(br[b])+str(sets[st])+'/'+str(tr[rt])+str(pos[ps])
                    #print(pd.read_csv(path))
                    yc1=list((pd.read_csv(path))[parm])
                    #print(yc1)
                    spdl.append((yc1))
                    cnal=len(yc1)/6
                    cellc.append(cnal)
                    #if parm=='Avg_v':
                        #yc1=list(map(lambda x: x*-1,yc1))
                    #print(np.mean(yc1))
                    #fn=sorted(list(set((pd.read_csv(path))['frame'])))
                    #nof=(fn[-1]/4)+1
                    cn,bn=np.histogram(yc1,bins)
                    #print('lll',cn)
                    print(len(cn),len(bn))
                    #matC.append(cn)
                    #print(cn,type(cn))
                    cn=cn/sum(cn)
                    #print(len(cn))
                    
                    matP=matP+list(cn)
                    
                
            #print(matP)
            print(len(matP))
            matP=np.matrix(matP)
            matP=matP.reshape((len(br)*len(tr)),len(cn))
            #print(matP[:,0])
            
            
           
            
            
            for jj in range(len(cn)):
               
                meanP,stdevP=np.mean(matP[:,jj]),np.std(matP[:,jj])
                #sm=(np.sum(matf[:,jj]))
                allM.append(meanP)#/sm)
                
                allS.append(stdevP)
          
    allM,allS=(np.matrix(allM)).reshape(len(sets),cc-1),(np.matrix(allS)).reshape(len(sets),cc-1)    
    rf,cf=((allM).shape) 
    for tt in range(rf):
        mdat=allM[tt,:]
        kk=((mdat).tolist())
        kk=kk[0]
        #print(kk)
        sdat=allS[tt,:]
        kp=((sdat).tolist())
        kp=kp[0]
        #if parm=='Avg velocity':
         #   label=
        plt.gcf().set_size_inches(6,3)
        plt.errorbar(binsf,kk,yerr=kp,fmt='o',color=colz[tt])#,label='Avg.speed='+str(np.mean(kk))+'\u03BC'+'m/s')
        plt.ylabel('Rel. Freq',labelpad=15,fontsize=18,fontweight=15)
        plt.xlabel(lab,labelpad=15,fontsize=18,fontweight=15)
        #plt.xticks(np.arange(x0,xf,20))
        #plt.gca().xaxis.set_major_locator(plt.MaxNLocator(5))
        #plt.legend()
        #plt.savefig(svB+pos[0]+nem+'//'+tym[tt]+'.png')
        plt.show()
        return(binsf,kk,kp)
    #print(x)
    #return(bines,mlP,sdlP)
    
biny,avsp,avsd=mot_plt(pth1,'Avg velocity', 0,150,10,'Absolute Speed ('+'\u03BC'+'m/s)','Speed')
#mot_plt(pth1,'Avg_v', -100,100,5,'y Component ('+'\u03BC'+'m/s)','y Comp')
#mot_plt(pth1,'Avg_u', -100,100,5,'x Component ('+'\u03BC'+'m/s)','x Comp')
print(avsp,avsd)

spT=[0.0, 0.0, 0.003034504377740588, 0.02205883232955654, 0.04001005853921465, 0.06402635284138868, 0.09227849212325562, 0.1473350725711832, 0.19069268252030722, 0.18909927457378695, 0.13603200887963982, 0.07234078885010303, 0.03143640692564351, 0.011655525468180236]
sdT=[0.0, 0.0, 0.001920603973199928, 0.008588252772792725, 0.011567106663139272, 0.011520868253488449, 0.013222183806545088, 0.009612789531930595, 0.015539471648581351, 0.020010917423920353, 0.016650015017418317, 0.013516866250594162, 0.008689058493739948, 0.00437785851890331]
spB=[0.0, 0.0, 0.004692087252314652, 0.03155725033141769, 0.04891312839330122, 0.06720919821096329, 0.09128470446611424, 0.13540208860905953, 0.17475402981035235, 0.1863169383506179, 0.13847774014722383, 0.0770475892206466, 0.03178253543191844, 0.012562709776070215]
sdB= [0.0, 0.0, 0.0038250270029082617, 0.016069014428934575, 0.020930277100882223, 0.026613456020000426, 0.028626050692504457, 0.027479612247521542, 0.0220449559236443, 0.032224120024779083, 0.04472013202350688, 0.030051097033949876, 0.01558875759108872, 0.005336386126863436]

#plt.errorbar(biny,spT,yerr=sdT,color='r',fmt='o')
#plt.errorbar(biny,spB,yerr=sdB,color='b',fmt='^')
biny=biny-5
plt.errorbar(biny,spT,color='r',fmt='o',label='Top')
plt.errorbar(biny,spB,color='b',fmt='^',label='Bottom')
plt.fill_between(biny,np.array(spT)+np.array(sdT),np.array(spT)-np.array(sdT),facecolor='r',alpha=.35)
plt.fill_between(biny,np.array(spB)+np.array(sdB),np.array(spB)-np.array(sdB),facecolor='b',alpha=.35)
plt.yticks(np.arange(0,0.26,.1))
plt.xticks(np.arange(0,140,40))
plt.legend(fontsize=15)
plt.show()
print(biny)
#print(type(biny))
print('counts:', cellc, np.mean(cellc),np.std(cellc))

cffl,bffl=[],[]
for xu in range(len(spdl)):
    cfl,bfl=np.histogram(np.array(spdl[xu]),bins=np.arange(0,200,10))
    cfl=cfl/(sum(cfl))
    print(cfl,sum(cfl))
    cffl.append(cfl)
    bffl.append(bfl)
    

##################### speed avg ################
spdl=[]+spdl[0]+spdl[1]+spdl[2]+spdl[3]+spdl[4]+spdl[5]
#print('avg speed',np.mean(spdl,axis=0))#,'+-',np.std(spdl))
print(len(spdl),np.mean((spdl)),np.std((spdl)))
dfd=[]
for xxo in cellc:
    dfd.append(xxo*6)
print(np.sum(dfd))
cf,bf=np.histogram(spdl,bins=np.arange(0,200,10))
cf=list(np.array(cf)/20546)
print(len(cf),len(bf))
plt.plot(bf[:-1],cf,'ro')
plt.show()
print(list(np.mean(cffl,axis=0)),list(np.std(cffl,axis=0)))
bnF=[  0. , 10.,  20.,  30.,  40.,  50.,  60.,  70. , 80.,  90., 100., 110., 120., 130.,140., 150. ,160., 170., 180.]
spTf=[0.0, 0.0, 0.0030228391659843368, 0.0219738207585999, 0.03984696735563277, 0.0637688635333565, 0.09190325754254579, 0.14670327777756678, 0.18986029902803617, 0.18825425314492042, 0.1354071038020097, 0.07201093195299679, 0.03128248705353873, 0.011596035028707659, 0.004369863856104421, 0.0, 0.0, 0.0, 0.0]
sdTf=[0.0, 0.0, 0.0019172120148886885, 0.008587855838541901, 0.011573402184338503, 0.011580709295676834, 0.01333242047716029, 0.00976426419590089, 0.015502179977609427, 0.019748720383754914, 0.016333507388245082, 0.013396016962448623, 0.008587948211115495, 0.004334868958088027, 0.0024769991874170815, 0.0, 0.0, 0.0, 0.0]
spBf=[0.0, 0.0, 0.0046729953340951804, 0.031400364487086184, 0.04868024674412331, 0.06689908284737411, 0.09085086120482512, 0.1347487610280373, 0.17387054605975286, 0.1853216333677883, 0.13766414671540575, 0.07657831523575882, 0.03158043064026475, 0.012482933836493218, 0.005249682498995069, 0.0, 0.0, 0.0, 0.0]
sdBf=[0.0, 0.0, 0.003821444926344396, 0.016013136409652056, 0.02090779186179485, 0.026650881544118724, 0.028682803786750737, 0.027693991322900204, 0.02220981876778649, 0.03203478510051924, 0.04429927659754899, 0.029759527725304363, 0.015461207085701506, 0.005279647526477737, 0.002695554656693563, 0.0, 0.0, 0.0, 0.0]
plt.rcParams["font.family"] = "Times New Roman"
plt.errorbar(bnF,spTf,color='r',fmt='o',label='Top')
plt.fill_between(bnF,np.array(spTf)+np.array(sdTf),np.array(spTf)-np.array(sdTf),facecolor='r',alpha=.35)
plt.errorbar(bnF,spBf,color='b',fmt='o',label='Bottom')
plt.fill_between(bnF,np.array(spBf)+np.array(sdBf),np.array(spBf)-np.array(sdBf),facecolor='b',alpha=.35)
plt.xlim(-1.5,155)
plt.yticks(np.arange(0,0.25,.1))
plt.xticks(np.arange(0,160,50))
plt.gcf().set_size_inches(5,3)
plt.legend(fontsize=15,loc='upper left')
plt.show()