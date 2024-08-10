import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Load the dataset
df = pd.read_csv("medical_examination.csv")

# Calculate BMI and add a new column 'overweight'
df['BMI'] = df['weight'] / ((df['height'] / 100) ** 2)
df['overweight'] = (df['BMI'] > 25).astype(int)

# Normalize 'cholesterol' and 'gluc' columns so that 0 means good and 1 means bad
df['cholesterol'] = df['cholesterol'].apply(lambda x: 0 if x == 1 else 1)
df['gluc'] = df['gluc'].apply(lambda x: 0 if x == 1 else 1)

# Function to draw the categorical plot
def draw_cat_plot():
    # Reshape the dataframe for the categorical plot
    df_cat = pd.melt(df, id_vars=["cardio"], value_vars=["cholesterol", "gluc", "smoke", "alco", "active", "overweight"])
    
    # Aggregate data by the categories
    df_cat = df_cat.groupby(["cardio", "variable", "value"]).size().reset_index(name="total")
    
    # Create the categorical plot
    cat_plot = sns.catplot(x="variable", y="total", hue="value", col="cardio", data=df_cat, kind="bar")
    
    # Save and return the figure
    cat_plot.fig.savefig("catplot.png")
    return cat_plot.fig

# Function to draw the heatmap
def draw_heat_map():
    # Filter the data according to the given conditions
    df_filtered = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]
    
    # Compute the correlation matrix
    correlation_matrix = df_filtered.corr()

    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(correlation_matrix, dtype=bool))
    
    # Set up the matplotlib figure
    plt.figure(figsize=(12, 12))

    # Draw the heatmap
    heatmap = sns.heatmap(correlation_matrix, mask=mask, annot=True, fmt=".1f", linewidths=.5, square=True, center=0, vmin=-0.1, vmax=0.25, cbar_kws={"shrink": .45, "format": "%.2f"})
    
    # Save and return the figure
    plt.savefig("heatmap.png")
    return plt.gcf()
