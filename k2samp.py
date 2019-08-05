from scipy import stats
import numpy as np
np.random.seed(12345678)  #fix random seed to get the same result
n1 = 40 # size of first sample 
n2 = 40  # size of second sample
 

'''
Generating random number distributions with different means(loc) and variances(scale) 
''' 
rvs1 = stats.norm.rvs(size=n1, loc=0., scale=1)
rvs2 = stats.norm.rvs(size=n2, loc=0.5, scale=1.5)
rvs3 = stats.norm.rvs(size=n2, loc=0.001, scale=1.0)
rvs4 = stats.norm.rvs(size=n2, loc=0.0, scale=1.0)

print(rvs1)
print('\n')
print(rvs2)
print('\n')
print(rvs3)
print('\n')
print(rvs4)

'''
Printing K-S results between the distributions
'''

print(stats.ks_2samp(rvs1, rvs4))
print(stats.ks_2samp(rvs1, rvs3))
print(stats.ks_2samp(rvs1, rvs2))

'''
For a different distribution, we can reject the null hypothesis since the pvalue is below 1%:
For a slightly different distribution, we cannot reject the null hypothesis at a 10% or lower alpha since the p-value at 0.144 is higher than 10%
For an identical distribution, we cannot reject the null hypothesis since the p-value is high, 41%:
'''




