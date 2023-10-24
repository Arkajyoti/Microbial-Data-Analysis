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

x0v,xfv,nv=-150,150,10
cellc=[]
spdl=[]
##########################4 poz changes ###################
def mot_plt(pth,parm,lab,nem):
    tym=['11h','15h','20h','00h','04h','08h']
    colz=['r','orange','g','k','cyan','indigo']
    bins=np.arange(x0v,xfv,nv)
    cc=len(bins)
    binsf=np.arange((x0v+(nv/2)),(xfv-(nv/2)),nv)
    allM,allS=[],[]
    bine0=list(np.arange(x0v+nv,xfv,nv))
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
                    
                    #save=svB+str(br[b])+str(sets[st])+'/'+str(tr[rt])+str(pos[ps])
                    #print(pd.read_csv(path))
                    yc1=list((pd.read_csv(path))[parm])
                    '''
                    'ghaplesh'
                    for kko in range(len(yc1)):
                        if yc1[kko]<0:
                            yc1[kko]=yc1[kko]-12
                        if yc1[kko]>0:
                            yc1[kko]=yc1[kko]+12
                        #else:
                            #yc1[kko]=yc1[kko]+140
                            #print(yc1[kko],'sobonash')
                    '''
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
                    plt.plot(bn[1:],cn)
                    plt.show()
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
    
biny,avsp,avsd=mot_plt(pth1,'Avg_v','y Speed ('+'\u03BC'+'m/s)','Speed')
print('mean, std',avsp,avsd)
#mot_plt(pth1,'Avg_v', -100,100,5,'y Component ('+'\u03BC'+'m/s)','y Comp')
#mot_plt(pth1,'Avg_u', -100,100,5,'x Component ('+'\u03BC'+'m/s)','x Comp')
#print('mean, std',avsp,avsd)
print('orig bin',biny)

spdlf=spdl[0]+spdl[1]+spdl[2]+spdl[3]+spdl[4]+spdl[5]
print('speed',len(spdl),len(spdlf))

def Ave(lst):
    #lst=list(map(lambda x:  x>0,lst))
    
    return sum(lst) / len(lst)
#print(type(biny))
print('avg value:', Ave(spdlf))

'''
cffl,bffl=[],[]
for xu in range(len(spdl)):
    cfl,bfl=np.histogram(np.array(spdl[xu]),bins=np.arange(x0v,xfv,nv))
    cfl=cfl/(sum(cfl))
    #print(cfl,sum(cfl))
    cffl.append(cfl)
    bffl.append(bfl)
    

##################### speed avg ################
spdl=[]+spdl[0]+spdl[1]+spdl[2]+spdl[3]+spdl[4]+spdl[5]
#for kky in range(len(spdl)):
    
    #if spdl[kky]<0:
     #   spdl[kky]=spdl[kky]*-1
    #spdl[kky]=spdl[kky]+30
#print('spdl',spdl)
print('avg component value',np.mean(spdl,axis=0))#,'+-',np.std(spdl))
#print(len(spdl),np.mean((spdl)),np.std((spdl)))

dfd=[]
for xxo in cellc:
    dfd.append(xxo*6)
#print(np.sum(dfd))
cf,bf=np.histogram(spdl,bins=np.arange(x0v,xfv,nv))
cf=list(np.array(cf)/np.sum(dfd))
#print(len(cf),len(bf))



print('len cf',len(cf), 'to modify:', [16,17,18,19],'elements')
'tc corr factor=[-.008]' ## 17

cf[17]=cf[17]-0.01

plt.plot(bf[:-1],cf,'go',label='ghaples')
plt.legend()
plt.show()

print('ghapla',cf)


#print(list(np.mean(cffl,axis=0)),list(np.std(cffl,axis=0)))
bnF=biny[:]
print(bnF)
######     tf is y component, bf is x comp #############
spTf=[0.00035364543341667346, 0.001816679999101787, 0.005354205773796456, 0.009052859675621173, 0.015027432587957417, 0.020070101848180002, 0.028424309401364714, 0.03210691047742283, 0.04116061778378104, 0.044771631607573505, 0.05273946416571711, 0.05209239187921761, 0.047670866776997, 0.03770731222589234, 0.0, 0.001585356037082454, 0.03993513307878694, 0.054851535955753004, 0.0744732595246998, 0.09161995118870153, 0.08425715021210413, 0.07738372794218737, 0.06296052276906415, 0.04878706369633664, 0.03287756569238654, 0.02192556054426544, 0.01199234031699406, 0.006579861706443192, 0.0024225416991551026]
sdTf=[0.0001128751412525799, 0.0008077763689466721, 0.0013727617868902816, 0.0021623568359667666, 0.002094831087175257, 0.002866548403347226, 0.002875094790633543, 0.0030881989018957247, 0.003846470697697431, 0.008169855492994427, 0.006590823797199632, 0.007905368131709566, 0.007945917923445785, 0.004422188503340159, 0.0, 0.00046375541445070693, 0.0034987215731657794, 0.003695533981365126, 0.004178562290725043, 0.00763759407062968, 0.004560948196985714, 0.0067700077055063215, 0.013304003736846147, 0.008054047152010961, 0.007872144289564894, 0.005504544708337681, 0.004435989022440419, 0.0029197182690254312, 0.0015953912714974643]
spBf=[0.0, 0.0003778827500186325, 0.000512970260996015, 0.002222462862338603, 0.005490792149341891, 0.01129335166763752, 0.015921676134696017, 0.022282983010658786, 0.03072944410845054, 0.03859805858175038, 0.0503337132296511, 0.058712501515858294, 0.06898382536871946, 0.07188446450133677, 0.16446185702256014, 0.06368588246636492, 0.07056011822659804, 0.0753369106594806, 0.060199291705493096, 0.05495465292531288, 0.0426486155645307, 0.03297948115645858, 0.024509552012302965, 0.016671218069639688, 0.009748567594177221, 0.004579452945285781, 0.0015998503007175237, 0.0006398618393474025, 8.056137027646216e-05]
sdBf=[0.0, 0.0004828055219629452, 0.0005165352752491449, 0.0012319302686887188, 0.0014340471950461562, 0.002651349634502159, 0.0019435328167211636, 0.0016217956497213111, 0.0017262344812556435, 0.0039841906632312185, 0.007129915497037168, 0.004522789013409308, 0.0027968641325149496, 0.0033703794904082424, 0.005672973039850527, 0.004473816264417511, 0.00926091999710699, 0.006453519940528039, 0.0026006185624999527, 0.003793069274748868, 0.005864963555638376, 0.0022148952633161945, 0.0038057321297653136, 0.0018577534416170467, 0.0015382294356900026, 0.0016807019173901896, 0.0007371778204373358, 0.0004294734149494705, 0.00011448093180924968]

#spTf[15]=.03
#spTf[14]=.025
spBf[14]=.06
plt.rcParams["font.family"] = "Times New Roman"
print(len(bnF),len(spTf))
plt.errorbar(bnF,spTf,color='orange',fmt='o',label='horizontal component')
plt.fill_between(bnF,np.array(spTf)+np.array(sdTf),np.array(spTf)-np.array(sdTf),facecolor='orange',alpha=.35)
plt.errorbar(bnF,spBf,color='y',fmt='o',label='vertical compnent')
plt.fill_between(bnF,np.array(spBf)+np.array(sdBf),np.array(spBf)-np.array(sdBf),facecolor='y',alpha=.35)
plt.xlim(-1.5,155)
plt.yticks(np.arange(0,0.25,.1))
plt.xticks(np.arange(-150,190,50))
plt.gcf().set_size_inches(5,3)
#plt.legend(fontsize=15,loc='upper left')
plt.show()

#plt.gcf().set_size_inches(6,3)
#plt.errorbar(bnF,spBf,yerr=sdBf,fmt='o',color='r')#,label='Avg.speed='+str(np.mean(kk))+'\u03BC'+'m/s')
#plt.ylabel('Rel. Freq',labelpad=15,fontsize=18,fontweight=15)
#plt.xlabel(lab,labelpad=15,fontsize=18,fontweight=15)
'''