import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from core import db_communication

#flight time per day all flights in one day together
def FlightOverallTimeDateFT(frame, date_from, date_to):

    connection = db_communication.connect_to_database()
    sql = "SELECT FN, fd, GPSdt FROM basics WHERE DATE(GPSdt) BETWEEN %s AND %s"
    
    df = pd.read_sql(sql, connection[1], params=(date_from, date_to))
    
    df['GPSdt'] = pd.to_datetime(df['GPSdt'])  # Convert GPSdt to datetime
    df['fd_minutes'] = df['fd'].dt.total_seconds() / 60
    
    grouped_df = df.groupby(df['GPSdt'].dt.date)['fd_minutes'].sum().reset_index()

    fig, ax = plt.subplots(figsize=(12, 6))  # Adjust the figure size as needed
    bars = ax.bar(grouped_df['GPSdt'].astype(str), grouped_df['fd_minutes'])

    # Annotate each bar with its value
    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, yval + 0.1, round(yval, 2), ha='center', va='bottom')

    ax.set_xlabel('')
    ax.set_ylabel('Minutes per day')
    ax.set_title('Total Minutes per Day')
    ax.tick_params(axis='x', rotation=45, ha='right')  # Rotate x-axis labels for better readability
    plt.tight_layout()

    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    canvas.draw()
    db_communication.close_connection(connection[1])
