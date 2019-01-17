#Code from oliver gugenberger tp plot a 3D function. The data points are interpolated using a polynomial function to create a 3D mesh.

import matplotlib.pyplot as plt
from matplotlib import cm	# 3d plot
import numpy as np
import scipy.interpolate

#from mpl_toolkits.mplot3d import Axes3D #3D Plots
#from mayavi.mlab import * #3D Plots
#import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d # 3d plot
#from matplotlib import cm # 3d plot
from matplotlib.ticker import LinearLocator, FormatStrFormatter #3d plot

scale=8  # number of points
number=50 # number of points to interpolate

X=np.asarray([[0.]*scale]*scale)
Y=np.asarray([[0.]*scale]*scale)
Z=np.asarray([[0.]*scale]*scale)

for i in range(scale):
	for j in range(scale):
		X[i][j]=float(i)
		Y[i][j]=float(j)
		Z[i][j]=np.sin(float(i)+float(j))**2
		
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
#ax.plot_wireframe(X, Y, Z)	#plot with no interpolation

x=X
y=Y
z=Z
xi, yi = np.linspace(x.min(), x.max(), number), np.linspace(y.min(), y.max(), number)
xi, yi = np.meshgrid(xi, yi)
rbf = scipy.interpolate.Rbf(x, y, z, function='multiquadric') #or function='linear'
zi = rbf(xi, yi)
ax.plot_surface(xi, yi, zi, rstride=1, cstride=1, cmap=cm.coolwarm,	linewidth=0, antialiased=False)

ax.set_xlabel('x Label')
ax.set_ylabel('y Label')
ax.set_zlabel('z label')

fig.show()