import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    data = pd.read_csv('epa-sea-level.csv')
    x = data['Year']
    y = data['CSIRO Adjusted Sea Level']
    # Create scatter plot
    fig, ax = plt.subplots(figsize=(8,5))
    ax.scatter(x,y,s=8,label='CSIRO Data')
    ax.grid()
    ax.set_xlim(1850,2075)
    

    # Create first line of best fit
    #The slope and intercept for the first best fit line
    slope1 = linregress(x,y)[0]
    intercept1 = linregress(x,y)[1]
    #xnew is data for future as precitions
    xnew = [item for item in range(2014, 2050+1)]
    xnew = pd.Series(xnew)#this makes it a pd series for ease of work
    x_fit1 = pd.concat([x,xnew])#Joins the new year data to the original
    y_fit1 = slope1*x_fit1+ intercept1 #Makes the y data for the best fit line
    
    ax.plot(x_fit1,y_fit1,'r-',label='CSIRO Best fit')

    # Create second line of best fit
    #Mask to pick out the data only from year 2000 onwards
    data_recent = data.loc[(data['Year']>1999)]
    #The x and y data for the data from year 2000 onwards
    x_recent = data_recent['Year']
    y_recent = data_recent['CSIRO Adjusted Sea Level']
    #Linear regression for the year 2000 onwards data set
    slope_recent = linregress(x_recent,y_recent)[0]
    intercept_recent = linregress(x_recent,y_recent)[1]
    #Joins the future years to the original years of 2000 onwards
    x_fit2 = pd.concat([x_recent,xnew])
    #Makes the best fit line for 2000 onwards
    y_fit2 = slope_recent*x_fit2 + intercept_recent
    
    ax.plot(x_fit2,y_fit2,'-',color='orange',label='Best fit post 2000')

    # Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    ax.legend(loc=2)
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.pdf')
    return plt.gca()
