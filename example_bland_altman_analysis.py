"""
Example of Bland-Altman analysis
 
    2023, Carmen Ensink, Sint Maartenksliniek,
    c.ensink@maartenskliniek.nl

"""

# Import dependencies
import numpy as np
import matplotlib as mpl
from bland_altman_analysis import bland_altman_analysis

# Generate random data
data_reference = 10*np.append(np.append(np.random.rand(50)+2, np.random.rand(50)+3), np.random.rand(50)+4)
data_new = np.append(np.append(data_reference[0:50]+0.5*np.random.rand(50)-0.3*np.random.rand(50), data_reference[50:100]+0.4*np.random.rand(50)-0.2*np.random.rand(50)), data_reference[100:150]+0.4*(np.random.rand(50)))
# Generate outliers
for i in range(0,50,7):
    data_new[i] = data_new[i] + 4*np.random.rand(1)
for i in range(0,50,8):
    data_new[i] = data_new[i] - 4*np.random.rand(1)
for i in range(50,100,5):
    data_new[i] = data_new[i] + 2.5*np.random.rand(1)
for i in range(50,100,7):
    data_new[i] = data_new[i] - 2.5*np.random.rand(1)
for i in range(100,150,7):
    data_new[i] = data_new[i] + 3.5*np.random.rand(1)
for i in range(100,150,8):
    data_new[i] = data_new[i] - 3.5*np.random.rand(1)

# Bland-Altman analysis
mean_difference, sd_difference = bland_altman_analysis(data_reference, data_new)
