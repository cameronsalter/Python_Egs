# -*- coding: utf-8 -*-
"""
Created on Wed Aug 13 13:08:34 2014
# Plotting tests
@author: salter
"""

from matplotlib import *
import matplotlib.pyplot as plt
import numpy as np

#close('all') #close all open windows

## Two (or more) datasets with same x-axis and y=axes on opposite sides of one plot
####################################################################################
fig, ax1 = plt.subplots(nrows=1, ncols=1,figsize=[8,6])
t = np.arange(0.01, 10.0, 0.01)
s1 = np.exp(t)
ax1.plot(t, s1, 'b-')
ax1.set_xlabel('time (s)')
# Make the y-axis label and tick labels match the line color.
ax1.set_ylabel('exp', color='b')
for tl in ax1.get_yticklabels():
    tl.set_color('b')
plt.tick_params(axis='both', which='major', labelsize=15)

ax2 = ax1.twinx()
s2 = np.sin(np.pi*t)
s3 = np.sin(2*np.pi*t)
ax2.plot(t, s2, 'r.')
ax2.plot(t, s3, 'r.')
ax2.set_ylabel('sin', color='r')
for tl in ax2.get_yticklabels():
    tl.set_color('r')
ax2.annotate('Annotate the plot',xy=(0.1,0.9),xycoords='axes fraction',fontsize=15)
plt.show()

## Multiple graphs plotted in an array
#################################################################
# From: http://matplotlib.org/examples/pylab_examples/subplots_demo.html
#More e.gs available there
#import matplotlib.colors as colors
#import matplotlib.cm as cmx

x = np.arange(0.01, 10.0, 0.01)
y = np.sin(np.pi*x)

Nplots=20
nrows=Nplots/4
ncols=4

"""
#For line colours
jet = plt.get_cmap('spectral') 
cNorm  = colors.Normalize(vmin=0, vmax=Nplots)
scalarMap = cmx.ScalarMappable(norm=cNorm, cmap=jet)
"""

colors = plt.cm.jet(np.linspace(0,1,Nplots))

fig, axarr = plt.subplots(nrows, ncols, sharey=True, figsize=[10,10]) #Array of axes is produced
PlotNo=-1
for row in range(0,nrows):
    for col in range(0,ncols):
        PlotNo=PlotNo+1
        colorVal = colors[PlotNo] #scalarMap.to_rgba(PlotNo)
        axarr[row,col].plot(x, y, label="Row=%.2f, Col=%.1f" %(row,col), color=colorVal)
        axarr[row,col].set_xlim(0, 10)
        axarr[row,col].set_ylim(-1.5, 1.5)
        axarr[row,col].legend(fontsize='9')
        axarr[row,col].tick_params(axis='both', which='major', labelsize=10)
        axarr[row,col].set_xlabel('X')
        axarr[row,col].set_ylabel('Y')
        axarr[row,col].grid()
plt.suptitle('Title centered above all subplots', size='x-large', y=1)     
fig.tight_layout()


## Multiple datasets in one plot with offset and legend outside plotted area
###############################################################################
x = np.arange(0.01, 10.0, 0.01)
y = np.sin(np.pi*x)

Nplots=20
yOffsetStep=1

"""
jet = plt.get_cmap('spectral') 
cNorm  = colors.Normalize(vmin=0, vmax=Nplots)
scalarMap = cmx.ScalarMappable(norm=cNorm, cmap=jet)
"""
colors = plt.cm.jet(np.linspace(0,1,Nplots))

fig, ax1 = plt.subplots(1, 1, figsize=[10,8])
LabelList=[]
offset=0
for PlotNo in range(0,Nplots,1):
    colorVal = colors[PlotNo]#scalarMap.to_rgba(PlotNo)
    ax1.plot(x, y+offset, color=colorVal)
    LabelList.append("Plot no.= %.1d" %(PlotNo))
    offset=offset+yOffsetStep    
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_xlim(0, 10)
ax1.set_ylim(-1, offset)

# Plot Legend. Shrink current axis by 20% to fit legend
box = ax1.get_position()
ax1.set_position([box.x0, box.y0, box.width * 0.75, box.height])
ax1.legend(LabelList,loc='center left', bbox_to_anchor=(1, 0.5),fontsize=10, title="Label list")


## Interactive plot with two sliders
###############################################################################
# To mkae interactive should be plotted either in its own window or using %matplotlib notebook in ipyhon notebook
from matplotlib.widgets import Slider, Button, RadioButtons

def sine_signal(amp, freq, phase):
    return amp * np.sin(2 * np.pi * freq * t + phase)
    
t = np.arange(0.0, 1.0, 0.001)
amp_0 = 5
freq_0 = 2
phase = [0,np.pi]

fig, ax = plt.subplots(nrows=1, ncols=1,figsize=[10,8])
fig.subplots_adjust(left=0.25, bottom=0.25) # Adjust the subplots region to leave some space for the sliders and buttons
colormap = ['g','b']
# Draw the initial plot
linelist = [[]]*2 # The 'linelist' variable is used for modifying the line later
annotation=[]
for i in range(len(linelist)): # cycle through each variable to be plotted
    linelist[i] = ax.plot(t, sine_signal(amp_0, freq_0, phase[i]), linewidth=2, color=colormap[i])
ann = ax.annotate('Amplitude = %1.1f. freq = %1.2f'%(amp_0,freq_0),xy=(0.1,0.9),xycoords='axes fraction',fontsize=15)
annotation.append(ann)

# Add two sliders for tweaking the parameters
# Define an axes area and draw a slider in it
axis_color = 'lightgoldenrodyellow'
amp_slider_ax  = fig.add_axes([0.25, 0.15, 0.65, 0.03], axisbg=axis_color)
freq_slider_ax = fig.add_axes([0.25, 0.1, 0.65, 0.03], axisbg=axis_color)
amp_slider = Slider(amp_slider_ax, 'Amp', 0.1, 10.0, valinit=amp_0,valfmt='%1.1f')
freq_slider = Slider(freq_slider_ax, 'Freq', 0.1, 30.0, valinit=freq_0,valfmt='%1.1f')

# Define an action for modifying the line when any slider's value changes
def sliders_on_changed(val):
    for i in range(len(linelist)):  # cycle through each Eval for a given strain        
        linelist[i][0].set_ydata(sine_signal(amp_slider.val, freq_slider.val,phase[i]))        
    annotation[0].set_text('Amplitude = %1.2f. freq = %1.2f'%(amp_slider.val,freq_slider.val))    
    fig.canvas.draw_idle()
    
amp_slider.on_changed(sliders_on_changed)
freq_slider.on_changed(sliders_on_changed)

plt.show()