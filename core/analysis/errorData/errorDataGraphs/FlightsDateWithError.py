import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from core import db_communication

#two graphs about flights per day + all flying time of flights that got an error code per date
#not connected, not in use. Will do after presentation
def FlightsDateWithError(df2):
    df2['GPSdt'] = pd.to_datetime(df2['GPSdt'])

    # Create a new column for the date
    df2['Date'] = df2['GPSdt'].dt.date

    # Plotting the number of flights per day
    plt.figure(figsize=(10, 6))
    df2['Date'].value_counts().sort_index().plot(kind='bar', color='skyblue', align='center')
    plt.title('Number of Flights per Day')
    plt.xlabel('Date')
    plt.ylabel('Number of Flights')
    plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better visibility
    plt.yticks(range(0, df2['Date'].value_counts().max() + 1, 1))  # Show only integer y-axis values
    plt.show()

    # Plotting the length of flights
    plt.figure(figsize=(10, 6))
    df2['fd'] = pd.to_timedelta(df2['fd'])  # Convert to timedelta
    df2['Flight Length'] = df2['fd'].dt.total_seconds() / 60  # Convert to minutes
    df2.groupby('Date')['Flight Length'].sum().plot(kind='bar', color='salmon', align='center')
    plt.title('Total Flight Length per Day')
    plt.xlabel('Date')
    plt.ylabel('Total Flight Length (minutes)')
    plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better visibility
    plt.show()