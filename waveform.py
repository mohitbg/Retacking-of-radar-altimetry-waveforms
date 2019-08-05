
""" 
Open anaconda prompt and paste the line "conda install -c anaconda netcdf4" to install netcdf4 package
scipy package is used to perform K-S test
 """
from netCDF4 import Dataset 
import numpy as np
import matplotlib.pyplot as plt
import pylab
from scipy import stats 
''' For ploting in 3D'''
#from mpl_toolkits.mplot3d import Axes3D 
#fig = plt.figure()
#ax = fig.add_subplot(111, projection='3d')

''' 
Reading netcdf file
'''
nc = Dataset('test2.nc','r')
"""printing variables and size present in netcdf file"""
for i in nc.variables:
    print(i,nc.variables[i].shape) 
    
waveform = nc.variables['waveforms_40hz'][:]
'''
printing attributes of variables
'''
print(nc.variables['surface_type'])
print(nc.variables['waveforms_40hz'])
'''
calculating mean about axis 1 i.e meas_ind to eliminate random errors
'''
waveform_mean = np.mean(waveform, 1)
'''

Plotting data --> exploring
'''
plt.subplot(4, 1, 1)
plt.plot(waveform[500, 0, :])
plt.plot(waveform[500, 8, :])
plt.plot(waveform[500, 16, :])
plt.plot(waveform[500, 32, :])
plt.plot(waveform[500, 39, :])

plt.subplot(4, 1, 2)
plt.plot(waveform_mean[500,:])
plt.plot(waveform_mean[100,:])

plt.subplot(4, 1, 3)
pylab.plot(waveform[0, 20, :],label="1")
pylab.plot(waveform[100, 20, :],label='2')
pylab.plot(waveform[500, 20, :],label='3')
pylab.plot(waveform[1000, 20, :],label='4')
#pylab.plot(waveform[2000, 20, :],label='5')
pylab.legend(loc='upper left')

'''
Ploting mean of waveform
'''
plt.subplot(4,1,4)
pylab.plot(waveform_mean[0,:],label="1")
pylab.plot(waveform_mean[100, :],label='2')
pylab.plot(waveform_mean[500, :],label='3')
pylab.plot(waveform_mean[1000, :],label='4')
#pylab.plot(waveform_mean[2000, :],label='5')
pylab.legend(loc='upper left')
'''
Performing K-S test of two samples(Refer to k2samp.py for more info.)
'''
print(stats.ks_2samp(waveform_mean[100,:],waveform_mean[500,:]))
'''
Ploting the data in 3D
'''
#xs=waveform[1,1,:]
#ys=waveform[:,1,1]
#zs=waveform[1,:,1]
#ax.plot(xs,ys,zs)