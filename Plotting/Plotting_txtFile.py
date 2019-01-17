# -*- coding: utf-8 -*-
"""
Created on Wed Aug 13 13:08:34 2014
# Plot data in .txt file
@author: salter
"""

from matplotlib import *
import matplotlib.pyplot as plt
import numpy as np

close('all') #close all open windows

data = loadtxt("blah.txt") #loadtxt is a numpy function


fig, ax1 = plt.subplots()
x = data[:,0]
y = data[:,1]
ax1.plot(x, y, 'b-')
#plt.ticklabel_format(style='sci', scilimits=(0,0))
ax1.set_xlabel('Wavelength (nm)',fontsize='large')
ax1.set_ylabel('Intensity (counts)',fontsize='large')
ax1.set_title('Spectrum of apparent fibre fluorescence')

#plt.savefig('Laser 532 in reflection with Laser Line Filter.png')


"""
ax2 = ax1.twinx()
s2 = np.sin(2*np.pi*t)
s3 = np.sin(4*np.pi*t)
ax2.plot(t, s2, 'r.')
ax2.plot(t, s3, 'r.')
ax2.set_ylabel('sin', color='r')
# Make the y-axis label and tick labels match the line color.
for tl in ax2.get_yticklabels():
    tl.set_color('r')
plt.show()

"""