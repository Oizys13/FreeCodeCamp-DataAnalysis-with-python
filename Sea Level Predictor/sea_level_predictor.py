from turtle import color
from grpc import intercept_channel
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def generate_sea_level_plot():
    # Load data
    data = pd.read_csv('epa-sea-level.csv')

    # Initialize plot
    figure = plt.figure()
    plt.scatter(data['Year'], data['CSIRO Adjusted Sea Level'], s=8)

    # Compute and plot the first line of best fit
    first_fit = linregress(data['Year'], data['CSIRO Adjusted Sea Level'])
    x_values1 = np.arange(data['Year'].min(), 2051, 1)
    y_values1 = first_fit.intercept + first_fit.slope * x_values1
    plt.plot(x_values1, y_values1, color='firebrick')

    # Compute and plot the second line of best fit
    recent_data = data[data['Year'] >= 2000]
    second_fit = linregress(recent_data['Year'], recent_data['CSIRO Adjusted Sea Level'])
    x_values2 = np.arange(recent_data['Year'].min(), 2051, 1)
    y_values2 = second_fit.intercept + second_fit.slope * x_values2
    plt.plot(x_values2, y_values2, color='mediumseagreen')

    # Set labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Sea Level Increase')

    # Save plot and provide access to the axis object for testing
    plt.savefig('sea_level_increase.png')
    return plt.gca()
