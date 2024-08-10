import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
from pandas.plotting import register_matplotlib_converters

# Register converters for matplotlib to handle date formatting
register_matplotlib_converters()

# Load the data with date parsing and setting the index to 'date'
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=True, index_col='date')

# Filter the data to remove outliers (keeping data between 2.5th and 97.5th percentiles)
df = df[df['value'].between(df['value'].quantile(0.025), df['value'].quantile(0.975))]

def draw_line_plot():
    # Create a line plot for the forum page views data
    fig, ax = plt.subplots(figsize=(18, 6))
    ax.plot(df, color='firebrick')
    ax.set_title('Daily freeCodeCamp Forum Page Views (5/2016 - 12/2019)')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')

    # Save the plot as a PNG file and return the figure
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Prepare data for the monthly bar plot
    df_bar = df.copy()
    df_bar['Year'] = df_bar.index.year
    df_bar['Month'] = df_bar.index.month_name()

    # Reorder months for the plot
    month_order = ["January", "February", "March", "April", "May", "June", 
                   "July", "August", "September", "October", "November", "December"]
    df_bar['Month'] = pd.Categorical(df_bar['Month'], categories=month_order, ordered=True)

    # Pivot the data to create a multi-index for years and months
    df_pivot = df_bar.pivot_table(values='value', index='Year', columns='Month', aggfunc='mean')

    # Create the bar plot
    fig = df_pivot.plot(kind='bar', figsize=(10, 6)).get_figure()
    plt.xlabel('Year')
    plt.ylabel('Average Page Views')
    plt.legend(title='Month', bbox_to_anchor=(1.0, 1.0))

    # Save the plot as a PNG file and return the figure
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['Year'] = df_box['date'].dt.year
    df_box['Month'] = df_box['date'].dt.strftime('%b')

    # Reorder months for the plot
    month_order = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", 
                   "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    df_box['Month'] = pd.Categorical(df_box['Month'], categories=month_order, ordered=True)

    # Create side-by-side box plots for yearly and monthly data
    fig, axes = plt.subplots(1, 2, figsize=(18, 6))
    sns.boxplot(x='Year', y='value', data=df_box, ax=axes[0])
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')

    sns.boxplot(x='Month', y='value', data=df_box, ax=axes[1])
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')

    # Save the plot as a PNG file and return the figure
    fig.savefig('box_plot.png')
    return fig
