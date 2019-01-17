# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 17:01:39 2017

#Plot scattering parameter measurements

CPWG_v1 measurements taken outside cryo, bare CPWG on 27/1/17
@author: admin
"""

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import os

AnalyFreq= 2.870    # Analyse data at this frequency (in GHz)

filenames=sorted([item for item in os.listdir(os.getcwd()) if ".csv" in item])
print('files found =',filenames)
labels=('S11','S12')


fig, ax1 = plt.subplots(nrows=1, ncols=1)
for i in range(0,np.size(filenames)):
    x,y=np.loadtxt(filenames[i],delimiter=';',skiprows=3,usecols=(0,1),unpack=True)
    x = x/1e9
    S_at_AnalyFreq = y[np.argmin(abs(x-AnalyFreq))]
    ax1.plot(x,y,label=labels[i])
    ax1.annotate('%s = %.2f'%(labels[i],S_at_AnalyFreq),(3,-15-3*i))

plt.legend(loc=0)
plt.axvline(AnalyFreq,color='k',linestyle='--')
plt.annotate('Freq = %.2f GHz'%AnalyFreq,(AnalyFreq-0.3,-10),rotation=90)
plt.title("Co-planar waveguide v1, outside cryo (27/1/17)")
plt.xlabel("Frequency [GHz]")
plt.ylabel("Scattering parameter [dB]")

plt.savefig('S11andS12.png')