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
import math
from matplotlib.patches import Circle
from skimage import measure
from skimage.segmentation import clear_border
import scipy.stats as stats
#pthB='P:/HA452_Motility/24h_R2/BR1/'
#svB='C:/PhD/Hak_motility/24hrs/R2/Analysed/BR1/'#3/TR2/Top/Bias//'
h1,h2=30,2020

br=['BR1/','BR2/','BR3/']
###No BR as diff BRs can have diff h1,h2####
sets=[4]#,2,3,4,5,6]
tr=['TR1/','TR2/']
pos=['Bot/']#,'Top/']

##########################4 poz changes ###################
cellc=[]
fin_rf=[] #all rel freq
ml,sdl=[],[]

for ps in range(len(pos)):    
    for st in range(len(sets)):
        mat=[]
        
        
        for b in range(len(br)):
            #ar_tr=[]
            #ls=[]
            for rt in range(len(tr)):
                
                path='C:/PhD/Hak_motility/24hrs/R2/Analysed/'+str(br[b])+str(sets[st])+'/'+str(tr[rt])+str(pos[ps])+'Bias//y_combined.csv'
                print(path)
                yc1=list((pd.read_csv(path))['yval'])
                #print(yc1)

                fn=sorted(list(set((pd.read_csv(path))['frame'])))
                ccnt=len(yc1)/len(fn)
                cellc.append(ccnt)
                cn,bn=np.histogram(yc1,bins=20)
                
                cn=cn/sum(cn)
                
               
                mat.append(cn)
                
                #ls=ls+yc1
            #print(len(ls))
            #print(len(ls))
            #cnt,bine=np.histogram(ls,bins=20)
            #print(cnt,bine,sum(cnt))
            #cnt=cnt/sum(cnt)
###############  becoz frame numbers may not match, better to normalize before averaging #######            
            #print(cnt)            
            
                
        matf=np.matrix(mat)
        fin_rf=fin_rf+(mat)
        

        row,col=matf.shape
        mn,dv=[],[]
        #print(matf,row,col)
        for jj in range(col):
        #print(jj)
            mean,stdev=np.mean(matf[:,jj]),np.std(matf[:,jj])
            #sm=(np.sum(matf[:,jj]))
            mn.append(mean)#/sm)
            
            dv.append(stdev)
        mna=mn
        dva=dv
        #mna=(np.array(mn)/sum(np.array(mn)))
        #dva=(np.array(dv)/sum(np.array(mn)))
        #print(len(mna),'ooo',len(dva))
        ml.append(mna)
        sdl.append(dva)
print('avg',ml)
print('stdv',sdl)


#plt.barh(bn[1:],ml[0])
#print(ml[0])
        ################  ubias from avergae ####################
av1B=[0.23802157106611396, 0.150805311402005, 0.10594076931572459, 0.07657117306445103, 0.058727610991735436, 0.04443937518638765, 0.03327293351022182, 0.029944711619127855, 0.0236913901338183, 0.023845667733087716, 0.023164798548472813, 0.01687839216539916, 0.015448629556516748, 0.016287853075729965, 0.015271682650769627, 0.01756351442713361, 0.015735841819370374, 0.021338183527100495, 0.024344108889946703, 0.04870648131688707]
sd1B=[0.05890776364200283, 0.040484238095576046, 0.02601319377615786, 0.01604689409005669, 0.013383947250292379, 0.005933922972603497, 0.005838170003105987, 0.010512229547674513, 0.008962577808918012, 0.009983063784592692, 0.015118793708410485, 0.010715152016388084, 0.007708272742714066, 0.008369563240688077, 0.009765810830821132, 0.009258019243480858, 0.008838002222821276, 0.007688403446644277, 0.012612962158301792, 0.018597914593793216]

av1T=[0.13567200724661013, 0.10328121527938888, 0.07977458223099335, 0.06610401651542362, 0.053020065109599224, 0.044621272981666425, 0.037039078557470524, 0.03512908268980777, 0.030159316336370836, 0.030201588793510717, 0.027533812210207037, 0.02631153310594009, 0.02551396547006965, 0.025658182700036152, 0.025306512773435357, 0.03026191787389269, 0.03429487499217305, 0.041053328359681486, 0.057311783646407814, 0.09175186312731519]
sd1T=[0.01948039333511903, 0.010456176573092585, 0.013285302159083889, 0.008261784861581807, 0.008928977113130494, 0.006962981495296425, 0.0062365025855602805, 0.0032861368927744913, 0.0011104873020088644, 0.00284445344305926, 0.003969609494672997, 0.003223027145522523, 0.0030787859979921482, 0.0034707528144393793, 0.00481126461900736, 0.005698564385009802, 0.006400707626155807, 0.006581936594140995, 0.010033331988280934, 0.02247433340285615]

#plt.errorbar(bn[1:],av1T,yerr=sd1T,color='b',label='Top')
#plt.errorbar(bn[1:],av1B,yerr=sd1B,color='g',label='Bottom')
#print(bn[1:])
plt.rcParams["font.family"] = "Times New Roman"
#plt.rcParams["font.size"] = "100"
plt.errorbar(bn[1:],av1T,color='r',label='Top')
plt.errorbar(bn[1:],av1B,color='b',label='Bottom')
plt.fill_between(bn[1:],np.array(av1T)+np.array(sd1T),np.array(av1T)-np.array(sd1T),facecolor='r',alpha=.35)
plt.fill_between(bn[1:],np.array(av1B)+np.array(sd1B),np.array(av1B)-np.array(sd1B),facecolor='b',alpha=.55)
plt.ylim(0,.2)
plt.xlim(80,2002)
plt.gca().yaxis.tick_right()
plt.legend(loc=('center'),fontsize=14)
plt.plot([397.6,397.6],[0,.2],'--',color='#F87014')
plt.plot([1689.8,1689.8],[0,.2],'--',color='#9A62FE')
plt.tight_layout()
plt.show()
#print(bn,len(bn),ml[0],len(ml[0]))
'''
n1B,n2B=np.sum(av1B[:4]),np.sum(av1B[-4:])
bB=(n1B-n2B)/(n1B+n2B)
print('Bias Bot',bB)

n1T,n2T=np.sum(av1T[:4]),np.sum(av1T[-4:])
bT=(n1T-n2T)/(n1T+n2T)
print('Bias Top',bT)
'''
#####################  ubias bias direcet calc #################
n1v,n2v=[],[]
for kk in range(len(matf)):
    x=np.sum(matf[kk][0,:4])
    n1v.append(x)
    n2v.append(np.sum(matf[kk][0,-4:]))
bva=[]
for ie in range(len(n1v)):
    npc=n1v[ie]+n2v[ie]
    nmc=n1v[ie]-n2v[ie]
    bva.append(nmc/npc)
print('mean,stdv',np.mean(bva),np.std(bva))


plt.bar(['Top','Bot'],[.25,.6586],yerr=[.135,.17],color=['r','b'],capsize=10)
plt.gcf().set_size_inches(3,4)
#plt.legend()
plt.yticks(np.arange(0,1.25,.25))

print(np.mean(cellc),np.std(cellc))

'''
Stat test done using online software, check imgs v6'''
