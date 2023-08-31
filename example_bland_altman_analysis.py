"""
Example of Bland-Altman analysis
 
    2023, Carmen Ensink, Sint Maartenksliniek,
    c.ensink@maartenskliniek.nl

"""

# Import dependencies
import numpy as np
import matplotlib as mpl
from bland_altman_analysis import bland_altman_plot

# Random data
data_reference = np.append(np.append(np.random.rand(50), np.random.rand(50)+3), 1.5*(np.random.rand(50)+1.5))
data_new = np.append(np.append(0.5*data_reference[0:50]+2+0.4*np.random.rand(50), 0.7*data_reference[50:100]+1.8+np.random.rand(50)), 0.4*data_reference[100:150]+2.4+0.6*(np.random.rand(50)))

# Bland-Altman plot
mean_difference, sd_difference = bland_altman_plot(data_reference, data_new)
