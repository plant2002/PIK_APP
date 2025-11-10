import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from core import db_communication

#two graphs about flights per day + all flying time of flights that got an error code per date
#not connected, not in use. Will do after presentation
#sql3 = f"SELECT * FROM faildata WHERE FN IN ({', '.join(map(str, df1['FN']))}) AND failCode = %s"
#df3 = pd.read_sql(sql3, connection[1], params=(code, ))
def FlightTimeErrorCode(df3):
    column_means = df3.mean()

    # Calculate the deviation of each value from the mean in percentage
    deviations_percentage = ((df3 - column_means) / column_means) * 100

    # Plotting
    plt.figure(figsize=(12, 8))

    # Plot horizontal bars for each flight number
    for i, fn in enumerate(df3['FN'].unique()):
        fn_data = df3.loc[df3['FN'] == fn].iloc[0]
        width_value = column_means.iloc[i]

        # Set colors based on deviations from mean
        colors = ['green' if val > 0 else 'red' for val in deviations_percentage.iloc[i]]

        # Plot horizontal bars with different colors for each deviation
        plt.barh(i, width_value, color='lightgrey')  # Main bar representing width
        plt.barh(i, fn_data, color=colors, left=[width_value] * len(fn_data))

        # Plot a red horizontal line for the mean value
        plt.axvline(x=width_value, color='red', linestyle='--', linewidth=2)

    # Set y-axis labels to flight numbers
    plt.yticks(range(len(df3['FN'].unique())), df3['FN'].unique())

    # Set x-axis limits based on mean and mean difference percentage
    max_deviation = 10 / 100 * column_means.abs().max()
    plt.xlim(column_means.min() - max_deviation, column_means.max() + max_deviation)

    plt.title('Width Deviation from Mean for Each Flight Number')
    plt.xlabel('Width Deviation from Mean')
    plt.ylabel('Flight Number')
    plt.show()
