'''
Surface_type attribute has predefined classification of land as:
    0 = open oceans or semi-enclosed seas; 1 = enclosed seas or lakes; 2 = continental ice; 3 = land 
'''
from netCDF4 import Dataset
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
nc = Dataset('test2.nc','r')
surface = nc.variables['surface_type'][:]

print(nc.variables['surface_type'])


waveform = nc.variables['waveforms_40hz'][:]
waveform_mean = np.mean(waveform, 1)
print(surface[135])
print(surface[136])

'''
Printing indices of different surface type
'''
for i in range(2800):
    if (surface[i]==3):
        print(i)
print('\n')
for i in range(2800):
    if (surface[i]==2):
        print(i)
'''
Plotting surface type
'''
plt.subplot(3,1,1)
plt.plot(surface,'rx')

'''
Performing K-S test between different surface types using the index calculated above
'''
plt.subplot(3,1,2)
plt.plot(waveform_mean[135,:])
plt.plot(waveform_mean[136,:])
print(stats.ks_2samp(waveform_mean[135,:],waveform_mean[136,:]))
print(stats.ks_2samp(waveform_mean[136,:],waveform_mean[135,:]))     
print(stats.ks_2samp(waveform_mean[135,:],waveform_mean[137,:]))
print(stats.ks_2samp(waveform_mean[138,:],waveform_mean[139,:]))   