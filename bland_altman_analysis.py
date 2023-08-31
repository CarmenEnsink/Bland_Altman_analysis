"""
Function to create a Bland-Altman analysis figure showing the individual data points, 
mean, and limits of agreement. 

INPUT
bland_altman_analysis(data_reference, data_new)
data_reference:   N x 1 numpy array containing the data points of the reference method
data_new:         N x 1 numpy array containing the data points of the new method
          
OPTIONAL INPUT
bland_altman_analysis(..., **kwargs)
    'Color'        Color of the data points. 
                   Defaults to black. 
    'Markersize'   Markersize of data points.
                   Defaults to 15.   
    'Alpha'        Color density of the data points.
                   Defaults to 0.5.
    'Linewidth'    Linewidth of the mean and std plot.
                   Defaults to 3.  
    'Capsize'      Capsize of the mean and std plot. 
                   Defaults to 15.
    'XLim'         Xlim [min max]
                   Defaults to standard lims. 
    'XLabel'       Xlabel {str}. 
                   Defaults to 'Mean reference data, new data'.
    'YLim'         Ylim [min max]
                   Defaults to standard lims. 
    'YLabel'       Ylabel {str}. 
                   Defaults to 'Difference new data - reference data'.
    'Title'        Title of the plot. 
                   Defaults to 'Bland-Altman analysis'.
    'Fontsize'     Fontsize [int] of the plot. 
                   Defaults to 20.
    'Labels'       Labels for values of mean difference and borders of the limits of agreement [True/False].
                   Defaults to True.
    
Copyright (c)   2023, Carmen Ensink, Sint Maartenksliniek,
                c.ensink@maartenskliniek.nl

"""

# Import dependencies
import numpy as np
import matplotlib.pyplot as plt

def bland_altman_analysis(data_reference=False, data_new=False, **kwargs):
    
    # Input errors
    if type(data_reference) == bool or type(data_new) == bool:
        raise Exception("Not enough input arguments")
    elif len(data_reference) != len(data_new):
        raise Exception('Reference data and new data should be the same length')
    
    # Defaults
    Color = 'black'
    Markersize = 15
    Alpha = 0.5
    Linewidth = 3
    Capsize = 15
    XLabel = 'Mean reference data, new data'
    YLabel = 'Difference new data - reference data'
    Title = 'Bland-Altman analysis'
    Fontsize = 20
    Labels = True
    
    # Correct data structure
    data_reference = np.asarray(data_reference)
    data_new = np.asarray(data_new)
    
    # Mean values (x-axis)
    mean = np.nanmean([data_reference, data_new], axis=0)
    # Difference values (y-axis)
    difference = data_new - data_reference
    # Mean of the difference
    mean_difference = np.nanmean(difference)
    mean_diff_string = round(mean_difference, 2).astype(str)
    # Standard deviation of the difference
    sd_difference = np.nanstd(difference, axis=0)
    UB_string = round(mean_difference + 1.96*sd_difference, 2).astype(str)
    LB_string = round(mean_difference - 1.96*sd_difference, 2).astype(str)
        
    # Check for optional inputs in **kwargs items
    for key, value in kwargs.items():
        if key == 'Color':
            Color = value
        if key == 'Markersize':
            Markersize = value
        if key == 'Alpha':
            Alpha = value
        if key == 'Linewidth':
            Linewidth = value
        if key == 'Capsize':
            Capsize = value
        if key == 'XLabel':
            XLabel = value
        if key == 'YLabel':
            YLabel = value
        if key == 'Title':
            Title = value
        if key == 'Fontsize':
            Fontsize = value
        if key == 'Labels':
            Labels = value
        
    fig = plt.subplots()
    plt.title(Title, fontsize=Fontsize)
    
    plt.scatter(mean, difference, edgecolor = 'none', facecolor=Color, alpha=Alpha, marker = 'o', s=Markersize, )
    
    plt.axhline(mean_difference, color='gray', linestyle='--', linewidth=Linewidth)
    plt.axhline(mean_difference + 1.96*sd_difference, color='gray', linestyle='--', linewidth=Linewidth)
    plt.axhline(mean_difference - 1.96*sd_difference, color='gray', linestyle='--', linewidth=Linewidth)
    
    if Labels == True:
        plt.text(np.nanmax(mean), mean_difference, mean_diff_string, fontsize=Fontsize-6) 
        plt.text(np.nanmax(mean), mean_difference + 1.96*sd_difference, UB_string, fontsize=Fontsize-6) 
        plt.text(np.nanmax(mean), mean_difference - 1.96*sd_difference, LB_string, fontsize=Fontsize-6) 
        
    plt.xlabel(XLabel, fontsize=Fontsize-6)
    plt.ylabel(YLabel, fontsize=Fontsize-6) #Difference between measures
    
    plt.xticks(fontsize=Fontsize-6)    
    plt.yticks(fontsize=Fontsize-6)
    plt.legend(fontsize=Fontsize-6)  
    
    plt.show()
        
    return mean_difference, sd_difference