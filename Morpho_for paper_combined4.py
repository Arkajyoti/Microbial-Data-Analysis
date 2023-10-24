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

#df=pd.read_excel('P:/Manuscript/24h+chem_sig/AS plots/c-a values.xlsx',header=None)
#print(df)


mTT,sTT=[0.649,	0.648,	0.628,	0.622],[0.057	,0.063,	0.052,	0.049]
mBB,sBB=[0.618,	0.614	,0.613	,0.645],[0.058,	0.057,	0.04,	0.011]
mTB,sTB=[0.601	,0.642,	0.634	,0.668],[0.04	,0.08,	0.05	,0.03]
mBT,sBT=[0.657	,0.623,	0.666	,0.63],[0.052	,0.06,	0.08	,0.043]

ty=['0','20','60','120']

tt,bb,tb,bt='#ee5c42','purple','#2F4F4F','#FFFACD'

plt.plot(ty,mTT,'o-',color=tt)
plt.fill_between(ty,np.array(mTT)-np.array(sTT),np.array(mTT)+np.array(sTT),color=tt,alpha=0.35)
plt.ylim(0.55,0.75)
plt.yticks(np.arange(0.54,.84,.1))
#plt.show()
plt.plot(ty,mBB,'o-',color=bb)
plt.fill_between(ty,np.array(mBB)-np.array(sBB),np.array(mBB)+np.array(sBB),color=bb,alpha=0.35)
#plt.ylim(0.55,0.75)
#plt.yticks(np.arange(0.55,.9,.15))


plt.plot(ty,mTB,'o-',color=tb)
plt.fill_between(ty,np.array(mTB)-np.array(sTB),np.array(mTB)+np.array(sTB),color=tb,alpha=0.35)
#plt.ylim(0.55,0.85)
#plt.yticks(np.arange(0.55,.9,.15))

plt.plot(ty,mBT,'o-',color=bt)
plt.fill_between(ty,np.array(mBT)-np.array(sBT),np.array(mBT)+np.array(sBT),color=bt,alpha=0.35)
#plt.ylim(0.55,0.85)
#plt.yticks(np.arange(0.55,.9,.15))
plt.show()


plt.plot(ty,mTT,'o-',color=tt)
plt.fill_between(ty,np.array(mTT)-np.array(sTT),np.array(mTT)+np.array(sTT),color=tt,alpha=0.35)
plt.ylim(0.55,0.75)
plt.yticks(np.arange(0.54,.84,.1))
plt.show()
plt.plot(ty,mBB,'o-',color=bb)
plt.fill_between(ty,np.array(mBB)-np.array(sBB),np.array(mBB)+np.array(sBB),color=bb,alpha=0.35)
plt.ylim(0.55,0.75)
plt.yticks(np.arange(0.54,.84,.1))
plt.show()
plt.plot(ty,mTB,'o-',color=tb)
plt.fill_between(ty,np.array(mTB)-np.array(sTB),np.array(mTB)+np.array(sTB),color=tb,alpha=0.35)
plt.ylim(0.55,0.75)
plt.yticks(np.arange(0.54,.84,.1))
plt.show()
plt.plot(ty,mBT,'o-',color=bt)
plt.fill_between(ty,np.array(mBT)-np.array(sBT),np.array(mBT)+np.array(sBT),color=bt,alpha=0.35)
plt.ylim(0.55,0.75)
plt.yticks(np.arange(0.54,.84,.1))
plt.show()
