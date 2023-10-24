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

oT11=[20.83333333
,20
,11.9047619
,14.28571429
,12.82051
,12.82051282
,5.319148936
,17.24137931
,7.278020378
,8.038585209
,5.952380952
,12.5
]
oT11=pd.read_csv('file:///C:/PhD/Hak_motility/24hrs/R2/Analysed_Reor/Combined_Mean_Sd/11h/Top/Us/11h_Top_Us_Allreplicates-fin.csv')['time2'][:12]
oB11=pd.read_csv('file:///C:/PhD/Hak_motility/24hrs/R2/Analysed_Reor/Combined_Mean_Sd/11h/Bot/Us/11h_Top_Us_Allreplicates-fin2.csv')['time2'][:12]
#print(oB11)

av1T,sd1T=np.mean(oT11),np.std(oT11)
av1B,sd1B=np.mean(oB11),np.std(oB11)

plt.gcf().set_size_inches(7,7)
plt.bar(['Top','Bot'],[av1T,av1B],yerr=[sd1T,sd1B],color=['r','b'],capsize=10)#,label=['Top','Bottom'])
#plt.legend()
plt.yticks(np.arange(0,45,10))
plt.xticks([])
plt.show()
#plt.yticks(np.arange(0,25,5),[0,5,10,15,20])
print('Top',av1T,'+-',sd1T,'Bot',av1B,'+-',sd1B)

#######################################################


############################## night time ############################
plt.gcf().set_size_inches(4,3)
plt.bar(['Top','Bot'],[12.6,6.32],yerr=[7.6,3.03],color=['r','b'],capsize=10)#,label=['Top','Bottom'])
#plt.legend()
plt.ylim(0,30)
plt.yticks(np.arange(0,40,10))
plt.xticks([])

'''' Stat test done using online, see Images v7....For AS'''''
